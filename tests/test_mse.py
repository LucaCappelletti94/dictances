from distances import mse
from utils import create_cases

def test_mse():
    a, b = create_cases()
    assert mse(a,b) == 0.00013567081521