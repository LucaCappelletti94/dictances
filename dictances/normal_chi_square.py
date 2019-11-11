"""Return the normalized chi square distance beetween the two given dictionaries."""
from typing import Dict


def normal_chi_square(a: Dict, b: Dict) -> float:
    """Return the normalized chi square distance beetween the two given dictionaries.

    Parameters
    ----------------------------
    a: Dict,
        First dictionary to consider.
    b: Dict,
        Second dictionary to consider.

    Returns
    ----------------------------
    Return the normalized chi square distance beetween the two given dictionaries.
    """

    a_factor = 1.0/sum(a.values())
    b_factor = 1.0/sum(b.values())
    total = 0
    for k, aval in a.items():
        aval = aval*a_factor
        try:
            bval = b[k]*b_factor
            total += (aval - bval) * (aval - bval) / (aval + bval)
        except KeyError:
            total += aval

    for k in b:
        if k not in a:
            total += b[k]*b_factor

    return total
