"""Return the chi square distance beetween a and b."""

def chi_square(a: dict, b: dict)->float:
    """Return the chi square distance beetween a and b."""

    total = 0
    for k, aval in a.items():
        try:
            bval = b[k]
            total += (aval - bval) * (aval - bval) / (aval + bval)
        except KeyError:
            total += aval

        for k in b:
            try:
                a[k]
            except KeyError:
                total += b[k]

    return total
