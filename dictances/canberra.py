def canberra(a: dict, b: dict)->float:
    """Returns the canberra distance beetween a and b"""
    total = 0
    aget = a.get
    bget = b.get
    for k in a:
        aval = aget(k)
        bval = bget(k)
        if bval:
            total += abs(aval-bval)/(aval+bval)
        else:
            total += 1
    for k in b:
        if k not in a:
            total += 1
    return round(total, 14)
