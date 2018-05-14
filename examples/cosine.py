from example_utils import generate_example_dicts
from distances import cosine

a, b = generate_example_dicts()

print(cosine(a,b))
# >>> 0.52336690346601