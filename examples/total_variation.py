from example_utils import generate_example_dict
from distances import total_variation

a, b = generate_example_dict(), generate_example_dict()

print(total_variation(a,b))
# >>> 376204.668226937