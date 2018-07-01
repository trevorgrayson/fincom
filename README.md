# fincom
Financial Wealth Management Command-line utils

Shooting to be compatible with both python 2.7 and 3 for maximum usability 
and minimum dependency


## Add CSVs of assets

* portfolio.csv
** Format: "Ticker, Name (optional), Quantity"
* crypto.csv
** Format: "Ticker, Quantity"


## Build portfolio.csv
You're going to need to get a list of your assets, so 
use the included scripts, or you can manually make one 
in the format:

```
Symbol, Readable Name, Quantity
```


Total Value:

```
  ./bin/total.py
```

Get total coming in, and total expenses going out, by month.

```
  burnrate.py
```
