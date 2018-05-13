import random
random.seed(42) # for reproducibility

# Simple function to generate the example dictionaries
def generate_example_dict(n=1000):
    return {random.randint(0,1000):random.uniform(0,1000) for i in range(n)}

def generate_normalized_example_dict(n=1000):
    d = {random.randint(0,1000):random.uniform(0,1) for i in range(n)}
    return {k: v / sum(d.values()) for k, v in d.items()}