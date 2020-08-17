include Makef.io

PYTHON=python
DEPDIR=.venv
export PYTHONPATH=.:$(DEPDIR)

compile: $(DEPDIR)
$(DEPDIR): requirements.txt
	$(PYTHON) -m pip install -t $(DEPDIR) -r requirements.txt

nut: compile # etl
	# python normalize_download.py
	$(PYTHON) src/python/total.py

etl: compile
	./bin/etl

sheets: compile
	$(PYTHON) src/python/services/google/sheets.py

clean:
	find . -name "*.pyc" -delete
	rm -rf $(DEPDIR)
