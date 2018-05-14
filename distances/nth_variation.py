def even_nth(a_val:float, b_val:float)->float:
    return a_val-b_val

def odd_nth(a_val:float, b_val:float)->float:
    return abs(a_val-b_val)

def nth_variation(a:dict, b:dict, exponent=2, overlap = False)->float:
    """Returns the nth power distance beetween a and b"""
    total = 0
    n = 0
    bget = b.get

    if exponent%2==0:
        nth = even_nth
    else:
        nth = odd_nth

    for k, a_val in a.items():
        b_val = bget(k)
        if b_val:
            total += nth(a_val, b_val)**exponent
        else:
            total += a_val**exponent
        n+=1
    for k, b_val in b.items():
        if k not in a:
            total += b_val**exponent
            n+=1
    result = round(total,14)
    if overlap:
        return result, n
    return result