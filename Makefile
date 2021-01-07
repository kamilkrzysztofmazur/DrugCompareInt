install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
lint:
	pylint --disable=R,C BeautifulSoup.py
format:
	black *.py
test:
	python -m pytest -vv --cov=hello BeautifulSoup_test.py
deploy:
	echo "CD"
all: install lint test