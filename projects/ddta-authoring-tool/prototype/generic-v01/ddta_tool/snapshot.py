"""Single shared snapshot entrypoint for editor adapters and CLI.

DDTA-FR: FR-MR01-01-01
DDTA-FR: FR-MR01-01-03
"""
from __future__ import annotations
from pathlib import Path
from .engine import DEFAULT_SCHEMAS, validate
from .relations import check_workspace


def check_snapshot(workspace: Path, document: Path, text: str, *,
                   profile: str = 'draft', schemas_dir: Path = DEFAULT_SCHEMAS) -> dict:
    """Validate unsaved text and its declared relations without modifying files.

    The document must already be an in-scope file. New unsaved documents and
    broader snapshot collections are intentionally deferred.
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    workspace = Path(workspace).resolve()
    document = Path(document)
    target = (workspace / document).resolve() if not document.is_absolute() else document.resolve()
    if not target.is_relative_to(workspace):
        raise ValueError('Snapshot target escapes the selected workspace')
    rel = target.relative_to(workspace).as_posix()
    # No separate interpretation in the editor/CLI. Both invoke the same code.
    document_result = validate(text, profile, schemas_dir)
    workspace_result = check_workspace(workspace, profile, schemas_dir, {rel: text})
    return {'snapshot': rel, 'document': document_result.as_dict(),
            'workspace': workspace_result.as_dict(),
            'valid': document_result.valid and workspace_result.valid}
