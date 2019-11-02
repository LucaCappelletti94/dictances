"""Return the euclidean distance beetween the given dictionaries."""
from .minkowsky import minkowsky
from typing import Dict


def euclidean(a: Dict, b: Dict)->float:
    """Return the euclidean distance beetween the given dictionaries.

    Parameters
    ----------------------------
    a: Dict,
        First dictionary to consider.
    b: Dict,
        Second dictionary to consider.

    Returns
    ----------------------------
    Return the euclidean distance beetween the given dictionaries.
    """
    return minkowsky(a, b, 2)
