"""Import all the functions offered by package dictances."""
from .bhattacharyya import bhattacharyya
from .canberra import canberra
from .chebyshev import chebyshev
from .cosine import cosine
from .euclidean import euclidean
from .hamming import hamming
from .hellinger import hellinger
from .jensen_shannon import jensen_shannon
from .kullback_leibler import kullback_leibler
from .mae import mae
from .manhattan import manhattan
from .minkowsky import minkowsky
from .mse import mse
from .normal_total_variation import normal_total_variation
from .nth_variation import nth_variation
from .pearson import pearson
from .squared_variation import squared_variation
from .total_variation import total_variation

__all__ = ['bhattacharyya', 'canberra', 'chebyshev', 'cosine', 'euclidean',
           'hamming', 'hellinger', 'jensen_shannon', 'kullback_leibler',
           'mae', 'manhattan', 'minkowsky', 'mse', 'normal_total_variation',
           'nth_variation', 'pearson', 'squared_variation', 'total_variation']
