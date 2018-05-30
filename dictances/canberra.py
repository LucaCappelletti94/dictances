"""Return the canberra distance beetween a and b."""


def canberra(a: dict, b: dict)->float:
    """Return the canberra distance beetween a and b."""
    total = 0
    bget = b.__getitem__
    aget = a.__getitem__
    for k, aval in a.items():
        try:
            bval = bget(k)
            total += abs(aval - bval) / (aval + bval)
        except KeyError as e:
            total += 1
    for k in b:
        try:
            aget(k)
        except KeyError:
            total += 1
    return total
