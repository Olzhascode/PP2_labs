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

# Update data
def update_entry():
    old_name = input("Enter the name you want to update: ")
    new_name = input("Enter new name: ")
    new_phone = input("Enter new phone number: ")

    if new_name:
        cur.execute("UPDATE phonebook SET first_name = %s WHERE first_name = %s", (new_name, old_name))
    if new_phone:
        cur.execute("UPDATE phonebook SET phone_number = %s WHERE first_name = %s", (new_phone, new_name or old_name))

    conn.commit()
    print("Update completed.")


# Querying data
def search_entries():
    print("Search options:\n1. By name\n2. By phone")
    choice = input("Choose (1 or 2): ")
    if choice == '1':
        name = input("Enter name to search: ")
        cur.execute("SELECT * FROM phonebook WHERE first_name ILIKE %s", ('%' + name + '%',))
    else:
        phone = input("Enter phone to search: ")
        cur.execute("SELECT * FROM phonebook WHERE phone_number LIKE %s", ('%' + phone + '%',))

    rows = cur.fetchall()
    for row in rows:
        print(row)


# Delete data
def delete_entry():
    print("Delete by:\n1. Username\n2. Phone")
    choice = input("Choose (1 or 2): ")
    if choice == '1':
        name = input("Enter name to delete: ")
        cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
    else:
        phone = input("Enter phone to delete: ")
        cur.execute("DELETE FROM phonebook WHERE phone_number = %s", (phone,))

    conn.commit()
    print("Entry deleted.")

    # Menu
def menu():
    while True:
        print("\nPhoneBook Menu:")
        print("1. Insert from CSV")
        print("2. Insert from Console")
        print("3. Update Entry")
        print("4. Search Entries")
        print("5. Delete Entry")
        print("6. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            insert_from_csv("phonebook_data.csv")
        elif choice == '2':
            insert_from_console()
        elif choice == '3':
            update_entry()
        elif choice == '4':
            search_entries()
        elif choice == '5':
            delete_entry()
        elif choice == '6':
            break # Exit
        else:
            print("Invalid option. Try again.")

menu()

cur.close()
conn.close()

