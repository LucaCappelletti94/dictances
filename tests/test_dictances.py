from dictances import canberra, chebyshev, cityblock, cosine, manhattan, total_variation, euclidean
from scipy.spatial import distance
from .utils import compare_metrics
from tqdm.auto import tqdm

candidates = {
    canberra: distance.canberra,
    chebyshev: distance.chebyshev,
    cityblock: distance.cityblock,
    manhattan: distance.cityblock,
    total_variation: distance.cityblock,
    cosine: distance.cosine,
    euclidean: distance.euclidean,
}

def test_dictances():
    """Run tests on each metric."""
    for candidate, reference in tqdm(candidates.items(), total=len(candidates), desc="Testing dictances"):
        compare_metrics(candidate, reference)