from dictances import pearson
from utils import create_cases


def test_pearson():
    a, b = create_cases()
    assert pearson(a, b) == 0.89895209792992
