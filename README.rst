Distances
==========

|travis| |coveralls| |sonar_quality| |sonar_bugs| |sonar_lines| |sonar_maintainability|

Distances and divergences between distributions implemented in python.

In the complexity notations, `n` is `len(a)` and `m` is `len(b)`.

+------------------------------+-------------------------------+-----------------------------+-------------------+
| Metric name                  | Function name                 | Average time on same sample | Complexity        |
+==============================+===============================+=============================+===================+
| `Euclidean distance`_        | `euclidean`_                  | 50.1 µs ± 2.26 µs           | O(nm)             |
+------------------------------+-------------------------------+-----------------------------+-------------------+
| `Jensen Shannon divergence`_ | `jensen_shannon`_             | 20.8 µs ± 1.36 µs           | O(min(n,m))       |
+------------------------------+-------------------------------+-----------------------------+-------------------+

.. |travis| image:: https://travis-ci.org/LucaCappelletti94/distances.png
   :target: https://travis-ci.org/LucaCappelletti94/distances

.. |coveralls| image:: https://coveralls.io/repos/github/LucaCappelletti94/distances/badge.svg?branch=master

.. |sonar_quality| image:: https://sonarcloud.io/api/project_badges/measure?project=distances.lucacappelletti&metric=alert_status
    :target: https://sonarcloud.io/dashboard/index/distances.lucacappelletti

.. |sonar_bugs| image:: https://sonarcloud.io/api/project_badges/measure?project=distances.lucacappelletti&metric=bugs
    :target: https://sonarcloud.io/dashboard/index/distances.lucacappelletti

.. |sonar_lines| image:: https://sonarcloud.io/api/project_badges/measure?project=distances.lucacappelletti&metric=duplicated_lines_density
    :target: https://sonarcloud.io/dashboard/index/distances.lucacappelletti

.. |sonar_maintainability| image:: https://sonarcloud.io/api/project_badges/measure?project=distances.lucacappelletti&metric=sqale_rating
    :target: https://sonarcloud.io/dashboard/index/distances.lucacappelletti

.. _Euclidean distance: https://en.wikipedia.org/wiki/Euclidean_distance
.. _Jensen Shannon divergence: https://en.wikipedia.org/wiki/Jensen%E2%80%93Shannon_divergence
.. _euclidean: https://github.com/LucaCappelletti94/distances/blob/master/examples/euclidean.py
.. _jensen_shannon: https://github.com/LucaCappelletti94/distances/blob/master/examples/jensen_shannon.py