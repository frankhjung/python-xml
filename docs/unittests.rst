.. _unittest:

Unit Tests
==========

Here are the `unit tests results <_static/results.html>`_ for this project.

This is using the default Python :ref:`unittest <references>` suite, but using
:ref:`nosetests <references>` to produce nice HTML output. A list of unit test
assert methods is `here
<https://docs.python.org/2/library/unittest.html#classes-and-functions>`_

To run the unit tests using :download:`testemployees <../test/testemployees.py>`::

	python-coverage run -a --source=employees --include=main.py,employees.py -m test.testemployees

Or::

    python -m unittest discover test/ -v

Or::

    nosetests --config=test/nosetests.cfg --verbose --where $PWD test/test*.py
    

The basic report of unit test results is::

    TODO

See also :ref:`coverage`.

.. EOF
