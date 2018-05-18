from example_utils import generate_example_dicts
from dictances import minkowsky

a, b = generate_example_dicts()

print(minkowsky(a, b, 1))
# >>> 376204.668226937

print(minkowsky(a, b, 2))
# >>> 15119.400349404095

print(minkowsky(a, b, 3))
# >>> 5447.507442156695
