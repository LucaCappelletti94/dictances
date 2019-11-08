from dictances import canberra, chebyshev, chi_square, cityblock, cosine, manhattan, total_variation, euclidean, minkowsky, mse, mae, bhattacharyya, kullback_leibler, jensen_shannon
from dictances import hamming, intersection_nth_variation, intersection_squared_hellinger, intersection_squared_variation, intersection_total_variation, pearson
from scipy.spatial import distance
from sklearn.metrics import mean_squared_error, mean_absolute_error
from scipy.stats import chisquare, entropy
from .utils import compare_metrics, bhattacharyya_distance, jensen_shannon_divergence
from tqdm.auto import tqdm
import pytest

candidates = {
    canberra: distance.canberra,
    chebyshev: distance.chebyshev,
    chi_square: chisquare,
    cityblock: distance.cityblock,
    manhattan: distance.cityblock,
    total_variation: distance.cityblock,
    cosine: distance.cosine,
    euclidean: distance.euclidean,
    jensen_shannon: jensen_shannon_divergence,
    minkowsky: distance.minkowski,
    mse: mean_squared_error,
    mae: mean_absolute_error,
    bhattacharyya: bhattacharyya_distance,
    kullback_leibler: entropy,
    hamming: None,
    intersection_nth_variation: None,
    intersection_squared_hellinger: None,
    intersection_squared_variation: None,
    intersection_total_variation: None,
    pearson: None
}


def test_dictances():
    """Run tests on each metric."""
    for candidate, reference in tqdm(candidates.items(), total=len(candidates), desc="Testing dictances"):
        compare_metrics(candidate, reference)
    with pytest.raises(AssertionError):
        compare_metrics(canberra, distance.cosine)


def test_invalid_minkowsky():
    with pytest.raises(ValueError):
        minkowsky({}, {}, 0)
