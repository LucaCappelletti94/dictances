from .distances_utils import sort
from math import sqrt, log

def bhattacharyya_coefficient(a:dict, b:dict) -> float:
    """Determines the bhattacharyya coefficient"""
    total = 0
    big, small = sort(a,b)
    big_get = big.get
    for k,small_value in small.items():
        big_value = big_get(k)
        if big_value:
            total += sqrt(big_value*small_value)
    return total

def bhattacharyya(a:dict, b:dict) -> float:
    """Determines the bhattacharyya distance"""
    return round(-log(bhattacharyya_coefficient(a,b)),14)