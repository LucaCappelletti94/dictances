import math

def euclidean(a:dict, b:dict)->float:
    total = 0
    aget = a.get
    bget = b.get
    for k in (set(a) | set(b)):
        total += (aget(k,0)-bget(k,0))**2
    return math.sqrt(total)