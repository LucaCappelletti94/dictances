from dictances import chebyshev
from utils import create_cases


def test_chebyshev():
    a, b = create_cases()
    assert chebyshev(a, b) == 0.02015304120034
