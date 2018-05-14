from dictances.distances_utils import sort
from utils import create_case

def test_distances_utils():
    a = create_case(n=10)
    b = create_case(n=100)
    assert ((b,a),(b,a)) == (sort(a,b), sort(b,a))