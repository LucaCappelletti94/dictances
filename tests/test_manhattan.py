from distances import manhattan
from utils import create_cases

def test_manhattan():
    a, b = create_cases()
    assert manhattan(a,b) == 1.80865306195869