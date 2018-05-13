def total_variation(a:dict, b:dict) -> float:
    """Determines the Total Variation distance"""
    total = 0
    aget = a.get
    bget = b.get
    for key in a:
        total += abs(aget(key,0) - bget(key,0))
    for key in b:
        if key not in a:
            total += bget(key,0)
    return round(total,14)