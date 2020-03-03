init:
	pip install -r requirements.txt

install:
	pip install -r requirements.txt
	python setup.py install --user

test:
	nosetests tests

