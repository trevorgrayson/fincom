test:
	py.test

build:
	pip install -r requirements.txt

nut:
	# make etl
	# python normalize_download.py
	python src/python/total.py

etl:
	./bin/etl

sheets:
	python src/python/services/google/sheets.py

clean:
	find . -name "*.pyc" -delete

