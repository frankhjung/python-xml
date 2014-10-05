#!/usr/bin/env python
# coding: utf-8

"""
Run unit tests for YAML file processing example, Employees.
"""

from employees.employees import Employees
import os
import unittest


class TestEmployees(unittest.TestCase):

    """ Tests for Employees. """

    __version__ = Employees.__version__

    TEST_FILE = 'data/test.xml'

    @classmethod
    def setUpClass(cls):
        print cls.__name__, cls.__version__

    def setUp(self):
        testFile = os.path.join(os.getcwd(), self.TEST_FILE)
        self.assertTrue(os.access(testFile, os.R_OK))

    def testLoadFromFile1(self):
        employees = Employees()
        employees.loadFromFile(self.TEST_FILE)
        self.assertIsNotNone(employees, 'expected employees')

    def testLoadFromFile2(self):
        employees = Employees()
        employees.loadFromFile(file(self.TEST_FILE))
        self.assertIsNotNone(employees, 'expected employees')

    def testDump(self):
        employees = Employees(self.TEST_FILE)
        dump = employees.dump()
        count = len(dump.split('\n'))
        self.assertEqual(
            count, 17,
            "expected %i lines dump, got %i" % (17, count))

    def testTurnoverByName(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees, 'expected employees')
        turnover = employees.getByName('frank')
        self.assertEqual(turnover, 100000 + 140000 + 200000)

    def testNoName(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees, 'expected employees')
        self.assertIsNone(employees.getByName('badname'))

    def testTurnoverById(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees, 'expected employees')
        turnover = employees.getById('004')
        self.assertEqual(turnover, 130000 + 220000 + 210000)

    def testNoId(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees, 'expected employees')
        self.assertIsNone(employees.getById(001))

    def testTurnoverByYear(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees, 'expected employees')
        turnover = employees.getByYear('frank', 2012)
        self.assertEqual(turnover, 140000)

    def testNoYear(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees, 'expected employees')
        turnover = employees.getByYear('frank', 2001)
        self.assertIsNone(turnover)

    def testTurnoverTotalByYear(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees, 'expected employees')
        turnover = employees.getTotalByYear(2012)
        self.assertEqual(turnover, 270000)

    def testZeroTurnover(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees, 'expected employees')
        self.assertEqual(
            employees.getTotalByYear(2001), None,
            "expected no turnover for this year")

    def tearDown(self):
        pass


#
# MAIN
#
if __name__ == '__main__':
    # to get verbose output use '-v' option
    unittest.main()
    # the following gives verbose output by default
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestEmployees)
    # unittest.TextTestRunner(verbosity=2).run(suite)

#EOF
