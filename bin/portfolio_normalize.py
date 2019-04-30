#!/usr/bin/env python
"""
    This is trying to take a large breadth of formats in
    and export a normalized form of usable portfolio data.

    This will need to get broken up in some sensible way to
    both infer values, or be directed by human inputs.
    Maybe finger printing file formats 
"""

import csv
from glob import glob
from format import *


if __name__ == "__main__":
    # move old portfolio
    with open('portfolio2.csv', 'w') as portfolio:
        #TODO remove im_positions
        for filename in glob('portfolio/im_positions*.csv'):
            # check for tabs or commas
            try:
                with open(filename, 'rb') as csvfile:
                    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                    for row in reader:
                        if is_header(row):
                            continue

                        if len(row) > 2:

                            if row[2] > 0:
                                # cost basis = value - gain / qt
                                qt = price_scrub(row[2])

                                if not qt:
                                    qt = 1.0

                                cost_basis = price_scrub(row[3]) - (price_scrub(row[6]) / qt)
                            else: 
                                cost_basis = row[3]

                            portfolio.write(format_row([
                                ticker_scrub(row[0]), 
                                "", 
                                row[2],
                                cost_basis,
                            ]))
                        else:
                            portfolio.write(format_row([
                                ticker_scrub(row[0]), 
                                "", 
                                row[1]
                            ]))


            except IOError: pass

