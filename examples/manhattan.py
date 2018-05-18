from example_utils import generate_example_dicts
from dictances import manhattan

a, b = generate_example_dicts()

print(manhattan(a, b))
# >>> 376204.668226937
