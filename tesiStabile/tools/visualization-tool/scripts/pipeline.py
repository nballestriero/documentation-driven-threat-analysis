"""Avvio autonomo di pipeline da qualunque directory, senza PYTHONPATH."""
from pathlib import Path
import sys
import os

# Do not leave generated Python caches inside the stable DDTA workspace.
sys.dont_write_bytecode = True
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
# Unico punto d'ingresso DDTA: CORE invariato per default; PROCESS opzionale.
# PROCESS R5: modular extension under tools/visualization-tool/src.
if __name__ == "__main__":
    if "--process-guide" in sys.argv[1:]:
        from ddta_process_pipeline import main as process_main
        raise SystemExit(process_main(sys.argv[1:]))
    from ddta_viz.pipeline import main as core_main
    raise SystemExit(core_main(sys.argv[1:]))
