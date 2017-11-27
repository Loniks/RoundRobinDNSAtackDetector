original = []

header = []

import csv

# read all lines
with open('dump.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        if not row[5].isdigit():
            header = row
        else:
            original.append(row)

good = []
bad = []

# find number of pairs

dictionary = {}

for row in original:
    key = '{}-{}'.format(row[2], row[4])
    if key not in dictionary:

        dictionary[key] = {row[3]}
    else:
        set = dictionary.get(key)
        set.add(row[3])
        dictionary[key] = set

good = []

bad = []

# split rows
for row in original:
    key = '{}-{}'.format(row[2], row[4])
    if len(dictionary.get(key))>1:
        bad.append(row)
    else:
        good.append(row)

# save into separate files

with open('dump_good.csv', 'w') as fp:
    writer = csv.writer(fp, delimiter=',', lineterminator='\n')
    writer.writerow(header)
    writer.writerows(good)

with open('dump_bad.csv', 'w') as fp:
    writer = csv.writer(fp, delimiter=',', lineterminator='\n')
    writer.writerow(header)
    writer.writerows(bad)
