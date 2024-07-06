from dictances import (
    canberra,
    chebyshev,
    chi_square,
    cityblock,
    cosine,
    manhattan,
    total_variation,
    euclidean,
    minkowsky,
    mse,
    mae,
    bhattacharyya,
)
from dictances import (
    kullback_leibler,
    jensen_shannon,
    hamming,
    intersection_nth_variation,
    intersection_squared_hellinger,
    intersection_squared_variation,
)
from dictances import intersection_total_variation, pearson, normal_chi_square
from scipy.spatial import distance
from sklearn.metrics import mean_squared_error, mean_absolute_error
from scipy.stats import entropy
from .utils import (
    compare_metrics,
    bhattacharyya_distance,
    chi_square_distance,
    jensen_shannon_divergence,
    normal_chi_square_distance,
)
from tqdm.auto import tqdm
import pytest

candidates = {
    bhattacharyya: bhattacharyya_distance,
    canberra: distance.canberra,
    chebyshev: distance.chebyshev,
    chi_square: chi_square_distance,
    cityblock: distance.cityblock,
    cosine: distance.cosine,
    euclidean: distance.euclidean,
    jensen_shannon: jensen_shannon_divergence,
    kullback_leibler: entropy,
    mae: mean_absolute_error,
    manhattan: distance.cityblock,
    minkowsky: distance.minkowski,
    mse: mean_squared_error,
    normal_chi_square: normal_chi_square_distance,
    total_variation: distance.cityblock,
    hamming: None,
    intersection_nth_variation: None,
    intersection_squared_hellinger: None,
    intersection_squared_variation: None,
    intersection_total_variation: None,
    pearson: None,
}


def test_dictances():
    """Run tests on each metric."""
    for candidate, reference in tqdm(
        candidates.items(), total=len(candidates), desc="Testing dictances", leave=False
    ):
        compare_metrics(candidate, reference)
    with pytest.raises(AssertionError):
        compare_metrics(canberra, distance.cosine)


def test_invalid_minkowsky():
    """Test invalid input for minkowsky."""
    with pytest.raises(ValueError):
        minkowsky({}, {}, 0)


def test_intersection_nth_variation():
    """Test the intersection_nth_variation function."""
    a = {"a": 1, "b": 2, "c": 3}
    b = {"b": 2, "c": 3, "d": 4}
    assert intersection_nth_variation(a, a, 1, overlap=True)[0] == 0
    assert intersection_nth_variation(a, b, 1, overlap=True)[0] == 0
    assert intersection_nth_variation(a, b, 1, overlap=True)[1] == 2
