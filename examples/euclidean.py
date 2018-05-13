import random
from distances import euclidean
random.seed(42) # for reproducibility

# Simple function to generate the example dictionaries
def generate_example_dict(n=1000):
    return {random.randint(0,1000):random.uniform(0,1000) for i in range(n)}

a, b = generate_example_dict(), generate_example_dict()

euclidean(a,b)
# >>> 15119.400349404095