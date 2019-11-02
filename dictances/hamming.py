"""Return the Hamming distance beetween the given dictionaries."""
from typing import Dict

def hamming(a: Dict, b: Dict)->float:
    """Return the Hamming distance beetween the given dictionaries.

    Parameters
    ----------------------------
    a: Dict,
        First dictionary to consider.
    b: Dict,
        Second dictionary to consider.

    Returns
    ----------------------------
    Return the Hamming distance beetween the given dictionaries.
    """
    common = 0
    bget = b.__getitem__
    for k in a:
        try:
            bget(k)
            common += 1
        except KeyError:
            pass
    return len(a) + len(b) - common * 2
