from distances import hamming
from utils import create_cases

def test_hamming():
    a, b = create_cases()
    assert hamming(a,b) == 167