"""Return the total distance beetween the intersection of a and b."""

from typing import Dict
from dictances.intersection_nth_variation import intersection_nth_variation


def intersection_total_variation(a: Dict, b: Dict, overlap: bool = False) -> float:
    """Return the total distance beetween the intersection of a and b."""
    return intersection_nth_variation(a, b, 1, overlap)
