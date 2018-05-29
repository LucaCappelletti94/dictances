"""Return the mean total total variation."""
from .distances_utils import mean
from .total_variation import total_variation


def mae(a, b):
    """Return the mean total total variation."""
    return mean(a, b, total_variation)
