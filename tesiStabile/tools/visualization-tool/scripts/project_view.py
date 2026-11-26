"""Avvio autonomo di project_view da qualunque directory, senza PYTHONPATH."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from ddta_viz.project_view import main

if __name__ == "__main__":
    raise SystemExit(main())
