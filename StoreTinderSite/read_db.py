import os
import sqlite3
import json
from sqlite3 import Error
import django
from django.utils import timezone


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

def select_all_stores(conn, table_name):
    cur = conn.cursor()
    cur.execute("SELECT * FROM " + table_name)
    return cur

def main():
    # Open KFC's database for retrieving all stores information.
    db_file = "kfcstore.sqlite"
    table_name = "stores"
    id_count = 1
    conn = create_connection(db_file)
    cursor = select_all_stores(conn, table_name)

    # Open the default database for inserting stores information.
    db_file = "db.sqlite3"
    table_name = "StoreTinder_stores"
    conn2 = create_connection(db_file)
    cursor2 = select_all_stores(conn2, table_name)
    # Delete the table data before inserting to prevent duplicate data.
    cursor2.execute("DELETE FROM " + table_name)
    # Data to be inserted into the default table.
    for id, latitude, longitude, name, address, phone, weekdayopen, weekdayclose, weekendopen, weekendclose in cursor.fetchall():
        metadata = {"phone": phone, "weekdayopen": weekdayopen, "weekdayclose": weekdayclose, "weekendopen": weekendopen, "weekendclose": weekendclose}
        cursor2.execute("INSERT INTO " + table_name + " (id, name, latitude, longitude, address, source, metadata, created_at, updated_at, is_verified) VALUES (?,?,?,?,?,?,?,?,?,?)",
        (id_count, name, latitude, longitude, address, "KFC", json.dumps(metadata),
        timezone.now(), timezone.now(), 0))
        id_count += 1
    conn.close()
    conn2.commit()
    conn2.close()
    print("Successfully inserted data.")
    

if __name__=='__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "StoreTinderSite.settings")
    django.setup()
    main()
