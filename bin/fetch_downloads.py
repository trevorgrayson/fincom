import glob


print 't'
filenames = glob.glob('/Users/trevor.grayson/Downloads/im_positions*')

count = 0
with open('/Users/trevor.grayson/projects/fincom/usaa.csv', 'w') as local:

    for filename in filenames:
        print 'opening %s' % filename
        with open(filename, 'r') as account:

            for line in account:
                count = count + 1
                if not line[0:6] == "Symbol":
                    local.write(line)

print count
