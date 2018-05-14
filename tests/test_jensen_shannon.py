from distances import jensen_shannon
from utils import create_cases

def test_jensen_shannon():
    a, b = create_cases()
    assert jensen_shannon(a,b) == 0.6098897698032