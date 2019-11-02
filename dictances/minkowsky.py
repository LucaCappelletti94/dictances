"""Return the minkowsky distance beetween a and b."""
from .nth_variation import nth_variation
from typing import Dict

def minkowsky(a: Dict, b: Dict, p=2)->float:
    """Return the minkowsky distance beetween a and b."""
    if p == 0:
        raise ValueError("Parameter p must be non zero.")
    return nth_variation(a, b, p)**(1 / p)
