import csv
from connect import connect

def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        phone VARCHAR(20)
    )
    """)
    conn.commit()
    conn.close()

# Insert from CSV
def insert_from_csv(filename):
    conn = connect()
    cur = conn.cursor()

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", row)

    conn.commit()
    conn.close()

# Insert from console
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    conn.close()

# Update contact
def update_contact():
    name = input("Enter name to update: ")
    new_phone = input("Enter new phone: ")

    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE contacts SET phone=%s WHERE name=%s", (new_phone, name))
    conn.commit()
    conn.close()

# Query with filters
def search():
    keyword = input("Search by name or phone prefix: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    SELECT * FROM contacts
    WHERE name ILIKE %s OR phone LIKE %s
    """, (f"%{keyword}%", f"{keyword}%"))

    results = cur.fetchall()
    for row in results:
        print(row)

    conn.close()

# Delete
def delete_contact():
    value = input("Enter name or phone to delete: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    DELETE FROM contacts
    WHERE name=%s OR phone=%s
    """, (value, value))

    conn.commit()
    conn.close()

# Menu
def menu():
    while True:
        print("\n1.Insert CSV\n2.Insert Console\n3.Update\n4.Search\n5.Delete\n6.Exit")
        choice = input("Choose: ")

        if choice == "1":
            insert_from_csv("contacts.csv")
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            search()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            break

create_table()
menu()