from dictances import canberra
from utils import create_cases

def test_canberra():
    a, b = create_cases()
    assert canberra(a,b) == 170.27780598478526