from math import sqrt
from .minkowsky import minkowsky
def euclidean(a:dict, b:dict)->float:
    """Returns the euclideam distance beetween a and b"""
    return round(minkowsky(a,b,2),14)