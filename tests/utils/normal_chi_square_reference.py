import numpy as np
from scipy.stats import chisquare

def normal_chi_square_distance(repr1: np.ndarray, repr2: np.ndarray) -> float:
    repr1.tolist()
    repr2.tolist()
    # Normalization of list adapted from https://stackoverflow.com/a/26785464/2941352
    repr1 = [float(x)/sum(repr1) for x in repr1]
    repr2 = [float(x)/sum(repr2) for x in repr2]
    dist_sum = 0

    for x in range(max(len(repr1), len(repr2))):
        val1 = 0
        val2 = 0

        try:
            val1 = repr1[x]
        except IndexError:
            pass

        try:
            val2 = repr2[x]
        except IndexError:
            pass

        dist_sum += chisquare([val1,val2])[0]
    return dist_sum