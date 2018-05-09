import random
random.seed(42) # for reproducibility

def create_case(n=100):
    return {i:random.uniform(0,100) for i in range(n)}

def create_cases(n=100):
    return create_case(n), create_case(n)