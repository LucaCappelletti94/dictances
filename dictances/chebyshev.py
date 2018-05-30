"""Determine the Chebyshev distance."""


def chebyshev(a: dict, b: dict) -> float:
    """Determine the Chebyshev distance."""
    result = 0
    bget = b.__getitem__
    aget = a.__getitem__
    for key, a_val in a.items():
        try:
            result = max(result, abs(a_val - bget(key)))
        except KeyError:
            result = max(result, a_val)
    for key, b_val in b.items():
        try:
            aget(key)
        except KeyError:
            result = max(result, b_val)
    return result
