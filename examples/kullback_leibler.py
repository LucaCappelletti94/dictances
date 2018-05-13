from example_utils import generate_normalized_example_dict
from distances import kullback_leibler

a, b = generate_normalized_example_dict(), generate_normalized_example_dict()

print(kullback_leibler(a,b))
# >>> 0.0
print(kullback_leibler(b,a))
# >>> 0.33440999671251