from example_utils import generate_normalized_example_dicts
from dictances import bhattacharyya

a, b = generate_normalized_example_dicts()

print(bhattacharyya(a,b))
# >>> 0.56357143781328