from distances import euclidean, jensen_shannon, bhattacharyya, total_variation, hellinger, kullback_leibler, squared_variation, canberra, chebyshev, cosine, hamming, mae, manhattan, minkowsky, mse, pearson
from utils import create_case

def test_origin():
    errors = []
    a = create_case()
    for distance_name, distance in [("squared_variation", squared_variation),("euclidean", euclidean), ("jensen_shannon", jensen_shannon), ("bhattacharyya", bhattacharyya), ("total_variation", total_variation), ("hellinger", hellinger), ("kullback_leibler", kullback_leibler), ("canberra", canberra), ("chebyshev", chebyshev), ("cosine", cosine), ("hamming", hamming), ("mae", mae), ("manhattan", manhattan), ("mse", mse), ("pearson", pearson)]:
       # replace assertions by conditions
        if distance(a,a) != 0:
            errors.append("Metric '%s' is not null on same point"%distance_name)

    # assert no error message has been registered, else print messages
    assert not errors, "errors occured:\n{}".format("\n".join(errors))