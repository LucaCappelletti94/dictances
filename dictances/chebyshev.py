def chebyshev(a: dict, b: dict) -> float:
    """Determines the Chebyshev distance"""
    result = 0
    bget = b.get
    for key, a_val in a.items():
        b_val = bget(key)
        if b_val:
            result = max(result, abs(a_val - b_val))
        else:
            result = max(result, a_val)
    for key, b_val in b.items():
        if key not in a:
            result = max(result, b_val)
    return round(result, 14)
