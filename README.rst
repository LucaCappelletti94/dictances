.. role:: py(code)
   :language: python

Distances
==========

|travis| |coveralls| |sonar_quality| |sonar_bugs| |sonar_lines| |sonar_maintainability|

Distances and divergences between discrete distributions implemented in python.

In the complexity notations, :py:`n` is :py:`len(a)` and :py:`m` is :py:`len(b)`. These are all tested on the same computer, on the same dictionaries.

+------------------------------+-------------------------------+-----------------------------+--------------------------------------+
| Metric name                  | Function name                 | Average time on same sample | Complexity                           |
+==============================+===============================+=============================+======================================+
| `Euclidean distance`_        | `euclidean`_                  | 49.2 µs ± 664 ns            | |On+m|                               |
+------------------------------+-------------------------------+-----------------------------+--------------------------------------+
| `Total variation`_           | `total_variation`_            | 46 µs ± 513 ns.             | |On+m|                               |
+------------------------------+-------------------------------+-----------------------------+--------------------------------------+
| `Jensen Shannon divergence`_ | `jensen_shannon`_             | 21.1 µs ± 442 ns            | |Omin|                               |
+------------------------------+-------------------------------+-----------------------------+--------------------------------------+
| `Bhattacharyya distance`_    | `bhattacharyya`_              | 14.4 µs ± 180 ns            | |Omin|                               |
+------------------------------+-------------------------------+-----------------------------+--------------------------------------+
| `Hellinger distance`_        | `hellinger`_                  | 16.8 µs ± 372 ns            | |Omin|                               |
+------------------------------+-------------------------------+-----------------------------+--------------------------------------+

.. |travis| image:: https://travis-ci.org/LucaCappelletti94/distances.png
   :target: https://travis-ci.org/LucaCappelletti94/distances

.. |coveralls| image:: https://coveralls.io/repos/github/LucaCappelletti94/distances/badge.svg?branch=master
    :target: https://coveralls.io/github/LucaCappelletti94/distances

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
.. _Bhattacharyya distance: https://en.wikipedia.org/wiki/Bhattacharyya_distance
.. _Total variation: https://en.wikipedia.org/wiki/Total_variation
.. _Hellinger distance: https://en.wikipedia.org/wiki/Hellinger_distance

.. _euclidean: https://github.com/LucaCappelletti94/distances/blob/master/examples/euclidean.py
.. _jensen_shannon: https://github.com/LucaCappelletti94/distances/blob/master/examples/jensen_shannon.py
.. _bhattacharyya: https://github.com/LucaCappelletti94/distances/blob/master/examples/bhattacharyya.py
.. _total_variation: https://github.com/LucaCappelletti94/distances/blob/master/examples/total_variation.py
.. _hellinger: https://github.com/LucaCappelletti94/distances/blob/master/examples/hellinger.py

.. |On+m| image:: https://github.com/LucaCappelletti94/distances/blob/master/images/On+m.gif?raw=true
.. |Omin| image:: https://github.com/LucaCappelletti94/distances/blob/master/images/Omin.gif?raw=true