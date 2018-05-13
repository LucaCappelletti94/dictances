from distances import euclidean, jensen_shannon, bhattacharyya, total_variation, hellinger, squared_variation, canberra, chebyshev, cosine, hamming, MAE, manhattan, MSE, pearson
from utils import create_cases

def test_symmetry():
    errors = []
    a,b = create_cases()
    for distance_name, distance in [("squared_variation", squared_variation), ("euclidean", euclidean), ("jensen_shannon", jensen_shannon), ("bhattacharyya", bhattacharyya), ("total_variation", total_variation), ("hellinger", hellinger), ("canberra", canberra), ("chebyshev", chebyshev), ("cosine", cosine), ("hamming", hamming), ("MAE", MAE), ("manhattan", manhattan), ("MSE", MSE), ("pearson", pearson)]:
       # replace assertions by conditions
        if distance(a,b) != distance(b,a):
            errors.append("Metric '%s' is not symmetric"%distance_name)

    # assert no error message has been registered, else print messages
    assert not errors, "errors occured:\n{}".format("\n".join(errors))