from .nth_variation import nth_variation
def minkowsky(a:dict, b:dict, p:float)->float:
    if p == 0:
        raise ValueError("Parameter p must be non zero.")
    """Returns the euclideam distance beetween a and b"""
    return round((nth_variation(a,b,p)**(1/p)),14)