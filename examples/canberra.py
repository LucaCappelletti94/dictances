from example_utils import generate_example_dicts
from distances import canberra

a, b = generate_example_dicts()

print(canberra(a,b))
# >>> 624.9088876554047