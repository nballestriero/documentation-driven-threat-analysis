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
    # Existing MR/Decision/FR retain all cross-document identity/link checks.
    # A new schema-driven type has no declared cross-document relation policy yet:
    # expose its *document* diagnostics to the same editor response protocol,
    # explicitly mark that relation checking was not performed.
    from .relations import DOCUMENT_FOLDERS
    folder = rel.split('/')[0]
    if folder in DOCUMENT_FOLDERS:
        workspace_result = check_workspace(workspace, profile, schemas_dir, {rel: text})
        return {'snapshot': rel, 'document': document_result.as_dict(),
                'workspace': workspace_result.as_dict(),
                'relationsChecked': True,
                'valid': document_result.valid and workspace_result.valid}
    if workspace.name != 'docs' or len(rel.split('/')) < 2:
        raise ValueError('New document types must be under a docs/ child folder')
    from .relations import DOCUMENT_TYPES
    if document_result.document_type in DOCUMENT_TYPES:
        raise ValueError('Existing linked document types must use their governed workspace folders')
    from .relations import RelationDiagnostic, WorkspaceResult
    ds = [RelationDiagnostic(rel, d.code, d.severity, d.message, d.line, d.column)
          for d in document_result.diagnostics]
    workspace_result = WorkspaceResult(str(workspace), profile, 1, ds, document_result.complete)
    return {'snapshot': rel, 'document': document_result.as_dict(),
            'workspace': workspace_result.as_dict(),
            'relationsChecked': False,
            'valid': document_result.valid}
