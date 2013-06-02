#!/usr/bin/python

"""
Simple example to demonstrate Python's ability to read from an XML file.
"""

import argparse
import sys
import xml.etree.ElementTree

def main(argv):
    """ Parse command line parameters, process XML document. """
    parser = argparse.ArgumentParser(
            prog='loadxml.py', 
            usage='%(prog)s [options]', 
            description='a Python example program to show XML processing',
            epilog='(c) 2013 Frank H Jung')
    parser.add_argument('--version', action='version', version='%(prog)s 0.0.1')
    parser.add_argument('-v', '--verbose', help='verbose output', action='count')
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default='test.xml', help='alternate XML file to test')
    
    # process command line arguments
    args = parser.parse_args()
    infile = args.infile
    verbose = args.verbose

    # show command parameters
    example = 0
    if verbose:
        example += 1
        print "\n(%s) dump XML file" % (example)
        print "\tverbose = %s" % (verbose)
        print "\tinfile = %s" % (infile.name)
        print "\tdata:\n%s" % (infile.read())

    # load XML document from file
    xmldoc = xml.etree.ElementTree.parse(infile.name)

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
