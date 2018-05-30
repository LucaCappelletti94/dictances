from dictances import total_variation

from utils import close, create_cases


def test_total_variation():
    a, b = create_cases()
    assert close(total_variation(a, b), 1.80865306195869)
