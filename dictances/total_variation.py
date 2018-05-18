from .nth_variation import nth_variation


def total_variation(a: dict, b: dict, overlap=False) -> float:
    """Determines the Total Variation distance"""
    return nth_variation(a, b, 1, overlap)
