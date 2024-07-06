# Dictances

[![pip](https://badge.fury.io/py/dictances.svg)](https://pypi.org/project/dictances/)
[![downloads](https://pepy.tech/badge/dictances)](https://pepy.tech/project/dictances)
[![license](https://img.shields.io/github/license/LucaCappelletti94/dictances)](https://github.com/LucaCappelletti94/dictances/blob/master/LICENSE)
[![python versions](https://img.shields.io/pypi/pyversions/dictances)](https://www.python.org/downloads/)
[![GitHub actions](https://github.com/LucaCappelletti94/dictances/actions/workflows/python.yml/badge.svg)](https://github.com/LucaCappelletti94/dictances/actions/)


Distances and divergences between discrete distributions described as dictionaries implemented in Python.

These are meant as fast solutions to compute distances and divergences between discrete distributions, especially when the two distributions contain a significant amount of events with nil probability which are not described in the dictionaries.

## How do I install this package?

As usual, just download it using pip:

```shell
pip install dictances
```

## Available metrics

A number of distances and divergences are available:

| Distances                                                                                                      | Methods                                         |
|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| [Bhattacharyya distance](https://en.wikipedia.org/wiki/Bhattacharyya_distance)                                 | `bhattacharyya`                                 |
| [Bhattacharyya coefficient](https://en.wikipedia.org/wiki/Bhattacharyya_distance#Bhattacharyya_coefficient)    | `bhattacharyya_coefficient`                     |
| [Canberra distance](https://en.wikipedia.org/wiki/Canberra_distance)                                           | `canberra`                                      |
| [Chebyshev distance](https://en.wikipedia.org/wiki/Chebyshev_distance)                                         | `chebyshev`                                     |
| [Chi Square distance](https://en.wikipedia.org/wiki/Chi-squared_test)                                          | `chi_square`                                    |
| [Cosine Distance](https://en.wikipedia.org/wiki/Cosine_similarity)                                             | `cosine`                                        |
| [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance)                                         | `euclidean`                                     |
| [Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance)                                             | `hamming`                                       |
| [Jensen-Shannon divergence](https://en.wikipedia.org/wiki/Jensen%E2%80%93Shannon_divergence)                   | `jensen_shannon`                                |
| [Kullback-Leibler divergence](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence)               | `kullback_leibler`                              |
| [Mean absolute error](https://en.wikipedia.org/wiki/Mean_absolute_error)                                       | `mae`                                           |
| [Taxicab geometry](https://en.wikipedia.org/wiki/Taxicab_geometry)                                             | `manhattan`, `cityblock`, `total_variation`     |
| [Minkowski distance](https://en.wikipedia.org/wiki/Minkowski_distance)                                         | `minkowsky`                                     |
| [Mean squared error](https://en.wikipedia.org/wiki/Mean_squared_error)                                         | `mse`                                           |
| [Pearson's distance](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient#Pearson's_distance)         | `pearson`                                       |
| [Squared deviations from the mean](https://en.wikipedia.org/wiki/Squared_deviations_from_the_mean)             | `squared_variation`                             |

## Usage example with points

Suppose you have a point described by `my_first_dictionary` and another one described by `my_second_dictionary`:

```python
from dictances import cosine

my_first_dictionary = {
    "a": 56,
    "b": 34,
    "c": 89
}

my_second_dictionary = {
    "a": 21,
    "d": 51,
    "e": 74
}

cosine(my_first_dictionary, my_second_dictionary)
#>>> 0.8847005261889619
```

## Usage example with distributions

Suppose you have a point described by `my_first_dictionary` and another one described by `my_second_dictionary`:

```python
from dictances import bhattacharyya, bhattacharyya_coefficient

a = {
    "event_1": 0.4,
    "event_2": 0.1,
    "event_3": 0.2,
    "event_4": 0.3,
}
b = {
    "event_1": 0.1,
    "event_2": 0.2,
    "event_5": 0.2,
    "event_9": 0.5,
}

bhattacharyya_coefficient(a, b)
#>>> 0.3414213562373095
bhattacharyya(a, b)
#>>> 1.07463791569453
```

## Handling nested dictionaries

If you need to compute the distance between two nested dictionaries you can use [`deflate_dict`](https://github.com/LucaCappelletti94/deflate_dict) as follows:

```python
from dictances import cosine
from deflate_dict import deflate

my_first_dictionary = {
    "a": 8,
    "b": {
        "c": 3,
        "d": 6
    }
}

my_second_dictionary = {
    "b": {
        "c": 8,
        "d": 1
    },
    "y": 3,
}

cosine(deflate(my_first_dictionary), deflate(my_second_dictionary))
```