"""Return the Total Variation distance."""
from .nth_variation import nth_variation
from typing import Dict


def total_variation(a: Dict, b: Dict, overlap: bool = False) -> float:
    """Return the Total Variation distance."""
    return nth_variation(a, b, 1, overlap)
