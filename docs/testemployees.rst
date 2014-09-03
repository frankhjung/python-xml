.. _testemployees:

TestEmployees
=============

.. automodule:: test.testemployees
   :members:

Tests are run using `nosetests
<http://nose.readthedocs.org/en/latest/usage.html>`_. The test configuration is
in the file :download:`nosetests.cfg <../test/nosetests.cfg>`.

Help on module :download:`test.testemployees.py <../test/testemployees.py>`::

   NAME
      test.testemployees - Run unit tests for YAML file processing example, Employees.

   FILE
      test/testemployees.py

   CLASSES
      unittest.case.TestCase(__builtin__.object)
         TestEmployees
      
      class TestEmployees(unittest.case.TestCase)
      |  Tests for Employees.
      |  
      |  Method resolution order:
      |      TestEmployees
      |      unittest.case.TestCase
      |      __builtin__.object
      |  
      |  Methods defined here:
      |  
      |  setUp(self)
      |  
      |  tearDown(self)
      |  
      |  testDump(self)
      |  
      |  testLoadFromFile1(self)
      |  
      |  testLoadFromFile2(self)
      |  
      |  testNoId(self)
      |  
      |  testNoName(self)
      |  
      |  testNoYear(self)
      |  
      |  testTurnoverById(self)
      |  
      |  testTurnoverByName(self)
      |  
      |  testTurnoverByYear(self)
      |  
      |  testTurnoverTotalByYear(self)
      |  
      |  testZeroTurnover(self)
      |  
      |  ----------------------------------------------------------------------
      |  Class methods defined here:
      |  
      |  setUpClass(cls) from __builtin__.type
      |  
      |  ----------------------------------------------------------------------
      |  Data and other attributes defined here:
      |  
      |  TEST_FILE = 'data/test.xml'
      |  
      |  __version__ = '0.1.0'
      |  
      |  ----------------------------------------------------------------------
      |  Methods inherited from unittest.case.TestCase:
      |  
      |  __call__(self, *args, **kwds)
      |  
      |  __eq__(self, other)
      |  
      |  __hash__(self)
      |  
      |  __init__(self, methodName='runTest')
      |      Create an instance of the class that will use the named test
      |      method when executed. Raises a ValueError if the instance does
      |      not have a method with the specified name.
      |  
      |  __ne__(self, other)
      |  
      |  __repr__(self)
      |  
      |  __str__(self)
      |  
      |  addCleanup(self, function, *args, **kwargs)
      |      Add a function, with arguments, to be called when the test is
      |      completed. Functions added are called on a LIFO basis and are
      |      called after tearDown on test failure or success.
      |      
      |      Cleanup items are called even if setUp fails (unlike tearDown).
      |  
      |  addTypeEqualityFunc(self, typeobj, function)
      |      Add a type specific assertEqual style function to compare a type.
      |      
      |      This method is for use by TestCase subclasses that need to register
      |      their own type equality functions to provide nicer error messages.
      |      
      |      Args:
      |          typeobj: The data type to call this function on when both values
      |                  are of the same type in assertEqual().
      |          function: The callable taking two arguments and an optional
      |                  msg= argument that raises self.failureException with a
      |                  useful error message when the two arguments are not equal.
      |  
      |  assertAlmostEqual(self, first, second, places=None, msg=None, delta=None)
      |      Fail if the two objects are unequal as determined by their
      |      difference rounded to the given number of decimal places
      |      (default 7) and comparing to zero, or by comparing that the
      |      between the two objects is more than the given delta.
      |      
      |      Note that decimal places (from zero) are usually not the same
      |      as significant digits (measured from the most signficant digit).
      |      
      |      If the two objects compare equal then they will automatically
      |      compare almost equal.
      |  
      |  assertAlmostEquals = assertAlmostEqual(self, first, second, places=None, msg=None, delta=None)
      |      Fail if the two objects are unequal as determined by their
      |      difference rounded to the given number of decimal places
      |      (default 7) and comparing to zero, or by comparing that the
      |      between the two objects is more than the given delta.
      |      
      |      Note that decimal places (from zero) are usually not the same
      |      as significant digits (measured from the most signficant digit).
      |      
      |      If the two objects compare equal then they will automatically
      |      compare almost equal.
      |  
      |  assertDictContainsSubset(self, expected, actual, msg=None)
      |      Checks whether actual is a superset of expected.
      |  
      |  assertDictEqual(self, d1, d2, msg=None)
      |  
      |  assertEqual(self, first, second, msg=None)
      |      Fail if the two objects are unequal as determined by the '=='
      |      operator.
      |  
      |  assertEquals = assertEqual(self, first, second, msg=None)
      |      Fail if the two objects are unequal as determined by the '=='
      |      operator.
      |  
      |  assertFalse(self, expr, msg=None)
      |      Check that the expression is false.
      |  
      |  assertGreater(self, a, b, msg=None)
      |      Just like self.assertTrue(a > b), but with a nicer default message.
      |  
      |  assertGreaterEqual(self, a, b, msg=None)
      |      Just like self.assertTrue(a >= b), but with a nicer default message.
      |  
      |  assertIn(self, member, container, msg=None)
      |      Just like self.assertTrue(a in b), but with a nicer default message.
      |  
      |  assertIs(self, expr1, expr2, msg=None)
      |      Just like self.assertTrue(a is b), but with a nicer default message.
      |  
      |  assertIsInstance(self, obj, cls, msg=None)
      |      Same as self.assertTrue(isinstance(obj, cls)), with a nicer
      |      default message.
      |  
      |  assertIsNone(self, obj, msg=None)
      |      Same as self.assertTrue(obj is None), with a nicer default message.
      |  
      |  assertIsNot(self, expr1, expr2, msg=None)
      |      Just like self.assertTrue(a is not b), but with a nicer default message.
      |  
      |  assertIsNotNone(self, obj, msg=None)
      |      Included for symmetry with assertIsNone.
      |  
      |  assertItemsEqual(self, expected_seq, actual_seq, msg=None)
      |      An unordered sequence specific comparison. It asserts that
      |      actual_seq and expected_seq have the same element counts.
      |      Equivalent to::
      |      
      |          self.assertEqual(Counter(iter(actual_seq)),
      |                           Counter(iter(expected_seq)))
      |      
      |      Asserts that each element has the same count in both sequences.
      |      Example:
      |          - [0, 1, 1] and [1, 0, 1] compare equal.
      |          - [0, 0, 1] and [0, 1] compare unequal.
      |  
      |  assertLess(self, a, b, msg=None)
      |      Just like self.assertTrue(a < b), but with a nicer default message.
      |  
      |  assertLessEqual(self, a, b, msg=None)
      |      Just like self.assertTrue(a <= b), but with a nicer default message.
      |  
      |  assertListEqual(self, list1, list2, msg=None)
      |      A list-specific equality assertion.
      |      
      |      Args:
      |          list1: The first list to compare.
      |          list2: The second list to compare.
      |          msg: Optional message to use on failure instead of a list of
      |                  differences.
      |  
      |  assertMultiLineEqual(self, first, second, msg=None)
      |      Assert that two multi-line strings are equal.
      |  
      |  assertNotAlmostEqual(self, first, second, places=None, msg=None, delta=None)
      |      Fail if the two objects are equal as determined by their
      |      difference rounded to the given number of decimal places
      |      (default 7) and comparing to zero, or by comparing that the
      |      between the two objects is less than the given delta.
      |      
      |      Note that decimal places (from zero) are usually not the same
      |      as significant digits (measured from the most signficant digit).
      |      
      |      Objects that are equal automatically fail.
      |  
      |  assertNotAlmostEquals = assertNotAlmostEqual(self, first, second, places=None, msg=None, delta=None)
      |      Fail if the two objects are equal as determined by their
      |      difference rounded to the given number of decimal places
      |      (default 7) and comparing to zero, or by comparing that the
      |      between the two objects is less than the given delta.
      |      
      |      Note that decimal places (from zero) are usually not the same
      |      as significant digits (measured from the most signficant digit).
      |      
      |      Objects that are equal automatically fail.
      |  
      |  assertNotEqual(self, first, second, msg=None)
      |      Fail if the two objects are equal as determined by the '!='
      |      operator.
      |  
      |  assertNotEquals = assertNotEqual(self, first, second, msg=None)
      |      Fail if the two objects are equal as determined by the '!='
      |      operator.
      |  
      |  assertNotIn(self, member, container, msg=None)
      |      Just like self.assertTrue(a not in b), but with a nicer default message.
      |  
      |  assertNotIsInstance(self, obj, cls, msg=None)
      |      Included for symmetry with assertIsInstance.
      |  
      |  assertNotRegexpMatches(self, text, unexpected_regexp, msg=None)
      |      Fail the test if the text matches the regular expression.
      |  
      |  assertRaises(self, excClass, callableObj=None, *args, **kwargs)
      |      Fail unless an exception of class excClass is raised
      |      by callableObj when invoked with arguments args and keyword
      |      arguments kwargs. If a different type of exception is
      |      raised, it will not be caught, and the test case will be
      |      deemed to have suffered an error, exactly as for an
      |      unexpected exception.
      |      
      |      If called with callableObj omitted or None, will return a
      |      context object used like this::
      |      
      |           with self.assertRaises(SomeException):
      |               do_something()
      |      
      |      The context manager keeps a reference to the exception as
      |      the 'exception' attribute. This allows you to inspect the
      |      exception after the assertion::
      |      
      |          with self.assertRaises(SomeException) as cm:
      |              do_something()
      |          the_exception = cm.exception
      |          self.assertEqual(the_exception.error_code, 3)
      |  
      |  assertRaisesRegexp(self, expected_exception, expected_regexp, callable_obj=None, *args, **kwargs)
      |      Asserts that the message in a raised exception matches a regexp.
      |      
      |      Args:
      |          expected_exception: Exception class expected to be raised.
      |          expected_regexp: Regexp (re pattern object or string) expected
      |                  to be found in error message.
      |          callable_obj: Function to be called.
      |          args: Extra args.
      |          kwargs: Extra kwargs.
      |  
      |  assertRegexpMatches(self, text, expected_regexp, msg=None)
      |      Fail the test unless the text matches the regular expression.
      |  
      |  assertSequenceEqual(self, seq1, seq2, msg=None, seq_type=None)
      |      An equality assertion for ordered sequences (like lists and tuples).
      |      
      |      For the purposes of this function, a valid ordered sequence type is one
      |      which can be indexed, has a length, and has an equality operator.
      |      
      |      Args:
      |          seq1: The first sequence to compare.
      |          seq2: The second sequence to compare.
      |          seq_type: The expected datatype of the sequences, or None if no
      |                  datatype should be enforced.
      |          msg: Optional message to use on failure instead of a list of
      |                  differences.
      |  
      |  assertSetEqual(self, set1, set2, msg=None)
      |      A set-specific equality assertion.
      |      
      |      Args:
      |          set1: The first set to compare.
      |          set2: The second set to compare.
      |          msg: Optional message to use on failure instead of a list of
      |                  differences.
      |      
      |      assertSetEqual uses ducktyping to support different types of sets, and
      |      is optimized for sets specifically (parameters must support a
      |      difference method).
      |  
      |  assertTrue(self, expr, msg=None)
      |      Check that the expression is true.
      |  
      |  assertTupleEqual(self, tuple1, tuple2, msg=None)
      |      A tuple-specific equality assertion.
      |      
      |      Args:
      |          tuple1: The first tuple to compare.
      |          tuple2: The second tuple to compare.
      |          msg: Optional message to use on failure instead of a list of
      |                  differences.
      |  
      |  assert_ = assertTrue(self, expr, msg=None)
      |      Check that the expression is true.
      |  
      |  countTestCases(self)
      |  
      |  debug(self)
      |      Run the test without collecting errors in a TestResult
      |  
      |  defaultTestResult(self)
      |  
      |  doCleanups(self)
      |      Execute all cleanup functions. Normally called for you after
      |      tearDown.
      |  
      |  fail(self, msg=None)
      |      Fail immediately, with the given message.
      |  
      |  failIf = deprecated_func(*args, **kwargs)
      |  
      |  failIfAlmostEqual = deprecated_func(*args, **kwargs)
      |  
      |  failIfEqual = deprecated_func(*args, **kwargs)
      |  
      |  failUnless = deprecated_func(*args, **kwargs)
      |  
      |  failUnlessAlmostEqual = deprecated_func(*args, **kwargs)
      |  
      |  failUnlessEqual = deprecated_func(*args, **kwargs)
      |  
      |  failUnlessRaises = deprecated_func(*args, **kwargs)
      |  
      |  id(self)
      |  
      |  run(self, result=None)
      |  
      |  shortDescription(self)
      |      Returns a one-line description of the test, or None if no
      |      description has been provided.
      |      
      |      The default implementation of this method returns the first line of
      |      the specified test method's docstring.
      |  
      |  skipTest(self, reason)
      |      Skip this test.
      |  
      |  ----------------------------------------------------------------------
      |  Class methods inherited from unittest.case.TestCase:
      |  
      |  tearDownClass(cls) from __builtin__.type
      |      Hook method for deconstructing the class fixture after running all tests in the class.
      |  
      |  ----------------------------------------------------------------------
      |  Data descriptors inherited from unittest.case.TestCase:
      |  
      |  __dict__
      |      dictionary for instance variables (if defined)
      |  
      |  __weakref__
      |      list of weak references to the object (if defined)
      |  
      |  ----------------------------------------------------------------------
      |  Data and other attributes inherited from unittest.case.TestCase:
      |  
      |  failureException = <type 'exceptions.AssertionError'>
      |      Assertion failed.
      |  
      |  longMessage = False
      |  
      |  maxDiff = 640


.. EOF
