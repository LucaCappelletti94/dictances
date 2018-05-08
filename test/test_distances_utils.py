from distances.distances_utils import sort
from utils import create_case

def test_answer():
    a = create_case(n=10)
    b = create_case(n=100)
    assert b,a == sort(a,b)