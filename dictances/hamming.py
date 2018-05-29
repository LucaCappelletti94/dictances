"""Return the hamming distance beetween a and b."""


def hamming(a: dict, b: dict)->float:
    """Return the hamming distance beetween a and b."""
    common = 0
    bget = b.__getitem__
    for k in a:
        try:
            bget(k)
            common += 1
        except KeyError:
            pass
    return len(a) + len(b) - common * 2
