from example_utils import generate_normalized_example_dicts
from dictances import jensen_shannon

a, b = generate_normalized_example_dicts()

print(jensen_shannon(a,b))
# >>> 0.3145726162024