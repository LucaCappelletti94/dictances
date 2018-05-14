from example_utils import generate_normalized_example_dicts
from distances import kullback_leibler

a, b = generate_normalized_example_dicts()

print(kullback_leibler(a,b))
# >>> 0.0

print(kullback_leibler(b,a))
# >>> 0.33440999671251