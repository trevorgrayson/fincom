import csv

with open("/Users/trevor.grayson/Downloads/bk_download (1).csv", "r") as bank:
    reader = csv.reader(bank)

    total = 0
    months = {}

    for row in reader:
        month = int(row[2].split('/')[0])
        amount = float(row[6])

        months[month] = months.get(month, 0) + amount
        total += amount

    for k, v in months.iteritems():
        print k, v
    print total + 1500 * 12


    print total * 25

    # -2,935,066.5
