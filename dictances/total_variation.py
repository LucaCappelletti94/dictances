"""Return the Total Variation distance."""

from typing import Dict
from dictances.nth_variation import nth_variation


def total_variation(a: Dict, b: Dict, overlap: bool = False) -> float:
    """Return the Total Variation distance."""
    return nth_variation(a, b, 1, overlap)
