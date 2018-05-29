"""Return the euclidean distance beetween a and b."""
from .minkowsky import minkowsky


def euclidean(a: dict, b: dict)->float:
    """Return the euclidean distance beetween a and b."""
    return round(minkowsky(a, b, 2), 14)
