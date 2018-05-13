from example_utils import generate_normalized_example_dict
from distances import bhattacharyya

a, b = generate_normalized_example_dict(), generate_normalized_example_dict()

print(bhattacharyya(a,b))
# >>> 0.563571437813277