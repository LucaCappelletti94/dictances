from example_utils import generate_example_dicts
from distances import MSE

a, b = generate_example_dicts()

print(MSE(a,b))
# >>> 260954.64260908752