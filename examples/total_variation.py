from example_utils import generate_example_dicts
from dictances import total_variation

a, b = generate_example_dicts()

print(total_variation(a,b))
# >>> 376204.668226937