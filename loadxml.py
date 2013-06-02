#!/usr/bin/python

"""
Simple example to demonstrate Python's ability to read from an XML file.
"""

import getopt
import os.path
import pprint
import re
import sys
import xml.dom.minidom
import xml.etree.ElementTree

""" Constants """
TEST_XML = 'test.xml'

def usage():
    """ Print usage message. """
    print """
NAME

    loadxml - a Python example program to show XML processing

SYNOPSIS

    loadxml [options]

OPTIONS

    -f filename     alternate XML document
    -h              help
    -v              verbose
"""

def main(argv):
    """ Parse command line parameters, process XML document. """
    try:
        opts, args = getopt.getopt(argv, 'hvf:', ['help', 'verbose', 'file='])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    # process command line parameters
    filename = TEST_XML
    verbose = False
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit(0)
        elif opt in ('-v', '--verbose'):
            verbose = True
        elif opt in ('-f', '--file'):
            filename = arg

    # show command parameters
    example = 0
    if verbose:
        example += 1
        print "\n(%s) show a specific year" % (example)
        print "\tverbose = %s" % (verbose)
        print "\tfilename = %s" % (filename)

    # load XML document from file
    xmldoc = loadFromFile(filename)

    # dump XML document
    if verbose:
        example += 1
        print "\n(%s) dump the XML that was read" % (example)
        xml.etree.ElementTree.dump(xmldoc)

    # show turnover for a specific year
    example += 1
    print "\n(%s) show value for a specific year." % (example)
    turnover = getYear(xmldoc, '2012')
    print "\tYear 2012 has turnover of %s" % (turnover)

    # show turnover for all years
    example += 1
    print "\n(%s) show turnover for all years." % (example)
    turnovers = getAllYears(xmldoc)
    for t in turnovers:
        print "\tYear %s has turnover of %s" % (t.attrib['id'], t.text)

def loadFromFile(name):
    """ Load XML from file. """
    if not os.path.exists(name):
        print "ERROR: file %s not found" % name
        sys.exit(1)
    return xml.etree.ElementTree.parse(name)

def getYear(doc, year):
    """ Show turnover for a specific year. """
    xpath = ".//turnover/year[@id='%s']" % (year)
    for y in doc.findall(xpath):
        return y.text

def getAllYears(doc):
    """ Show turnover for all years. """
    return doc.findall(".//turnover/year")

#
# MAIN
#
if __name__ == '__main__':
    main(sys.argv[1:])
    sys.exit(0)
