from dictances import mse

from utils import close, create_cases


def test_mse():
    a, b = create_cases()
    assert close(mse(a, b), 0.00013567081521)
