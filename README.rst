dictances
=========================================================================================
|travis| |sonar_quality| |sonar_maintainability| |codacy| |code_climate_maintainability| |pip| |downloads|

Distances and divergences between distributions implemented in python.

How do I install this package?
----------------------------------------------
As usual, just download it using pip:

.. code:: shell

    pip install dictances

Tests Coverage
----------------------------------------------
Since some software handling coverages sometime get slightly different results, here's three of them:

|coveralls| |sonar_coverage| |code_climate_coverage|


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
| `Chi Square distance <https://en.wikipedia.org/wiki/Chi-squared_test>`__                                       | :python:`chi_square`                             |
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

Usage example
--------------------

.. code:: python

    from dictances import cosine

    cosine(my_first_dictionary, my_second_dictionary)


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



.. |travis| image:: https://travis-ci.org/LucaCappelletti94/dictances.png
   :target: https://travis-ci.org/LucaCappelletti94/dictances
   :alt: Travis CI build

.. |sonar_quality| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_dictances&metric=alert_status
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_dictances
    :alt: SonarCloud Quality

.. |sonar_maintainability| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_dictances&metric=sqale_rating
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_dictances
    :alt: SonarCloud Maintainability

.. |sonar_coverage| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_dictances&metric=coverage
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_dictances
    :alt: SonarCloud Coverage

.. |coveralls| image:: https://coveralls.io/repos/github/LucaCappelletti94/dictances/badge.svg?branch=master
    :target: https://coveralls.io/github/LucaCappelletti94/dictances?branch=master
    :alt: Coveralls Coverage

.. |pip| image:: https://badge.fury.io/py/dictances.svg
    :target: https://badge.fury.io/py/dictances
    :alt: Pypi project

.. |downloads| image:: https://pepy.tech/badge/dictances
    :target: https://pepy.tech/badge/dictances
    :alt: Pypi total project downloads 

.. |codacy|  image:: https://api.codacy.com/project/badge/Grade/eefefda798b64e50ab091f1deab6dadc
    :target: https://www.codacy.com/manual/LucaCappelletti94/dictances?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=LucaCappelletti94/dictances&amp;utm_campaign=Badge_Grade
    :alt: Codacy Maintainability

.. |code_climate_maintainability| image:: https://api.codeclimate.com/v1/badges/25fb7c6119e188dbd12c/maintainability
    :target: https://codeclimate.com/github/LucaCappelletti94/dictances/maintainability
    :alt: Maintainability

.. |code_climate_coverage| image:: https://api.codeclimate.com/v1/badges/25fb7c6119e188dbd12c/test_coverage
    :target: https://codeclimate.com/github/LucaCappelletti94/dictances/test_coverage
    :alt: Code Climate Coverate