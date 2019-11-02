from typing import Callable
from random_dict import random_float_dict, random_int_dict
from deflate_dict import deflate
import pytest
from .dict_to_array import dict_to_array
from dict_hash import sha256
from .normalize_dict import normalize_dict
import json
import random
import os

def compare_metrics(candidate: Callable, reference: Callable, tests: int = 10) -> bool:
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
        random.seed(46)
        for _ in range(tests):
            a = normalize_dict(deflate(dict_generator(2, 10)))
            b = normalize_dict(deflate(dict_generator(2, 10)))
            assert candidate(b, a) == pytest.approx(candidate(a, b))
            assert 0 == pytest.approx(candidate(a, a))
            assert 0 == pytest.approx(candidate(b, b))
            path = "tests/references/{metric}/{sha}.json".format(
                metric=candidate.__name__,
                sha=sha256({
                    "a":a,
                    "b":b
                })
            )
            distance = candidate(a, b)
            if not os.path.exists(path):
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, "w") as f:
                    json.dump({
                        "distance":distance
                    }, f)
            with open(path, "r") as f:
                assert pytest.approx(distance) == json.load(f)["distance"]
            if reference is not None:
                try:
                    assert pytest.approx(distance) == reference(
                        *dict_to_array(a, b))
                except AssertionError as e:
                    print("Candidate {candidate} does not match {reference}: {candidate_value} != {reference_value}.".format(
                        candidate=candidate.__name__,
                        reference=reference.__name__,
                        candidate_value=candidate(a, b),
                        reference_value=reference(*dict_to_array(a, b))
                    ))
                    raise e
