from distances import euclidean
from utils import create_cases

def test_euclidean():
    a1, b1 = create_cases()
    a2, b2 = create_cases()
    a3, b3 = create_cases()
    assert (
        euclidean(a1,b1),
        euclidean(a2,b2),
        euclidean(a3,b3)
    ) == (
        7.740234942251407,
        8.071735136209226,
        7.8618714274105255
    )