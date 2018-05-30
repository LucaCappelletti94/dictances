from dictances import squared_variation

from utils import close, create_cases


def test_squared_variation():
    a, b = create_cases()
    assert close(squared_variation(a, b), 0.02414940510773)
