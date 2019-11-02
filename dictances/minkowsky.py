"""Return the minkowsky distance beetween the given dictionaries."""
from .nth_variation import nth_variation
from typing import Dict


def minkowsky(a: Dict, b: Dict, p: int = 2) -> float:
    """Return the minkowsky distance beetween the given dictionaries.

    Parameters
    ----------------------------
    a: Dict,
        First dictionary to consider.
    b: Dict,
        Second dictionary to consider.
    P: int,
        The order of the norm of the difference.

    Raises
    ----------------------------
    ValueError:
        When the order of the norm of the difference is zero.

    Returns
    ----------------------------
    Return the minkowsky distance beetween the given dictionaries.
    """
    if p == 0:
        raise ValueError("Parameter p must be non zero.")
    return nth_variation(a, b, p)**(1 / p)
