from distances import bhattacharyya
from utils import create_cases

def test_bhattacharyya():
    a, b = create_cases()
    assert bhattacharyya(a,b) == 0.563571437813277