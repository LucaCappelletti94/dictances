from .distances_utils import sort
from math import log

def jensen_shannon(a:dict, b:dict)->float:
    """Returns the jensen shannon divergence beetween a and b"""
    total = 0
    delta = 0
    big, small = sort(a,b)

    big_get = big.get

    for key, value in small.items():
        ov = big_get(key)
        if ov:
            denominator = (ov + value)/2
            total += value*log(value/denominator) + ov*log(ov/denominator)
            delta -= ov
        else:
            delta += value

    total += (1+delta)*log(2)
    return round(total/2,14)