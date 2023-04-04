import csv
with open('testcsv.csv') as file:
    spamreader = csv.reader(file, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))


# use  this program to read or write a csv

# it use for   training the module