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

sheets:
	python google/sheets.py

clean:
	find . -name "*.pyc" -delete

