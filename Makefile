install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
lint:
	pylint --disable=R,C beautiful_soup.py
format:
	black *.py
test:
	python -m pytest -vv --cov=hello beautiful_soup_test.py
deploy:
	echo "CD"
all: install lint test