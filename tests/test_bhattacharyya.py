from distances import bhattacharyya
from utils import create_cases

def test_bhattacharyya():
    a, b = create_cases()
    assert bhattacharyya(a,b) == 2.09088236794973