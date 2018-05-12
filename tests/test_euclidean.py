from distances import euclidean
from utils import create_cases

def test_euclidean():
    a, b = create_cases()
    assert euclidean(a,b) == 7.76683290336959