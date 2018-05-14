from example_utils import generate_example_dicts
from dictances import hamming

a, b = generate_example_dicts()

print(hamming(a,b))
# >>> 467