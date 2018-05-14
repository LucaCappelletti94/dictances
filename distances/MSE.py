from .squared_variation import squared_variation

def mse(a,b):
    result, n = squared_variation(a,b,overlap=True)
    return round(result/n,14)