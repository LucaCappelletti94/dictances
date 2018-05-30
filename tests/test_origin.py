from dictances import (bhattacharyya, canberra, chebyshev, cosine, euclidean,
                       hamming, hellinger, jensen_shannon, kullback_leibler,
                       mae, manhattan, mse, pearson, squared_variation,
                       total_variation)

from utils import close, create_case

distances = {
    "squared_variation": squared_variation,
    "euclidean": euclidean,
    "jensen_shannon": jensen_shannon,
    "bhattacharyya": bhattacharyya,
    "total_variation": total_variation,
    "hellinger": hellinger,
    "kullback_leibler": kullback_leibler,
    "canberra": canberra,
    "chebyshev": chebyshev,
    "cosine": cosine,
    "hamming": hamming,
    "mae": mae,
    "manhattan": manhattan,
    "mse": mse,
    "pearson": pearson
}


def test_origin():
    global distances
    errors = []
    a = create_case()
    for distance_name, distance in distances.items():
        if not close(distance(a, a), 0):
            errors.append("Metric '%s' is not null on same point: %s" % (
                          distance_name, distance(a, a)))

    assert not errors, "errors occured:\n{}".format("\n".join(errors))
