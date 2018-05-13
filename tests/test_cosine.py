from distances import cosine
from utils import create_cases

def test_cosine():
    a, b = create_cases()
    assert cosine(a,b) == 0.11290663021977