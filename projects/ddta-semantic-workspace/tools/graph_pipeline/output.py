"""Deterministic multi-file atomic publishing with rollback if any commit fails."""
from __future__ import annotations

import os
import tempfile
from pathlib import Path

from .compose import PipelineError


def publish(files: list[tuple[Path, str]], check: bool = False) -> list[Path]:
    paths = [p.resolve() for p, _ in files]
    if len(paths) != len(set(paths)):
        raise PipelineError('Same output path requested more than once')
    payload = [(path, content.encode('utf-8')) for (path, (_, content)) in zip(paths, files)]
    changed = [path for path, data in payload if not path.exists() or path.read_bytes() != data]
    if check:
        if changed:
            raise PipelineError('OUTDATED: ' + ', '.join(str(x) for x in changed))
        return []
    # All computation and validation happen before this function is called.
    # Keep prior bytes for rollback if a filesystem error interrupts commit.
    old = {p: p.read_bytes() if p.is_file() else None for p, _ in payload}
    staged: dict[Path, Path] = {}
    committed: list[Path] = []
    try:
        for path, data in payload:
            if path not in changed:
                continue
            path.parent.mkdir(parents=True, exist_ok=True)
            fd, temp_name = tempfile.mkstemp(prefix='.ddta-pipeline-', suffix='.tmp', dir=path.parent)
            tmp = Path(temp_name)
            staged[path] = tmp
            with os.fdopen(fd, 'wb') as f:
                f.write(data)
                f.flush()
                os.fsync(f.fileno())
        for path in changed:
            os.replace(staged.pop(path), path)
            committed.append(path)
        return changed
    except Exception:
        # Undo even a partly committed set. Best-effort rollback is needed only
        # for OS/disk failures; any semantic or parsing error occurs before writes.
        for path in reversed(committed):
            prev = old[path]
            if prev is None:
                path.unlink(missing_ok=True)
            else:
                path.write_bytes(prev)
        raise
    finally:
        for tmp in staged.values():
            tmp.unlink(missing_ok=True)
