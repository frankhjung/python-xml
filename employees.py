#!/usr/bin/python
# coding=utf-8

"""
Read Employee data to return turnover information.
This is a example Python program to read and process XML files.
"""


class Employees:

    """ Read Employee data to return turnover information. """

    def __init__(self, infile=None):
        self.employees = None
        if infile is not None:
            self.loadFromFile(infile)

    def loadFromFile(self, infile):
        from xml.etree import ElementTree
        if isinstance(infile, file):
            self.employees = ElementTree.parse(infile.name)
        else:
            self.employees = ElementTree.parse(infile)

    def dump(self):
        import sys
        import StringIO
        from xml.etree import ElementTree
        stdold, stdnew = sys.stdout, StringIO.StringIO()
        sys.stdout = stdnew
        ElementTree.dump(self.employees)
        sys.stdout = stdold
        return stdnew.getvalue()

    def getById(self, id):
        """ Returns turnover for all years for an employee. """
        total = 0
        years = self.employees.findall(
            ".//employee[@id='%s']/turnover/year" % (id))
        if len(years) > 0:
            for y in years:
                total += int(y.text)
        else:
            total = None
        return total

    def getByName(self, name):
        """ Returns turnover for all years for an employee. """
        total = 0
        years = self.employees.findall(
            ".//employee[@name='%s']/turnover/year" % (name))
        if len(years) > 0:
            for y in years:
                total += int(y.text)
        else:
            total = None
        return total

    def getByYear(self, name, year):
        """ Returns turnover for an employees by year. """
        total = 0
        years = self.employees.findall(
            ".//employee[@name='%s']/turnover/year[@id='%s']" % (name, year))
        if len(years) > 0:
            for y in years:
                total += int(y.text)
        else:
            total = None
        return total

    def getAllByYear(self, year):
        """ Returns turnover for all employees by year. """
        total = 0
        years = self.employees.findall(".//turnover/year[@id='%s']" % (year))
        for y in years:
            total += int(y.text)
        return total

#EOF
