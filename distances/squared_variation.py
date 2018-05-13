def squared_variation(a:dict, b:dict)->float:
    """Returns the squared distance beetween a and b"""
    total = 0
    aget = a.get
    bget = b.get
    for k in a:
        total += (aget(k)-bget(k,0))**2
    for k in b:
        if k not in a:
            total += bget(k)**2
    return round(total,14)