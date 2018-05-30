from dictances import cosine

from utils import close, create_cases


def test_cosine():
    a, b = create_cases()
    assert close(cosine(a, b), 0.88709336978023)
