"""Return the squared distance beetween a and b."""

from typing import Dict
from dictances.nth_variation import nth_variation


def squared_variation(a: Dict, b: Dict, overlap: bool = False) -> float:
    """Return the squared distance beetween a and b."""
    return nth_variation(a, b, 2, overlap)
