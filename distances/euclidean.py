from math import sqrt
from .squared_variation import squared_variation
def euclidean(a:dict, b:dict)->float:
    """Returns the euclideam distance beetween a and b"""
    return round(sqrt(squared_variation(a,b)),14)