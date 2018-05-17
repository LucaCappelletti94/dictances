from .total_variation import total_variation
from .distances_utils import mean

def mae(a,b):
    return mean(a,b,total_variation)