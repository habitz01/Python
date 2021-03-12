from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import StringVar
import sqlite3 # for sqlite db support
#from gui.net_gui_wrapper import *
#from db.db_devices import *



class list_devices_class():

    ####### Functions ###################################################################################
    
    def close_list(self):
        self.close_confirmation=messagebox.askquestion("Close", "Are you sure you want to close?")

        if self.close_confirmation=="yes":
            self.list.destroy()

    def update_rows(self, rows):
        self.trv.delete(*self.trv.get_children())
        for row in rows:
            self.trv.insert('', 'end', values=row)
   
    def get_device_list(self):
    
        db_connection=sqlite3.connect("devices")
        db_cursor=db_connection.cursor()

        try:
            self.query_get="SELECT * FROM devices"
            db_cursor.execute(self.query_get)
            self.devices=db_cursor.fetchall()
            return self.devices

        except:
            messagebox.showinfo("DB", "Unable to get the list of devices from db list")

    def search(self):

        db_connection=sqlite3.connect("devices")
        db_cursor=db_connection.cursor()

        try: 
            self.search_device=self.search_entry.get()
            self.query_search="SELECT * FROM devices WHERE hostname LIKE '%"+self.search_device+"%' OR ip LIKE '%"+self.search_device+"%'"
            db_cursor.execute(self.query_search)
            self.devices=db_cursor.fetchall()
            self.update_rows(self.devices)
        except:
            messagebox.showinfo("DB", "Unable to get the list of devices from db search")
    
    def clear(self):

        self.searchvar.set("")
        db_connection=sqlite3.connect("devices")
        db_cursor=db_connection.cursor()

        try: 
            self.search_device=self.search_entry.get()
            self.query_clear="SELECT * FROM devices"
            db_cursor.execute(self.query_clear)
            self.devices=db_cursor.fetchall()
            self.update_rows(self.devices)
        except:
            messagebox.showinfo("DB", "Unable to get the list of devices from db search")

    def get_device(self, event):
        self.rowid=self.trv.identify_row(event.y)
        self.item=self.trv.item(self.trv.focus())
        self.selectvar.set(self.item['values'][2])
        self.returndevice=self.selectvar.get()
        print ("IP: ", self.returndevice)

    def get_device_ip(self):
        return self.returndevice 

    '''
    def select():
        if selectvar.get() =="":
            messagebox.showinfo("Select", "No device were selected")
        else:
            print("Select")
            returndevice=selectvar.get()
            print("Retunr device: ", returndevice)
            return
    '''
        
        
    #####################################################################################################

    def __init__(self, list):

        self.list=list
        self.list.title("Get Device")
        self.list.attributes("-topmost", True)
        self.list.geometry("670x500")
        self.list.iconbitmap('C:/Users/rh682g/Google Drive/github/Python/apps/networking/gui/net_ico.ico')


    ####### Top Frame ########################################################################################

        self.top_frame=Frame(self.list)
        self.top_frame.pack()

    ### Wrappers ########################################################################################

        self.wrapper1=LabelFrame(self.list, text="Device List")
        self.wrapper2=LabelFrame(self.list, text="Search")
        self.wrapper3=LabelFrame(self.list, text="Select")

        self.wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
        self.wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
        self.wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

    ### Treeview ########################################################################################

    ## scroll

        self.trv_scroll=Scrollbar(self.wrapper1)
        self.trv_scroll.pack(side=RIGHT, fill=Y)
    

    ## treeview 

        self.trv=ttk.Treeview(self.wrapper1, yscrollcommand=self.trv_scroll.set ,columns=(1,2,3), show="headings", height="12")
        self.trv.pack()

        self.trv.heading(1, text="Device ID")
        self.trv.heading(2, text="Device Hostname")
        self.trv.heading(3, text="Device IP")

    ## scroll config

        self.trv_scroll.config(command=self.trv.yview)

        self.device_list=self.get_device_list()
        self.update_rows(self.device_list)

    ## double click

        self.trv.bind('<Double 1>', self.get_device)

        self.device_list=self.get_device_list()
        self.update_rows(self.device_list)

    ### Search ########################################################################################

        self.searchvar=StringVar()

  
        self.search_entry=ttk.Entry(self.wrapper2, textvariable=self.searchvar)
        self.search_entry.pack(side=tk.LEFT, padx=6)

        self.search_button=Button(self.wrapper2, text="Search", command=self.search)
        self.search_button.pack(side=tk.LEFT, padx=6)

        self.clear_button=Button(self.wrapper2, text="Clear", command=self.clear)
        self.clear_button.pack(side=tk.LEFT, padx=6)

    ### Select ########################################################################################

        self.selectvar=StringVar()

        self.select_entry=ttk.Entry(self.wrapper3, textvariable=self.selectvar)
        self.select_entry.pack(side=tk.LEFT, padx=6)

        self.select_button=Button(self.wrapper3, text="Selection")
        self.select_button.pack(side=tk.LEFT, padx=6)

        list.mainloop()
