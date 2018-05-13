Distances
==========

|travis| |coveralls| |sonar_quality| |sonar_bugs| |sonar_lines| |sonar_maintainability|

Distances and divergences between distributions implemented in python.

With |a| or |b| I mean the length of the dictionary a and b respectively.

+------------------------------+----------------+-----------------------------+-------------------+
| Metric name                  | Function name  | Average time on same sample | Complexity        |
+==============================+================+=============================+===================+
| `Euclidean distance`_        | euclidean(a,b) | 50.1 µs ± 2.26 µs           | O(|a||b|)         |
+------------------------------+----------------+-----------------------------+-------------------+
| `Jensen Shannon divergence`_ | jensen_shannon | 20.8 µs ± 1.36 µs           | O(min(|a|, |b|))  |
+------------------------------+----------------+-----------------------------+-------------------+

.. literalinclude:: examples/euclidean.py
   :language: python
   :emphasize-lines: 9-12
   :linenos:

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