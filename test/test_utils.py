import random
random.seed(42) # for reproducibility

def test_cases(n=100):
    a = {i:random.uniform(0,100) for i in range(n)}
    b = {i:random.uniform(0,100) for i in range(n)}
    return a,b