from example_utils import generate_example_dicts
from distances import MAE

a, b = generate_example_dicts()

print(MAE(a,b))
# >>> 429.45738382070437