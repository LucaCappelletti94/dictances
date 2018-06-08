from dictances import hellinger

from utils import close, create_cases


def test_hellinger():
    a, b = create_cases()
    assert close(hellinger(a, b), 0.9361741043264331)
