from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3 # for sqlite db support
from gui.create_devices_gui import *



def crud_devices_gui():

    ####### Functions ###################################################################################
    
    def close():
        close_confirmation=messagebox.askquestion("Close", "Are you sure you want to close?")

        if close_confirmation=="yes":
            crud.destroy()

    def update_rows(rows):
        trv.delete(*trv.get_children())
        for row in rows:
            trv.insert('', 'end', values=row)
            
   
    def get_device_list():
    
        db_connection=sqlite3.connect("devices")
        db_cursor=db_connection.cursor()

        try:
            query1="SELECT * FROM devices"
            db_cursor.execute(query1)
            devices=db_cursor.fetchall()
            return devices

        except:
            messagebox.showinfo("DB", "Unable to get the list of devices from db list")

    def search():

        db_connection=sqlite3.connect("devices")
        db_cursor=db_connection.cursor()

        try: 
            search_device=search_entry.get()
            query2="SELECT * FROM devices WHERE hostname LIKE '%"+search_device+"%' OR ip LIKE '%"+search_device+"%'"
            db_cursor.execute(query2)
            devices=db_cursor.fetchall()
            update_rows(devices)
        except:
            messagebox.showinfo("DB", "Unable to get the list of devices from db search")
    
    def clear():

        searchvar.set("")
        db_connection=sqlite3.connect("devices")
        db_cursor=db_connection.cursor()

        try: 
            search_device=search_entry.get()
            query2="SELECT * FROM devices"
            db_cursor.execute(query2)
            devices=db_cursor.fetchall()
            update_rows(devices)
        except:
            messagebox.showinfo("DB", "Unable to get the list of devices from db search")
    
    def get_device(event):
        rowid=trv.identify_row(event.y)
        item=trv.item(trv.focus())

        device_id.set(item['values'][0])
        device_hostname.set(item['values'][1])
        device_ip.set(item['values'][2])
   
    def create_device():
        create_devices_gui()
        
    
    def edit_device():
        return True
    
    def delete_device():

        db_connection=sqlite3.connect("devices")
        db_cursor=db_connection.cursor()

        id1=device_id.get()
        
        if messagebox.askyesno("Delete", "Are you sure you want to delete the device?"):

            try:
                query2="DELETE FROM devices WHERE id = "+id1
                db_cursor.execute(query2)
                db_connection.commit()
                messagebox.showinfo("DB", "Device deleted")
                clear()
                device_id.set("")
                device_hostname.set("")
                device_ip.set("")
            except:
                messagebox.showinfo("DB", "Device was not deleted")
                
        else:
            return True


    #####################################################################################################
    
    #crud=Tk()
    crud=tk.Toplevel()
    crud.title("Create Device")
    crud.attributes("-topmost", True)
    crud.geometry("670x500")
    crud.iconbitmap('C:/Users/rh682g/Google Drive/github/Python/apps/networking/gui/net_ico.ico')

 
    ####### Top Frame ########################################################################################

    top_frame=Frame(crud)
    top_frame.pack()

    ### Wrappers ########################################################################################

    wrapper1=LabelFrame(crud, text="Device List")
    wrapper2=LabelFrame(crud, text="Search")
    wrapper3=LabelFrame(crud, text="Create / Edit / Delete")

    wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
    wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
    wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

    ### Treeview ########################################################################################

    ## scroll

    trv_scroll=Scrollbar(wrapper1)
    trv_scroll.pack(side=RIGHT, fill=Y)
    

    ## treeview 

    trv=ttk.Treeview(wrapper1, yscrollcommand=trv_scroll.set ,columns=(1,2,3), show="headings", height="6")
    trv.pack()

    trv.heading(1, text="Device ID")
    trv.heading(2, text="Device Hostname")
    trv.heading(3, text="Device IP")

    ## scroll config

    trv_scroll.config(command=trv.yview)

   ## double click

    trv.bind('<Double 1>', get_device)

    device_list=get_device_list()
    update_rows(device_list)

    #command_scroll=ttk.Scrollbar(top_frame, orient=VERTICAL, command=listbox.yview)
    #listbox.configure(yscrollcommand=s.set)

    ### Search ########################################################################################

    searchvar=StringVar()

  
    search_entry=ttk.Entry(wrapper2, textvariable=searchvar)
    search_entry.pack(side=tk.LEFT, padx=6)

    search_button=Button(wrapper2, text="Search", command=search)
    search_button.pack(side=tk.LEFT, padx=6)

    search_button=Button(wrapper2, text="Clear", command=clear)
    search_button.pack(side=tk.LEFT, padx=6)

    ####### Device ####################################################################################

    ### Labels ########################################################################################

    id_label=Label(wrapper3, text="ID: ")
    id_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)

    hostname_label=Label(wrapper3, text="Hostname: ")
    hostname_label.grid(row=1, column=0, sticky="e", padx=10, pady=10)

    device_ip_label=Label(wrapper3, text="Device IP: ")
    device_ip_label.grid(row=2, column=0, sticky="e", padx=10, pady=10)

    ### Entry ########################################################################################

    
    device_id=StringVar()
    device_hostname=StringVar()
    device_ip=StringVar()
  
    id_entry=ttk.Entry(wrapper3, textvariable=device_id)
    #id_entry=ttk.Entry(wrapper3)
    id_entry.grid(row=0, column=1, padx=5, pady=3)
    id_entry.config(justify="right")

    hostname_entry=ttk.Entry(wrapper3, textvariable=device_hostname)
    #hostname_entry=ttk.Entry(wrapper3)
    hostname_entry.grid(row=1, column=1, padx=5, pady=3)
    hostname_entry.config(justify="right")

    device_ip_entry=ttk.Entry(wrapper3, textvariable=device_ip)
    #device_ip_entry=ttk.Entry(wrapper3)
    device_ip_entry.grid(row=2, column=1, padx=5, pady=3)
    device_ip_entry.config(justify="right")

    ### Buttons ########################################################################################

    create_button=Button(wrapper3, text="Create", command=create_device)
    create_button.grid(row=3, column=0, padx=5, pady=3)


    edit_button=Button(wrapper3, text="Update", command=edit_device)
    edit_button.grid(row=3, column=1, padx=5, pady=3)

    delete_button=Button(wrapper3, text="Delete", command=delete_device)
    delete_button.grid(row=3, column=2, padx=5, pady=3)

    close_button=Button(wrapper3, text="Close", command=close)
    close_button.grid(row=3, column=5, padx=210, pady=3)


    crud.mainloop()

#crud_devices_gui()