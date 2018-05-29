"""Return the squared distance beetween a and b."""
from .nth_variation import nth_variation


def squared_variation(a: dict, b: dict, overlap: bool=False)->float:
    """Return the squared distance beetween a and b."""
    return nth_variation(a, b, 2, overlap)
