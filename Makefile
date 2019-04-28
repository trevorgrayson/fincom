test:
	py.test

nut:
	make etl
	python normalize_download.py
	python total

etl:
	./bin/etl
