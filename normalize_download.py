import glob


headers = None

with open('portfolio.csv', 'w') as portfolio:
    for filename in glob.glob("downloads/im_pos*"):
        with open(filename, 'r') as csvfile:
            headers = csvfile.readline()
            # print headers

            for line in csvfile:
                line = line.split(',')
                portfolio.write(
                    ",".join([
                    line[0], # ticker
                    line[2], # Quantity
                    line[3]  # Price
                    ]) + '\n'
                )

