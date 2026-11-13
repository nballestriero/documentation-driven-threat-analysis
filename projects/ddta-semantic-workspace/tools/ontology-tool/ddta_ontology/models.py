"""Modelli dati tra le fasi: nessuna logica RDF o di file system."""

from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Record:
    """Una scheda YAML estratta dal Markdown.

    Attributes:
        module: Identificatore del modulo dichiarato nella scheda YAML.
        source: Percorso del documento che contiene la scheda.
        ordinal: Posizione del blocco normativo nel documento (partendo da 1).
        line: Riga iniziale nel Markdown, utile per correggere gli errori.
        body: Dati del blocco YAML convertiti in dizionario Python.
    """

    module: str
    source: Path
    ordinal: int
    line: int
    body: dict[str, Any]

    @property
    def context(self) -> str:
        """Restituisce il riferimento leggibile alla posizione della scheda."""
        return f"{self.source}:{self.line} (yaml ddta-ontology #{self.ordinal})"
