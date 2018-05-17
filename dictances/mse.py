from .squared_variation import squared_variation
from .distances_utils import mean

def mse(a,b):
    return mean(a,b,squared_variation)