import random

def create_case(n=100, seed = 42):
    random.seed(seed) # for reproducibility
    return {random.randint(0,1000):random.uniform(0,1) for i in range(n)}

def create_cases(n=100, seed_1 = 42, seed_2 = 69):
    return create_case(n, seed=seed_1), create_case(n, seed = seed_2)