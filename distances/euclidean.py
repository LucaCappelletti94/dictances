import math

def euclidean(a:dict, b:dict)->float:
    total = 0
    aget = a.get
    bget = b.get
    for k in a:
        total += (aget(k)-bget(k,0))**2
    for k in b:
        if k not in a:
            total += bget(k)**2
    return math.sqrt(total)