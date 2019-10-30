"""Return the chi square distance beetween a and b."""

def chi_square(a: dict, b: dict)->float:
    """Return the chi square distance beetween a and b."""

    # Chi Square requires normalized values (sum to 1), so normalize a and b to a_norm and b_norm.
    a_norm = dict()
    factor = 1.0/sum(a.values())
    for k in a:
        a_norm[k] = a[k]*factor

    b_norm = dict()
    factor = 1.0/sum(b.values())
    for k in b:
        b_norm[k] = b[k]*factor

    # After normalizing, do the math.
    total = 0
    for k, aval in a_norm.items():
        try:
            bval = b_norm[k]
            total += (aval - bval) * (aval - bval) / (aval + bval)
        except KeyError:
            total += aval

        for k in b_norm:
            try:
                a_norm[k]
            except KeyError:
                total += b_norm[k]

    return total
