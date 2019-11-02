"""Determine the Hellinger distance."""
from math import isclose, sqrt
from typing import Dict
from .squared_hellinger import squared_hellinger


def hellinger(a: Dict, b: Dict) -> float:
    """Determine the Hellinger distance."""
    try:
        v = squared_hellinger(a, b)
        return sqrt(v)
    except ValueError as e:
        if isclose(v, 0, abs_tol=1e-15):
            return 0
        raise e
