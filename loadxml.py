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
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default='test.xml', help='alternate XML file to test')
    parser.add_argument('-v', '--verbose', help='verbose output', action='count')
    parser.add_argument('--version', action='version', version='%(prog)s 0.0.1')
    
    # process command line arguments
    args = parser.parse_args()
    infile = args.infile
    verbose = args.verbose

    # load XML document from file
    xmldoc = xml.etree.ElementTree.parse(infile.name)

    # show turnover for a specific year
    print "\n(1) show value for a specific year."
    turnover = getYear(xmldoc, '2012')
    print "\tYear 2012 has turnover of %s" % (turnover)

    # show turnover for all years
    print "\n(2) show turnover for all years."
    turnovers = getAllYears(xmldoc)
    for t in turnovers:
        print "\tYear %s has turnover of %s" % (t.attrib['id'], t.text)

    # show command parameters
    if verbose:
        print "\n(3) dump XML file"
        print "\tverbose = %s" % (verbose)
        print "\tinfile = %s" % (infile.name)
        print "\tdata:\n%s" % (infile.read())

    # dump XML document
    if verbose:
        print "\n(4) dump the XML that was read"
        xml.etree.ElementTree.dump(xmldoc)

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
