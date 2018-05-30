from dictances import minkowsky

from utils import close, create_cases


def test_minkowsky():
    a, b = create_cases()

    try:
        minkowsky(a, b, 0)
        assert False
    except ValueError:
        assert True

    assert close(minkowsky(a, b, 1), 1.80865306195869) and close(minkowsky(a, b, 2), 0.15540078863291) and close(
        minkowsky(a, b, 3), 0.07115355218523) and close(minkowsky(a, b, 4), 0.04889067980003)
