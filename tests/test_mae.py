from dictances import mae

from utils import close, create_cases


def test_mae():
    a, b = create_cases()
    assert close(mae(a, b), 0.01016097225819)
