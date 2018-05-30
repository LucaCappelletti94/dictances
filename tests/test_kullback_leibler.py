from dictances import kullback_leibler

from utils import close, create_cases


def test_kullback_leibler():
    a, b = create_cases()
    assert close(kullback_leibler(a, b), 0) and close(
        kullback_leibler(b, a), 0.01247704999657)
