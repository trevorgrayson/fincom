PYTHON=python
DEPDIR=.venv
export PYTHONPATH=.:$(DEPDIR)

test: compile
	$(PYTHON) -m pytest

integ:
	echo 'client testing'
	
compile: $(DEPDIR)
$(DEPDIR): requirements.txt
	$(PYTHON) -m pip install -t $(DEPDIR) -r requirements.txt

nut: compile
	# make etl
	# python normalize_download.py
	$(PYTHON) src/python/total.py

etl: compile
	./bin/etl

sheets: compile
	$(PYTHON) src/python/services/google/sheets.py

clean:
	find . -name "*.pyc" -delete
	rm -rf $(DEPDIR)

validate:
	python -m py_compile `find . -name *.py`
