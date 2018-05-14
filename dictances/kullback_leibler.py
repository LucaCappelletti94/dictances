from .distances_utils import sort
from math import log
def kullback_leibler(a:dict, b:dict) -> float:
    """Determines the Kullback–Leibler divergence"""
    total = 0
    big, small = sort(a,b)
    big_get = big.get
    for key, small_value in a.items():
        big_value = big_get(key)
        if big_value:
            total += small_value*log(small_value/big_value)
    return round(total,14)