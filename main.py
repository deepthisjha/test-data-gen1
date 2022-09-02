import csv
# open the file in the write mode
with open('data.csv', 'w') as file:
    # create the csv writer
    header=[id, 'name', 'product']
    input_data=[[1,'ram','bow'],
                [2, 'dsj','toy'],
                [3, 'srj','book']]
    writer = csv.writer(file)


    writer.writerow(header)
    writer.writerows(input_data)


