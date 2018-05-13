from math import sqrt
def cosine(a:dict, b:dict)->float:
    """Returns the cosine distance beetween a and b"""
    prod_ab = 0
    sqr_a = 0
    sqr_b = 0
    aget = a.get
    bget = b.get
    for k in a:
        aval = aget(k)
        bval = bget(k,0)
        sqr_a += aval**2
        sqr_b += bval**2
        prod_ab += bval*aval
    return round(prod_ab/(sqrt(sqr_a)*sqrt(sqr_b)),14)
