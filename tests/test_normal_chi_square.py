from dictances import normal_chi_square

from utils import close, create_cases


def test_normal_chi_square():
    a, b = create_cases()
    assert close(normal_chi_square(a, b), 1.7709856709663239)
