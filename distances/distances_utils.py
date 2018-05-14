def sort(a:dict,b:dict):
    """Returns the bigger dict, then the smaller one"""
    if len(a)>len(b):
        return a,b
    return b,a