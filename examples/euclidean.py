from example_utils import generate_example_dict
from distances import euclidean

a, b = generate_example_dict(), generate_example_dict()

print(euclidean(a,b))
# >>> 15119.400349404095