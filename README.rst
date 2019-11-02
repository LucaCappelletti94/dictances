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

- bhattacharyya
- bhattacharyya_coefficient
- canberra
- chebyshev
- cosine
- euclidean
- hamming
- jensen_shannon
- kullback_leibler
- mae
- manhattan, cityblock, total_variation
- minkowsky
- mse
- normal_total_variation
- nth_variation
- pearson
- squared_variation
- intersection_squared_variation
- intersection_squared_hellinger
- intersection_nth_variation

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