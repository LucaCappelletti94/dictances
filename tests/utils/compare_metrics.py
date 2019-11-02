from typing import Callable
from random_dict import random_float_dict, random_int_dict
from deflate_dict import deflate
import pytest
from .dict_to_array import dict_to_array


def compare_metrics(candidate: Callable, reference: Callable, tests: int = 2) -> bool:
    """Test if candidate metric is identical within float error to reference metric.

    Parameters
    -------------------------------------------
    candidate: Callable,
        The metric to be tested.
    reference: Callable,
        The reference metric considered as ground truth.
    tests: int = 10,
        Number of random dictionaries (both float and integer) to test.

    Returns
    --------------------------------------------
    Boolean value with the test result.
    """
    for dict_generator in (random_float_dict, random_int_dict):
        for _ in range(tests):
            a = deflate(dict_generator(3, 50))
            b = deflate(dict_generator(3, 50))
            assert pytest.approx(candidate(a, b), candidate(b, a))
            assert pytest.approx(candidate(a, a), 0)
            assert pytest.approx(candidate(b, b), 0)
            assert pytest.approx(candidate(a, b), reference(*dict_to_array(a, b)))