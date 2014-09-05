# Manage project
#
# You can run unittests using ...
# - python -m test.testemployees -v
# - python -m unittest discover -v

.DEFAULT_GOAL := help
.PHONY: check run test doc clean help

COMMA:= ,
EMPTY:=
SPACE:= $(EMPTY) $(EMPTY)

COVER_DIR = target/cover
# srcs used by pychecker
SRCS=main.py employees/employees.py test/testemployees.py
SRCS_LIST=$(subst $(SPACE),$(COMMA),$(SRCS))

all: check cover run test doc dist

help:
	@echo
	@echo "Default goal: ${.DEFAULT_GOAL}"
	@echo "  all:   check cover run test doc dist"
	@echo "  check: validate code and distribution config"
	@echo "  cover: run test coverage report"
	@echo "  run:   run against test data"
	@echo "  test:  run unit test"
	@echo "  doc:   create documentation including test converage and results"
	@echo "  dist:  create a distrbution archive"
	@echo "  clean: delete all generated files"
	@echo

check:
	# Check with PyChecker
	pychecker --only $(SRCS)
	# Check with Pep8
	pep8 --verbose $(SRCS)
	# Check distutils
	python setup.py check

cover:
	# Run main module
	python-coverage run --include=main.py,employees.employees.py -m main
	# Run main module with verbose and test data
	python-coverage run -a --include=main.py,employees.employees.py -m main -v data/test.xml
	# Run unit tests (append results)
	python-coverage run -a --include=main.py,employees.employees.py -m test.testemployees
	# Annotate file to see what has been tested
	python-coverage annotate employees/employees.py main.py
	# Generate unit test coverage report
	python-coverage report

run:
	# Run main
	python -m main -v data/test.xml

test:
	# Run unit tests
	# python -m unittest discover -v
	# List nodetests plugins using nosetests --plugins -vv
	# Make directory for HTML test results to be included in documentation
	mkdir -p target/test
	# Search test directory
	nosetests --config=test/nosetests.cfg --verbose --where $(PWD) test/test*.py
	# Compare with
	# python -m test.testemployees -v
	# Test documentation (run coverage first)
	# (cd docs; make doctest; make linkcheck)

doc:
	# Creating coverage HTML report to be included in final documentation
	$(RM) -rf $(COVER_DIR)
	python-coverage html -d $(COVER_DIR)
	# Create Sphinx documentation
	(cd docs; make singlehtml)

dist:
	# Copy readme for use in distribution
	cp -f README.md README
	# Create source package and build distribution
	python setup.py clean
	python setup.py sdist --dist-dir=target/dist 
	python setup.py build --build-base=target/build

clean:
	# Cleaning workspace
	python-coverage erase
	# Clean build distribution
	python setup.py clean
	# Clean generated documents
	(cd docs; make clean)
	$(RM) -rf target
	$(RM) -v *,cover
	$(RM) -v employees/*.pyc employees/*.pyo employees/*.py,cover
	$(RM) -v MANIFEST
	$(RM) -v .noseids
	$(RM) -v *.pyc *.pyo *.pyo,cover
	$(RM) -v README
	$(RM) -v test/*.pyc test/*.pyo test/*.py,cover

#EOF
