# Manage project
#
# You can run unittests using ...
# - python testemployees.py
# - unit2 discover -v
# - python -m unittest discover -v

COVER_DIR = target/cover

.PROXY: all

all: check cover test doc

check:
	# Check with PyChecker
	pychecker --only main.py employees.py testemployees.py
	# Check with Pep8
	pep8 main.py employees.py testemployees.py 

cover:
	# Run main module
	python-coverage run --include=main.py,employees.py main.py -v test.xml
	# Run all unit tests (append results)
	python-coverage run -a --include=testemployees.py,employees.py testemployees.py
	# Annotate file to see what has been tested
	python-coverage annotate employees.py
	# Generate coverage report
	python-coverage report --include=testemployees.py,employees.py,main.py 

test:
	# Run unit tests (unit2 discover -v)
	python -m unittest discover -v

doc: force_doc
	# Creating coverage HTML report
	$(RM) -rf $(COVER_DIR)
	python-coverage html -d $(COVER_DIR)
	# Create Sphinx documentation
	(cd doc; make html)

clean:
	# Cleaning workspace
	$(RM) -f *,cover
	$(RM) -f *.pyc
	$(RM) -rf target
	python-coverage erase
	(cd doc; make clean)

force_doc:
	true

#EOF
