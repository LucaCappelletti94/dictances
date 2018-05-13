from .distances_utils import sort
from math import sqrt
def hellinger(a:dict, b:dict) -> float:
    """Determines the Hellinger distance"""
    total = 0
    big, small = sort(a,b)
    big_get = big.get
    for key, small_value in small.items():
        big_value = big_get(key)
        if big_value:
            total += (sqrt(small_value)-sqrt(big_value))**2
    return round(sqrt(total)/sqrt(2),14)