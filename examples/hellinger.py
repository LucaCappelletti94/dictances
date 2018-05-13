from example_utils import generate_normalized_example_dict
from distances import hellinger

a, b = generate_normalized_example_dict(), generate_normalized_example_dict()

print(hellinger(a,b))
# >>> 0.26382145453188