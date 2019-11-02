import numpy as np


def bhattacharyya_distance(repr1: np.ndarray, repr2: np.ndarray) -> float:
    """Calculates Bhattacharyya distance (https://en.wikipedia.org/wiki/Bhattacharyya_distance)."""
    value = - np.log(np.sum([np.sqrt(p*q) for (p, q) in zip(repr1, repr2)]))
    if np.isinf(value):
        return 0
    return value