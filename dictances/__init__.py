"""Import all the functions offered by package dictances."""
from support_developer import support_luca
from .bhattacharyya import bhattacharyya, bhattacharyya_coefficient
from .canberra import canberra
from .chebyshev import chebyshev
from .chi_square import chi_square
from .cosine import cosine
from .euclidean import euclidean
from .hamming import hamming
from .intersection_squared_hellinger import intersection_squared_hellinger
from .intersection_squared_variation import intersection_squared_variation
from .intersection_total_variation import intersection_total_variation
from .intersection_nth_variation import intersection_nth_variation
from .jensen_shannon import jensen_shannon
from .kullback_leibler import kullback_leibler
from .mae import mae
from .minkowsky import minkowsky
from .mse import mse
from .normal_chi_square import normal_chi_square
from .nth_variation import nth_variation
from .pearson import pearson
from .squared_variation import squared_variation
from .total_variation import total_variation

manhattan = cityblock = total_variation

support_luca()

__all__ = ['bhattacharyya', 'bhattacharyya_coefficient', 'canberra',
           'chebyshev', 'chi_square', 'cosine', 'euclidean',
           'hamming', 'jensen_shannon', 'kullback_leibler',
           'mae', 'manhattan', 'cityblock', 'minkowsky', 'mse', 'normal_chi_square',
           'nth_variation', 'pearson', 'squared_variation', 'total_variation', 'intersection_squared_variation',
           'intersection_squared_hellinger', 'intersection_nth_variation']
