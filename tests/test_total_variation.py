from dictances import total_variation
from utils import create_cases

def test_total_variation():
    a, b = create_cases()
    assert total_variation(a,b) == 1.80865306195869