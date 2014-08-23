#!/usr/bin/python
# coding=utf-8

"""
Simple example to demonstrate Python's ability to read from an XML file.
"""


import argparse
from employees import Employees
import os.path
import sys


def main(argv=sys.argv):

    """ Test employees class. """

    parser = argparse.ArgumentParser(
        prog=os.path.basename(argv[0]),
        usage='%(prog)s [options]',
        description='a Python example program to show XML processing',
        epilog='© 2013 Frank H Jung')
    parser.add_argument(
        'infile',
        nargs='?',
        type=argparse.FileType('r'),
        default='test.xml',
        help='alternate XML file to test')
    parser.add_argument(
        '-v',
        '--verbose',
        help='verbose output',
        action='count')
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 0.0.1')

    # process command line arguments
    args = parser.parse_args()

    # load employees from XML
    employees = Employees(args.infile)

    # show command parameters
    if args.verbose:
        print "\nShow command line parameters ..."
        print "\tinfile = %s" % (args.infile.name)
        print "\tprog = %s" % (parser.prog)
        print "\tdata:\n%s" % (args.infile.read())

    print "\nDump XML document ..."
    print employees.dump()

    print "\nShow turnover for an employee ..."
    turnover = employees.getByName('frank')
    print "\ttotal turnover for frank: %s" % ("${:,}".format(turnover))

    print "\nShow turnover by id ..."
    turnover = employees.getById('003')
    print "\ttotal turnover for 003: %s" % ("${:,}".format(turnover))

    print "\nShow turnover for employee in year 2012 ..."
    turnover = employees.getByYear('frank', 2012)
    print "\tturnover for frank in 2012: %s" % ("${:,}".format(turnover))

    print "\nShow turnover for 2012"
    turnover = employees.getAllByYear(2012)
    print "\ttotal turnover in 2012 is %s" % ("${:,}".format(turnover))

#
# MAIN
#
if __name__ == '__main__':
    main(sys.argv)
    sys.exit(0)

#EOF
