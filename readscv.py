import csv

with open('data.csv', mode='r') as file:
    csvFileReader = csv.reader(file)

    # displaying the contents of the CSV file
    for lines in csvFileReader:
        print(lines)
