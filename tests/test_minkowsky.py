from dictances import minkowsky
from utils import create_cases

def test_minkowsky():
    a, b = create_cases()

    try:
        minkowsky(a,b,0)
        assert False
    except ValueError:
        assert True

    assert (
        minkowsky(a,b,1),
        minkowsky(a,b,2),
        minkowsky(a,b,3),
        minkowsky(a,b,4)
    ) == (
        1.80865306195869,
        0.15540078863291,
        0.07115355218523,
        0.04889067980003
    )