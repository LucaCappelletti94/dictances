from typing import Dict
import copy


def align_dictionaries(a: Dict, b: Dict) -> Dict:
    """Return dictionary a aligned to dictionary b.

    Parameters
    ---------------------------------
    a: Dict,
        The dictionary to be aligned to the second one, adding missing keys to values 0 as required.
    b: Dict,
        The dictionary to align to.
    
    Returns
    ----------------------------------
    Aligned dictionary a.
    """
    a = copy.deepcopy(a)
    for key in set(b.keys()) - set(a.keys()):
        a[key] = 0
    return a