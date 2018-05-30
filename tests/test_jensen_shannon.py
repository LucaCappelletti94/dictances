from dictances import jensen_shannon

from utils import close, create_cases


def test_jensen_shannon():
    a, b = create_cases()
    assert close(jensen_shannon(a, b), 0.6098897698032)
