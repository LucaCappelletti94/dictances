from dictances import chi_square

from utils import close, create_cases


def test_chi_square():
    a, b = create_cases()
    assert close(chi_square(a, b), 1.7709856709663239)
