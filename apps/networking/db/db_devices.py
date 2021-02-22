import sqlite3 # for sqlite db support
from tkinter import messagebox



### Create DB

def db_create():
    devices_db_connection=sqlite3.connect("devices")
    
    devices_db_cursor=devices_db_connection.cursor()

    try:
        devices_db_cursor.execute('''
            CREATE TABLE DEVICES(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            HOSTNAME VARCHAR(50),
            IP VARCHAR(15))
            ''')
        messagebox.showinfo("DB", "DB successfully created")
    except:
        messagebox.showinfo("DB", "DB already exist")

def device_create():
    devices_db_connection=sqlite3.connect("devices")
    
    devices_db_cursor=devices_db_connection.cursor()

    try:
        devices_db_cursor.execute('''
            CREATE TABLE DEVICES(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            HOSTNAME VARCHAR(50),
            IP VARCHAR(15))
            ''')
        messagebox.showinfo("DB", "DB successfully created")
    except:
        messagebox.showinfo("DB", "DB already exist")
