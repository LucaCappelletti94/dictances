"""Import all the functions offered by package dictances."""
from .bhattacharyya import bhattacharyya, bhattacharyya_coefficient
from .canberra import canberra
from .chebyshev import chebyshev
from .cosine import cosine
from .euclidean import euclidean
from .hamming import hamming
from .hellinger import hellinger
from .intersection_squared_hellinger import intersection_squared_hellinger
from .intersection_squared_variation import intersection_squared_variation
from .intersection_total_variation import intersection_total_variation
from .jensen_shannon import jensen_shannon
from .kullback_leibler import kullback_leibler
from .mae import mae
from .minkowsky import minkowsky
from .mse import mse
from .normal_total_variation import normal_total_variation
from .nth_variation import nth_variation
from .pearson import pearson
from .squared_hellinger import squared_hellinger
from .squared_variation import squared_variation
from .total_variation import total_variation

manhattan = cityblock = total_variation

__all__ = ['bhattacharyya', 'bhattacharyya_coefficient', 'canberra',
           'chebyshev', 'cosine', 'euclidean',
           'hamming', 'hellinger', 'jensen_shannon', 'kullback_leibler',
           'mae', 'manhattan', 'cityblock', 'minkowsky', 'mse', 'normal_total_variation',
           'nth_variation', 'pearson', 'squared_variation', 'total_variation',
           'squared_hellinger', 'intersection_squared_variation',
           'intersection_squared_hellinger']
