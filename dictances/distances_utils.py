"""Generic utils used through all the package."""


def sort(a: dict, b: dict):
    """Return the bigger dict, then the smaller one."""
    if len(a) > len(b):
        return a, b
    return b, a


def mean(a, b, distance):
    """Return the mean of the given distance."""
    result, n = distance(a, b, overlap=True)
    return round(result / n, 14)
