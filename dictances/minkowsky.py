"""Return the minkowsky distance beetween a and b."""
from .nth_variation import nth_variation


def minkowsky(a: dict, b: dict, p=2)->float:
    """Return the minkowsky distance beetween a and b."""
    if p == 0:
        raise ValueError("Parameter p must be non zero.")
    return nth_variation(a, b, p)**(1 / p)
