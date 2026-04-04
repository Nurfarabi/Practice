from connect import get_connection
import csv

#  Insert / Update 
def insert_contact(name, phone):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "CALL upsert_contact(%s, %s)",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()


# Bulk insert из CSV 
def insert_from_csv(file):
    conn = get_connection()
    cur = conn.cursor()

    names = []
    phones = []

    with open(file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) >= 2:
                names.append(row[0])
                phones.append(row[1])

    cur.execute(
        "CALL bulk_insert_users(%s, %s)",
        (names, phones)
    )

    conn.commit()
    cur.close()
    conn.close()


# Search 
def search(keyword):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM get_contacts_by_pattern(%s)",
        (keyword,)
    )

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()


# Pagination 
def get_paginated(limit, offset):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM get_contacts_paginated(%s, %s)",
        (limit, offset)
    )

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()


# Delete (через procedure)
def delete(value):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "CALL delete_contact(%s)",
        (value,)
    )

    conn.commit()
    cur.close()
    conn.close()


# 🖥️ Menu
def menu():
    while True:
        print("1. Add / Update Contact")
        print("2. Load from CSV")
        print("3. Search")
        print("4. Pagination")
        print("5. Delete")
        print("6. Exit")

        choice = input("choice: ")

        if choice == "1":
            name = input("name: ")
            phone = input("phone: ")
            insert_contact(name, phone)

        elif choice == "2":
            insert_from_csv("contacts.csv")

        elif choice == "3":
            keyword = input("search: ")
            search(keyword)

        elif choice == "4":
            limit = int(input("limit: "))
            offset = int(input("offset: "))
            get_paginated(limit, offset)

        elif choice == "5":
            value = input("value to delete: ")
            delete(value)

        elif choice == "6":
            break

        else:
            print("Invalid choice")


menu()