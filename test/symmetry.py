from distances import euclidean
from .test_utils import test_cases

def test_answer():
    errors = []
    a,b = test_cases()
    for distance_name, distance in [("euclidean", euclidean)]:
       # replace assertions by conditions
        if distance(a,b) != distance(b,a):
            errors.append("Metric '%s' is not symmetric"%distance_name)

    # assert no error message has been registered, else print messages
    assert not errors, "errors occured:\n{}".format("\n".join(errors))