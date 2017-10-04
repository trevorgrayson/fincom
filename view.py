import locale
# https://stackoverflow.com/questions/320929/currency-formatting-in-python

def unit_total(sym, unit_price, total):
    total = "%9.2f" % total
    print "%s\t%7.2f\t\t%s" % (sym, unit_price, total.rjust(9, ' '))

def total(label, value):
    print "%s:\t\t\t%9.2f" % (label, value)
