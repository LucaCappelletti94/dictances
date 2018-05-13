from .squared_variation import squared_variation

def MSE(a,b):
    result, n = squared_variation(a,b,overlap=True)
    return round(result/n,14)