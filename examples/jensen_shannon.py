from example_utils import generate_normalized_example_dict
from distances import jensen_shannon

a, b = generate_normalized_example_dict(), generate_normalized_example_dict()

print(jensen_shannon(a,b))
# >>> 0.3145726162024