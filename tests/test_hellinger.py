from distances import hellinger
from utils import create_cases

def test_hellinger():
    a, b = create_cases()
    assert hellinger(a,b) == 0.09210690995562