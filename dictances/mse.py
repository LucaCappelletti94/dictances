"""Return the mean total squared variation."""
from .distances_utils import mean
from .squared_variation import squared_variation


def mse(a, b):
    """Return the mean total squared variation."""
    return mean(a, b, squared_variation)
