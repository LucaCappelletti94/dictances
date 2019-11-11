"""Return the chi square distance beetween the two given dictionaries."""
from typing import Dict


def chi_square(a: Dict, b: Dict) -> float:
    """Return the chi square distance beetween the two given dictionaries.

    Parameters
    ----------------------------
    a: Dict,
        First dictionary to consider.
    b: Dict,
        Second dictionary to consider.

    Returns
    ----------------------------
    Return the chi square distance beetween the two given dictionaries.
    """

    total = 0
    for k, aval in a.items():
        try:
            bval = b[k]
            total += (aval - bval) * (aval - bval) / (aval + bval)
        except KeyError:
            total += aval

    for k in b:
        if k not in a:
            total += b[k]

    return total
