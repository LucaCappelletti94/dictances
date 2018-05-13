from example_utils import generate_example_dict
from distances import squared_variation

a, b = generate_example_dict(), generate_example_dict()

print(squared_variation(a,b))
# >>> 228596266.92556065