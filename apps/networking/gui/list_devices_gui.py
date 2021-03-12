from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import StringVar
import sqlite3 # for sqlite db support
#from gui.net_gui_wrapper import *
#from db.db_devices import *



def list_devices_gui():

    ####### Functions ###################################################################################
    
    def close_list():
        close_confirmation=messagebox.askquestion("Close", "Are you sure you want to close?")

        if close_confirmation=="yes":
            list.destroy()

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
            query2="SELECT * FROM devices WHERE hostname LIKE '%"+search_device+"%' OR ip LIKE '%"+search_device+"%'"
            db_cursor.execute(query2)
            devices=db_cursor.fetchall()
            update_rows(devices)
        except:
            messagebox.showinfo("DB", "Unable to get the list of devices from db search")

    def get_device(event):
        rowid=trv.identify_row(event.y)
        item=trv.item(trv.focus())
        selectvar.set(item['values'][2])
        returndevice=selectvar.get()

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
    
    #list=Tk()
    list=tk.Toplevel()
    list.title("Get Device")
    list.attributes("-topmost", True)
    list.geometry("670x500")
    list.iconbitmap('C:/Users/rh682g/Google Drive/github/Python/apps/networking/gui/net_ico.ico')


    ####### Top Frame ########################################################################################

    top_frame=Frame(list)
    top_frame.pack()

    ### Wrappers ########################################################################################

    wrapper1=LabelFrame(list, text="Device List")
    wrapper2=LabelFrame(list, text="Search")
    wrapper3=LabelFrame(list, text="Select")

    wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
    wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
    wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

    ### Treeview ########################################################################################

    ## scroll

    trv_scroll=Scrollbar(wrapper1)
    trv_scroll.pack(side=RIGHT, fill=Y)
    

    ## treeview 

    trv=ttk.Treeview(wrapper1, yscrollcommand=trv_scroll.set ,columns=(1,2,3), show="headings", height="12")
    trv.pack()

    trv.heading(1, text="Device ID")
    trv.heading(2, text="Device Hostname")
    trv.heading(3, text="Device IP")

    ## scroll config

    trv_scroll.config(command=trv.yview)

    device_list=get_device_list()
    update_rows(device_list)

    ## double click

    trv.bind('<Double 1>', get_device)

    device_list=get_device_list()
    update_rows(device_list)

    ### Search ########################################################################################

    searchvar=StringVar()

  
    search_entry=ttk.Entry(wrapper2, textvariable=searchvar)
    search_entry.pack(side=tk.LEFT, padx=6)

    search_button=Button(wrapper2, text="Search", command=search)
    search_button.pack(side=tk.LEFT, padx=6)

    clear_button=Button(wrapper2, text="Clear", command=clear)
    clear_button.pack(side=tk.LEFT, padx=6)

    ### Select ########################################################################################

    selectvar=StringVar()

    select_entry=ttk.Entry(wrapper3, textvariable=selectvar)
    select_entry.pack(side=tk.LEFT, padx=6)

    select_button=Button(wrapper3, text="Selection")
    select_button.pack(side=tk.LEFT, padx=6)

    list.mainloop()

#list_devices_gui()