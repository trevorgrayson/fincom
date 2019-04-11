# fincom
Financial Wealth Management Tools

It's the goal of this tool to be useful to the laymen.  Additional scripts and 
resources may be added that would require programming skills, but they shouldn't
confuse the primary workflow to get to the basic functionality of the app.

The basic goal of this repository is to create an open source FI/RE Calc that
can be iterated on.  The basic functionality should be a mobile friendly 
retirement page, that can be stored on people's phones.

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


## Saving Progress

Progress will be saved in their cookies, unless refused by the user. This 
should provide a reasonable amount of discretion on users data, if they keep
their phone locked.  If the user options to, there could be additional 
functionality in a future release to provide central statistics of this data.
Salary, rent prices, saving rates, etc.

### "Backing Up" User Data 

In the case of a user who does not wish to store their data, or also for 
those who wish to transfer their data, the following "Save Code" system will 
be implemented.

A retirement calculator only requires several relatively small, numerical 
values to define it's inputs.  

Input Values include:


Value Name | Max Value | Required Bits | Required Hex Size | Justification/Description
--- | --- | --- | ---

Present Age | 110 | FF | Could be omitted if not yet retired.
Life Expectancy | 110 | FF | Approximating the value of human records.
Inflation Rate | 100 | FF | Note, there could be 155 wasted bits here if letters mapped exclusively to their letters | This is pretty much regulated to stay around 2.5%.
Net Worth | 1 Tillion | FFFFFFFFFFFF | In the world today, no one person that exists with a net worth in the excess of 100B dollars. Net Worth growth rate should be considered further, but this is a good approximate for now. To give you a good idea of the disparity in peoples financial differences: it takes 12 chars to represent the wealthiest individuals, while the "average" american would take 5 or less. |
Income 
Income Growth Rate
Social Security Benefits | 10000/wk | | | *Per Unit Time *Up to year
Investment Growth
Tax Growth Expectation | 100%/yr | | | Rounded to a day

Making an average person's code to be less than $F93D5

The default values go towards the beginning, and the last digits always represent their networth.

### Improving these values

These values can change drastically, so tools and documentation will be made to both tell the user how to approximate quickly, and how to reach it out thoroughly.
