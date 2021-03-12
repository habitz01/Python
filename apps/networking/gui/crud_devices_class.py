from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3 # for sqlite db support
from gui.create_devices_class import *



class crud_devices_class():

    ####### Functions ###################################################################################
    
    def close(self):
        self.close_confirmation=messagebox.askquestion("Close", "Are you sure you want to close?")

        if self.close_confirmation=="yes":
            self.crud.destroy()

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

        self.device_id.set(self.item['values'][0])
        self.device_hostname.set(self.item['values'][1])
        self.device_ip.set(self.item['values'][2])
   
    def create_device(self):
        create=tk.Toplevel()
        create_gui=create_devices_class(create)
        
    
    def edit_device(self):
        return True
    
    def delete_device(self):

        db_connection=sqlite3.connect("devices")
        db_cursor=db_connection.cursor()

        self.id_delete=self.device_id.get()
        
        if messagebox.askyesno("Delete", "Are you sure you want to delete the device?"):

            try:
                self.query_delete="DELETE FROM devices WHERE id = "+self.id_delete
                db_cursor.execute(self.query_delete)
                db_connection.commit()
                messagebox.showinfo("DB", "Device deleted")
                self.clear()
                self.device_id.set("")
                self.device_hostname.set("")
                self.device_ip.set("")
            except:
                messagebox.showinfo("DB", "Device was not deleted")
                
        else:
            return True


    #####################################################################################################
    
    def __init__(self, crud):

        self.crud=crud
        self.crud.title("Create Device")
        self.crud.attributes("-topmost", True)
        self.crud.geometry("670x500")
        self.crud.iconbitmap('C:/Users/rh682g/Google Drive/github/Python/apps/networking/gui/net_ico.ico')

 
        ####### Top Frame ########################################################################################

        self.top_frame=Frame(self.crud)
        self.top_frame.pack()

        ### Wrappers ########################################################################################

        self.wrapper1=LabelFrame(self.crud, text="Device List")
        self.wrapper2=LabelFrame(self.crud, text="Search")
        self.wrapper3=LabelFrame(self.crud, text="Create / Edit / Delete")

        self.wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
        self.wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
        self.wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

        ### Treeview ########################################################################################

        ## scroll

        self.trv_scroll=Scrollbar(self.wrapper1)
        self.trv_scroll.pack(side=RIGHT, fill=Y)
    

        ## treeview 

        self.trv=ttk.Treeview(self.wrapper1, yscrollcommand=self.trv_scroll.set ,columns=(1,2,3), show="headings", height="6")
        self.trv.pack()

        self.trv.heading(1, text="Device ID")
        self.trv.heading(2, text="Device Hostname")
        self.trv.heading(3, text="Device IP")

        ## scroll config

        self.trv_scroll.config(command=self.trv.yview)

        ## double click

        self.trv.bind('<Double 1>', self.get_device)

        self.device_list=self.get_device_list()
        self.update_rows(self.device_list)




        #trv.bind('<Double 1>', get_device)

        #device_list=get_device_list()
        #update_rows(device_list)


        ### Search ########################################################################################

        self.searchvar=StringVar()

  
        self.search_entry=ttk.Entry(self.wrapper2, textvariable=self.searchvar)
        self.search_entry.pack(side=tk.LEFT, padx=6)

        self.search_button=Button(self.wrapper2, text="Search", command=self.search)
        self.search_button.pack(side=tk.LEFT, padx=6)

        self.search_button=Button(self.wrapper2, text="Clear", command=self.clear)
        self.search_button.pack(side=tk.LEFT, padx=6)

        ####### Device ####################################################################################

        ### Labels ########################################################################################

        self.id_label=Label(self.wrapper3, text="ID: ")
        self.id_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)

        self.hostname_label=Label(self.wrapper3, text="Hostname: ")
        self.hostname_label.grid(row=1, column=0, sticky="e", padx=10, pady=10)

        self.device_ip_label=Label(self.wrapper3, text="Device IP: ")
        self.device_ip_label.grid(row=2, column=0, sticky="e", padx=10, pady=10)

        ### Entry ########################################################################################

    
        self.device_id=StringVar()
        self.device_hostname=StringVar()
        self.device_ip=StringVar()
  
        self.id_entry=ttk.Entry(self.wrapper3, textvariable=self.device_id)
        self.id_entry.grid(row=0, column=1, padx=5, pady=3)
        self.id_entry.config(justify="right")

        self.hostname_entry=ttk.Entry(self.wrapper3, textvariable=self.device_hostname)
        self.hostname_entry.grid(row=1, column=1, padx=5, pady=3)
        self.hostname_entry.config(justify="right")

        self.device_ip_entry=ttk.Entry(self.wrapper3, textvariable=self.device_ip)
        self.device_ip_entry.grid(row=2, column=1, padx=5, pady=3)
        self.device_ip_entry.config(justify="right")

        ### Buttons ########################################################################################

        self.create_button=Button(self.wrapper3, text="Create", command=self.create_device)
        self.create_button.grid(row=3, column=0, padx=5, pady=3)


        self.edit_button=Button(self.wrapper3, text="Update", command=self.edit_device)
        self.edit_button.grid(row=3, column=1, padx=5, pady=3)

        self.delete_button=Button(self.wrapper3, text="Delete", command=self.delete_device)
        self.delete_button.grid(row=3, column=2, padx=5, pady=3)

        self.close_button=Button(self.wrapper3, text="Close", command=self.close)
        self.close_button.grid(row=3, column=5, padx=210, pady=3)


        crud.mainloop()

