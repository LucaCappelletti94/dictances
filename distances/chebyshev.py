def chebyshev(a:dict, b:dict) -> float:
    """Determines the Chebyshev distance"""
    result = 0
    aget = a.get
    bget = b.get
    for key in a:
        result = max(result, abs(aget(key,0) - bget(key,0)))
    for key in b:
        if key not in a:
            result = max(result, bget(key,0))
    return round(result,14)