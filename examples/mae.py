from example_utils import generate_example_dicts
from dictances import mae

a, b = generate_example_dicts()

print(mae(a, b))
# >>> 429.45738382070437
