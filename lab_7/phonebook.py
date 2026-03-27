from connect import get_connection
import csv

#console insert
def insert_contact(name, phone):
    con= get_connection()
    cur = con.cursor()
    cur.execute(
        'INSERT INTO contacts (first_name, phone) VALUES (%s, %s)',
        (name, phone)
    )
    con.commit()
    cur.close()
    con.close()

#cvs insert
def insert_from_csv(contacts):
    conn = get_connection()
    cur = conn.cursor()
    with open(contacts ,'r') as file:
        reader = csv.reader(file)
        for row in reader:
            cur.execute(
                "INSERT INTO contacts (first_name, phone) VALUES(%s, %s)",
                (row[0], row[1])
            )
        conn.commit()
        cur.close()
        conn.close()

def search(keyword):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM contacts WHERE first_name ILIKE %s OR phone ILIKE %s",
        (f"%{keyword}", f"{keyword}%")
    )

    rows = cur.fetchall()
    for row in rows:
        print(row)
    
    cur.close()
    conn.close()

def update(old_name, new_name=None, new_phone=None):
    conn = get_connection()
    cur = conn.cursor()

    if new_name:
        cur.execute(
            "UPDATE contacts SET first_name = %s WHERE first_name = %s",
            (new_name, old_name)
        )
    if new_phone:
        cur.execute(
            "UPDATE contacts SET phone = %s WHERE first_name = %s",
            (new_phone, old_name)
        )

    conn.commit()
    cur.close()
    conn.close()

def delete(value):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM contacts WHERE first_name = %s OR phone = %s",
        (value, value)
    )
    
    conn.commit()
    cur.close()
    conn.close()

def menu():
     while True:
        print("1. Add Contact")
        print("2. Load from CSV")
        print("3. Search")
        print("4. Update")
        print("5. Delete")
        print("6. Exit")

        choice = input("choice: ")
        if choice =="1":
            name = input("name: ")
            phone= input("phone: ")
            insert_contact(name, phone)

        elif choice == "2":
            insert_from_csv("contacts.csv")
        
        elif choice == "3":
            keyword = input("input: ")
            search(keyword)
        elif choice == "4":
            old = input("Old name: ")
            new_name = input("new name: ")
            new_phone = input("new_phone: ")

            update(
                old,
                new_name if new_name else None,
                new_phone if new_phone else None
            )

        elif choice =="5":
            value = input("value to delete: ")
            delete(value)
        elif choice == "6":
            break

menu()