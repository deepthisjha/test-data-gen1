import csv
import psycopg2
import random

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
        cursor.execute("insert into customer (id, name,product) values(%s, %s, %s)", line)
        # Add 10 random orders for a customer
    # cursor.execute("create table order(order_id int PRIMARY KEY, order_value int)")
    for i in range(0, 10):
        randomInts = [random.randint(1, 999999999), random.randint(1, 999999999)]
        cursor.execute("insert into order_summary(order_id,order_value) values(%s,%s)", randomInts)

    cursor.execute(''' select * from order_summary ''')
    records = cursor.fetchall()

    print("Currently in DB")
    print(records)
    con.commit()
    con.close()
