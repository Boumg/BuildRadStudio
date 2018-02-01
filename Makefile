init:
	pip install -r requirements.txt
install:
    pip uninstall rxbuilder
	python setup.py install
test:
	nose2 test_rxbuilder