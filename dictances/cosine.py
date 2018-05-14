from math import sqrt
def cosine(a:dict, b:dict)->float:
    """Returns the cosine distance beetween a and b"""
    prod_ab = 0
    sqr_a = 0
    sqr_b = 0
    bget = b.get
    for k, a_val in a.items():
        b_val = bget(k,0)
        sqr_a += a_val**2
        if b_val:
            prod_ab += b_val*a_val

    for k, b_val in b.items():
        sqr_b += b_val**2

    return 1-round(prod_ab/(sqrt(sqr_a)*sqrt(sqr_b)),14)
