test:
	py.test

build:
	pip install -r requirements.txt

nut:
	make etl
	python normalize_download.py
	python total

etl:
	./bin/etl

clean:
	find . -name "*.pyc" -delete

