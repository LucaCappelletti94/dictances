from example_utils import generate_example_dicts
from dictances import nth_variation

a, b = generate_example_dicts()

print(nth_variation(a, b, 0))
# >>> 876.0

print(nth_variation(a, b, 1))
# >>> 376204.668226937

print(nth_variation(a, b, 2))
# >>> 228596266.92556065

print(nth_variation(a, b, 3))
# >>> 161656620966.50134
