import random
random.seed(42) # for reproducibility

def create_case(n=100):
    return {random.randint(0,1000):random.uniform(0,1) for i in range(n)}

def create_cases(n=100):
    return create_case(n), create_case(n)