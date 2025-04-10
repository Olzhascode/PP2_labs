import psycopg2
import csv

conn = psycopg2.connect(
    dbname="phonebook",
    user="postgres",
    password="Kesha2412:)",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Insert data from CSV
def insert_from_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            cur.execute("INSERT INTO phonebook (first_name, phone_number) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    print("Data from CSV inserted")


# Insert data from console
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    cur.execute("INSERT INTO phonebook (first_name, phone_number) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("Entry inserted.")