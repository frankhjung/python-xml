#!/usr/bin/env python
# coding: utf-8

"""
Read Employee data to return turnover information.
This is a example Python program to read and process XML files.
"""

from employees.employees import Employees
import argparse
import logging
import os.path
import sys


def main(argv=sys.argv):

    """ Test employees class. """

    __version__ = '0.3.0'

    parser = argparse.ArgumentParser(
        prog=os.path.basename(argv[0]),
        usage='%(prog)s [options]',
        description='a Python example program to show XML processing',
        epilog='© 2013-2018 Frank H Jung mailto:frankhjung@linux.com')
    parser.add_argument(
        'infile',
        nargs='?',
        type=argparse.FileType('r'),
        default='data/test.xml',
        help='alternate XML file to test')
    parser.add_argument(
        '-v',
        '--verbose',
        help='verbose output',
        action='count')
    parser.add_argument(
        '--version',
        action='version',
        version=__version__)

    # process command line arguments
    args = parser.parse_args()
    prog = parser.prog
    infile = args.infile
    verbose = args.verbose

    # show command parameters
    logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO)
    logger = logging.getLogger(__name__)
    if verbose:
        logger.setLevel(logging.DEBUG)

    # load employees from XML
    e = Employees(infile)

    logger.debug("infile ......................: {}".format(infile.name))
    logger.debug("prog ........................: {}".format(prog))
    logger.debug("verbose .....................: {}".format(verbose))
    logger.debug("dump ........................: \n{}".format(e.dump()))

    t = e.getById(3)
    logger.debug("name for id 3 ...............: {}".format(t))

    t = e.getByName('frank')
    logger.debug("turnover for frank ..........: ${:,}".format(t))

    t = e.getByYear(2012, 'frank')
    logger.debug("turnover for frank in 2012 ..: {}".format(t))

    t = e.getTotalByYear(2012)
    logger.debug("turnover for 2012 ...........: ${:,}".format(t))

    return 0


#
# MAIN
#
if __name__ == '__main__':
    rc = main(sys.argv)
    sys.exit(rc)

# EOF
