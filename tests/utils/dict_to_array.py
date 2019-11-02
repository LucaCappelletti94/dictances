import numpy as np
from typing import Tuple, Dict
from .align_dict import align_dictionaries


def dict_to_array(a: Dict, b: Dict) -> Tuple[np.ndarray, np.ndarray]:
    """Return tuple of arrays representing given dictionaries.

    Parameters
    ------------------------------
    a: Dict,
        First dictionary to turn into aligned array.
    b: Dict,
        Second dictionary to turn into aligned array.

    Returns
    -------------------------------
    Tuple containing the two dictonaries turned into alligned arrays.
    """
    a = align_dictionaries(a, b)
    b = align_dictionaries(b, a)
    return np.array([
        (a[key], b[key]) for key in a.keys()
    ]).T
