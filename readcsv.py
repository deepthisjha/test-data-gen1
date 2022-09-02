import csv
import psycopg2


with open('data.csv', mode='r') as file:
    csvFileReader = csv.reader(file)

    # Create DB Connection
    con = psycopg2.connect(
        host='127.0.0.1',
        port='5432',
        user='d2sdb',
        password='qwerty123',
        database="d2sdb"
    )
    cursor = con.cursor()

    cursor.execute(''' select * from customer ''')
    records = cursor.fetchall()

    print("Currently in DB")
    print(records)


    # displaying the contents of the CSV file
    for line in csvFileReader:
        print(line)
        cursor.execute("insert into customer (id, name,product) values (%s, %s, %s)", line)

    con.commit()
    con.close()



