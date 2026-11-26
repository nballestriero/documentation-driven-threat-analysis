"""Errori di input validati con un messaggio comprensibile all'autore."""


class OntologySourceError(ValueError):
    """Indica una scheda non conforme: nessun Turtle deve essere pubblicato."""


def require(condition: bool, message: str) -> None:
    """Solleva OntologySourceError quando una condizione obbligatoria non vale.

    Args:
        condition: Condizione da verificare.
        message: Descrizione del problema con contesto della scheda.
    """
    if not condition:
        raise OntologySourceError(message)
