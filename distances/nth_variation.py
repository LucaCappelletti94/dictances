def nth_variation(a:dict, b:dict, exponent:float, overlap = False)->float:
    """Returns the nth power distance beetween a and b"""
    total = 0
    n = 0
    aget = a.get
    bget = b.get
    for k in a:
        total += abs(aget(k)-bget(k,0))**exponent
        n+=1
    for k in b:
        if k not in a:
            total += bget(k)**exponent
            n+=1
    result = round(total,14)
    if overlap:
        return result, n
    return result