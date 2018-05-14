from .total_variation import total_variation

def mae(a,b):
    result, n = total_variation(a,b,overlap=True)
    return round(result/n,14)