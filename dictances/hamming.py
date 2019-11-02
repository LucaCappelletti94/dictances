"""Return the hamming distance beetween a and b."""
from typing import Dict

def hamming(a: Dict, b: Dict)->float:
    """Return the hamming distance beetween a and b."""
    common = 0
    bget = b.__getitem__
    for k in a:
        try:
            bget(k)
            common += 1
        except KeyError:
            pass
    return len(a) + len(b) - common * 2
