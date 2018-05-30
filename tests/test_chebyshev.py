from dictances import chebyshev

from utils import close, create_cases


def test_chebyshev():
    a, b = create_cases()
    assert close(chebyshev(a, b), 0.02015304120034)
