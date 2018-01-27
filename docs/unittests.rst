.. _unittest:

Unit Tests
==========

Here are the `unit tests results <_static/results.html>`_ for this project.

This is using the default Python :ref:`unittest <references>` suite, but using
:ref:`nosetests <references>` to produce nice HTML output. A list of unit test
assert methods is `here
<https://docs.python.org/2/library/unittest.html#classes-and-functions>`_

To run the unit tests using :download:`testemployees <../test/testemployees.py>`::

   python-coverage run -a --include=main.py,employees.employees.py -m test.testemployees

Or::

    python -m unittest discover test/ -v

Or::

    nosetests --config=test/nosetests.cfg --verbose --where $PWD test/test*.py

The basic report of unit test results is::

   TestEmployees 0.3.0
   testDump (__main__.TestEmployees) ... ok
   testLoadFromFile1 (__main__.TestEmployees) ... ok
   testLoadFromFile2 (__main__.TestEmployees) ... ok
   testNoId (__main__.TestEmployees) ... ok
   testNoName (__main__.TestEmployees) ... ok
   testNoYear (__main__.TestEmployees) ... ok
   testTurnoverById (__main__.TestEmployees) ... ok
   testTurnoverByName (__main__.TestEmployees) ... ok
   testTurnoverByYear (__main__.TestEmployees) ... ok
   testTurnoverTotalByYear (__main__.TestEmployees) ... ok
   testZeroTurnover (__main__.TestEmployees) ... ok

   ----------------------------------------------------------------------
   Ran 11 tests in 0.006s

   OK

See also :ref:`coverage`.

.. EOF
