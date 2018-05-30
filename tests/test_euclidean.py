from dictances import euclidean

from utils import close, create_cases


def test_euclidean():
    a, b = create_cases()
    assert close(euclidean(a, b), 0.15540078863291)
