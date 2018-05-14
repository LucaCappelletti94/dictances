from example_utils import generate_example_dicts
from distances import squared_variation

a, b = generate_example_dicts()

print(squared_variation(a,b))
# >>> 228596266.92556065