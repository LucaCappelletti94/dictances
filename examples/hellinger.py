from example_utils import generate_normalized_example_dicts
from dictances import hellinger

a, b = generate_normalized_example_dicts()

print(hellinger(a, b))
# >>> 0.26382145453188
