from example_utils import generate_example_dicts
from distances import hamming

a, b = generate_example_dicts()

print(hamming(a,b))
# >>> 467