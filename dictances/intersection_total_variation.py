"""Return the total distance beetween the intersection of a and b."""
from .intersection_nth_variation import intersection_nth_variation


def intersection_total_variation(a: dict, b: dict, overlap: bool=False)->float:
    """Return the total distance beetween the intersection of a and b."""
    return intersection_nth_variation(a, b, 1, overlap)
