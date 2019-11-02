"""Return the squared distance beetween the intersection of a and b."""
from .intersection_nth_variation import intersection_nth_variation
from typing import Dict

def intersection_squared_variation(a: Dict, b: Dict, overlap: bool=False)->float:
    """Return the squared distance beetween the intersection of a and b."""
    return intersection_nth_variation(a, b, 2, overlap)
