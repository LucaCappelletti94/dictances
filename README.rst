Dictances
=========================================================================================
|pip| |downloads|

Distances and divergences between discrete distributions described as dictionaries implemented in python.

These are meant as fast solutions to compute distances and divergences between discrete distributions,
expecially when the two distributions contains a significant amount of events with nill probability
which are not described in the dictionaries.

How do I install this package?
----------------------------------------------
As usual, just download it using pip:

.. code:: shell

    pip install dictances


Available metrics
-----------------------------------------------
A number of distances and divergences are available:

.. role:: python(code)
   :language: python

+----------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| Distances                                                                                                      | Methods                                         |
+================================================================================================================+=================================================+
| `Bhattacharyya distance <https://en.wikipedia.org/wiki/Bhattacharyya_distance>`__                              | :python:`bhattacharyya`                         |
+----------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| `Bhattacharyya coefficient <https://en.wikipedia.org/wiki/Bhattacharyya_distance#Bhattacharyya_coefficient>`__ | :python:`bhattacharyya_coefficient`             |
+----------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| `Canberra distance <https://en.wikipedia.org/wiki/Canberra_distance>`__                                        | :python:`canberra`                              |
+----------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| `Chebyshev distance <https://en.wikipedia.org/wiki/Chebyshev_distance>`__                                      | :python:`chebyshev`                             |
+----------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| `Chi Square distance <https://en.wikipedia.org/wiki/Chi-squared_test>`__                                       | :python:`chi_square`                            |
+----------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| `Cosine Distance <https://en.wikipedia.org/wiki/Cosine_similarity>`__                                          | :python:`cosine`                                |
+----------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| `Euclidean distance <https://en.wikipedia.org/wiki/Euclidean_distance>`__                                      | :python:`euclidean`                             |
+----------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| `Hamming distance <https://en.wikipedia.org/wiki/Hamming_distance>`__                                          | :python:`hamming`                               |
+----------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| `Jensen-Shannon divergence <https://en.wikipedia.org/wiki/Jensen%E2%80%93Shannon_divergence>`__                | :python:`jensen_shannon`                        |
+----------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| `Kullback-Leibler divergence <https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence>`__            | :python:`kullback_leibler`                      |
+----------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| `Mean absolute error <https://en.wikipedia.org/wiki/Mean_absolute_error>`__                                    | :python:`mae`                                   |
+----------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| `Taxicab geometry <https://en.wikipedia.org/wiki/Taxicab_geometry>`__                                          | :python:`manhattan, cityblock, total_variation` |
+----------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| `Minkowski distance <https://en.wikipedia.org/wiki/Minkowski_distance>`__                                      | :python:`minkowsky`                             |
+----------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| `Mean squared error <https://en.wikipedia.org/wiki/Mean_squared_error>`__                                      | :python:`mse`                                   |
+----------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| `Pearson's distance <https://en.wikipedia.org/wiki/Pearson_correlation_coefficient#Pearson's_distance>`__      | :python:`pearson`                               |
+----------------------------------------------------------------------------------------------------------------+-------------------------------------------------+
| `Squared deviations from the mean <https://en.wikipedia.org/wiki/Squared_deviations_from_the_mean>`__          | :python:`squared_variation`                     |
+----------------------------------------------------------------------------------------------------------------+-------------------------------------------------+

Usage example with points
--------------------------------------
Suppose you have a point described by `my_first_dictionary` and another one described by `my_second_dictionary`:

.. code:: python

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


Usage example with distributions
-----------------------------------------
Suppose you have a point described by `my_first_dictionary` and another one described by `my_second_dictionary`:

.. code:: python
    
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


Handling nested dictionaries
------------------------------------------
If you need to compute the distance between two nested dictionaries you can use `deflate_dict <https://github.com/LucaCappelletti94/deflate_dict>`_ as follows:

.. code:: python

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


.. |pip| image:: https://badge.fury.io/py/dictances.svg
    :target: https://badge.fury.io/py/dictances
    :alt: Pypi project

.. |downloads| image:: https://pepy.tech/badge/dictances
    :target: https://pepy.tech/badge/dictances
    :alt: Pypi total project downloads 
