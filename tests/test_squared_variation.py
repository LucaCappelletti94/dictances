from distances import squared_variation
from utils import create_cases

def test_squared_variation():
    a, b = create_cases()
    assert squared_variation(a,b) == 1.80865306195869