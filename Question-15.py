import csv

with open('data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')       # Creating a reader object

    for row in csvreader:                                # Printing each row of the file
        print(', '.join(row))
