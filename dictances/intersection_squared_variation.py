"""Return the squared distance beetween the intersection of a and b."""
from .intersection_nth_variation import intersection_nth_variation


def intersection_squared_variation(a: dict, b: dict, overlap: bool=False)->float:
    """Return the squared distance beetween the intersection of a and b."""
    return intersection_nth_variation(a, b, 2, overlap)
