import random
random.seed(42) # for reproducibility

def test_case(n=100):
    return {i:random.uniform(0,100) for i in range(n)}

def test_cases(n=100):
    return test_case(n), test_case(n)