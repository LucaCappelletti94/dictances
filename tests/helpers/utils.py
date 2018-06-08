import random
from math import isclose


def create_case(n=100, seed=42):
    random.seed(seed)  # for reproducibility
    d = {random.randint(0, 1000): random.uniform(0, 1) for i in range(n)}
    s = sum(d.values())
    return {k: v / s for k, v in d.items()}


def create_cases(n=100, seed_1=42, seed_2=69):
    return create_case(n, seed=seed_1), create_case(n, seed=seed_2)


def close(v1, v2):
    """Check if two values are close"""
    return isclose(v1, v2, abs_tol=1e-15)
