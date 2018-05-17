def sort(a:dict,b:dict):
    """Returns the bigger dict, then the smaller one"""
    if len(a)>len(b):
        return a,b
    return b,a

def mean(a,b,distance):
    result, n = distance(a,b,overlap=True)
    return round(result/n,14)