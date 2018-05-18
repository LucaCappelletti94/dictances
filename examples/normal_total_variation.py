from example_utils import generate_normalized_example_dicts
from dictances import normal_total_variation

a, b = generate_normalized_example_dicts()

print(normal_total_variation(a, b))
# >>> 0.57772309258949
