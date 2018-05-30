from dictances import manhattan

from utils import close, create_cases


def test_manhattan():
    a, b = create_cases()
    assert close(manhattan(a, b), 1.80865306195869)
