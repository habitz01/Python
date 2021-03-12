import sqlite3 # for sqlite db support
from tkinter import messagebox



### Create DB

def db_create():
    db_connection=sqlite3.connect("devices")
    
    db_cursor=db_connection.cursor()

    try:
        db_cursor.execute('''
            CREATE TABLE devices(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hostname VARCHAR(50),
            ip VARCHAR(15))
            ''')
        messagebox.showinfo("DB", "DB successfully created")
    except:
        messagebox.showinfo("DB", "DB already exist")

### Create Device

def device_create(hostname, ip):

    db_connection=sqlite3.connect("devices")
    
    db_cursor=db_connection.cursor()

    try:
        db_cursor.execute(" INSERT INTO DEVICES VALUES(MULL, '" + hostname + 
        "','" + ip + "')")

        messagebox.showinfo("DB", "Device successfully created")
    except:
        messagebox.showinfo("DB", "Device was not created")
