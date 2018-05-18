from .nth_variation import nth_variation


def squared_variation(a: dict, b: dict, overlap=False)->float:
    """Returns the squared distance beetween a and b"""
    return nth_variation(a, b, 2, overlap)
