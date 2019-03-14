import csv
import glob

def to_number(string):
    return float(string.replace(',','').replace('$',''))

def normalize(folder):
    rows = []
    for filename in glob.glob(folder + "/*"):
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            reader.next()
            rows.extend([dict(
                title=row[1],
                symbol=row[0],
                price=to_number(row[3]),
                quantity=to_number(row[2])
            ) for row in reader])

    return rows

if __name__ == '__main__':
    for row in normalize('data/2019-03-13'):
        print(row)
