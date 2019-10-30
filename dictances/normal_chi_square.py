"""Return the normalized chi square distance beetween a and b."""

def normal_chi_square(a: dict, b: dict)->float:
    """Return the normalized chi square distance beetween a and b."""

    a_factor = 1.0/sum(a.values())
    b_factor = 1.0/sum(b.values())
    total = 0
    for k, aval in a.items():
        aval = aval*a_factor
        try:
            bval = b[k]*b_factor
            total += (aval - bval) * (aval - bval) / (aval + bval)
        except KeyError:
            total += aval

    for k in b:
        try:
            a[k]
        except KeyError:
            total += b[k]*b_factor

    return total
