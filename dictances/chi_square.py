"""Return the chi square distance beetween a and b."""
from typing import Dict

def chi_square(a: Dict, b: Dict)->float:
    """Return the chi square distance beetween a and b."""

    total = 0
    for k, aval in a.items():
        try:
            bval = b[k]
            total += (aval - bval) * (aval - bval) / (aval + bval)
        except KeyError:
            total += aval

    for k in b:
        try:
            a[k]
        except KeyError:
            total += b[k]

    return total
