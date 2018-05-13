from distances import kullback_leibler
from utils import create_cases

def test_kullback_leibler():
    a, b = create_cases()
    assert (
        kullback_leibler(a,b),
        kullback_leibler(b,a)
    ) == (
        0.0,
        0.01247704999657
    )