from dictances import pearson

from utils import close, create_cases


def test_pearson():
    a, b = create_cases()
    assert close(pearson(a, b), 0.89895209792992)
