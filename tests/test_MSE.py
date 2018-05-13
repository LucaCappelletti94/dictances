from distances import MSE
from utils import create_cases

def test_MSE():
    a, b = create_cases()
    assert MSE(a,b) == 0.00013567081521