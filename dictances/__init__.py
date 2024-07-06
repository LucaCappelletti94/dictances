"""Import all the functions offered by package dictances."""

from dictances.bhattacharyya import bhattacharyya, bhattacharyya_coefficient
from dictances.canberra import canberra
from dictances.chebyshev import chebyshev
from dictances.chi_square import chi_square
from dictances.cosine import cosine
from dictances.euclidean import euclidean
from dictances.hamming import hamming
from dictances.intersection_squared_hellinger import intersection_squared_hellinger
from dictances.intersection_squared_variation import intersection_squared_variation
from dictances.intersection_total_variation import intersection_total_variation
from dictances.intersection_nth_variation import intersection_nth_variation
from dictances.jensen_shannon import jensen_shannon
from dictances.kullback_leibler import kullback_leibler
from dictances.mae import mae
from dictances.minkowsky import minkowsky
from dictances.mse import mse
from dictances.normal_chi_square import normal_chi_square
from dictances.nth_variation import nth_variation
from dictances.pearson import pearson
from dictances.squared_variation import squared_variation
from dictances.total_variation import total_variation

manhattan = cityblock = total_variation

__all__ = [
    "bhattacharyya",
    "bhattacharyya_coefficient",
    "canberra",
    "chebyshev",
    "chi_square",
    "cosine",
    "euclidean",
    "hamming",
    "jensen_shannon",
    "kullback_leibler",
    "mae",
    "manhattan",
    "cityblock",
    "minkowsky",
    "mse",
    "normal_chi_square",
    "nth_variation",
    "pearson",
    "squared_variation",
    "total_variation",
    "intersection_squared_variation",
    "intersection_squared_hellinger",
    "intersection_nth_variation",
]
