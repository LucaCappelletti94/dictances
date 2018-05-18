def hamming(a: dict, b: dict)->float:
    """Returns the hamming distance beetween a and b"""
    common = 0
    for k in a:
        if k in b:
            common += 1
    return len(a) + len(b) - common*2
