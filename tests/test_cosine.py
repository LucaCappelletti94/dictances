from dictances import cosine
from utils import create_cases

def test_cosine():
    a, b = create_cases()
    assert cosine(a,b) == 0.88709336978023