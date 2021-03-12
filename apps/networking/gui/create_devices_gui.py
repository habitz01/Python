from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from classes.device import *
import sqlite3 # for sqlite db support
import tkinter as tk
#from db.db_devices import *



def create_devices_gui():

    ####### Functions ###################################################################################

    def is_ipv4_address(ip): # Return True if ipv4 address, False if not
    
        octets = ip.split(".")

        if len(octets) != 4:
            return False
        elif any(not octet.isdigit() for octet in octets):
            return False
        elif any(int(octet) < 0 for octet in octets):
            return False
        elif any(int(octet) > 255 for octet in octets):
            return False

        return True

    def cancel():
        cancel_confirmation=messagebox.askquestion("Cancel", "Are you sure you want to cancel?")

        if cancel_confirmation=="yes":
            create.destroy()
    
    def accept():

        device_hostname=hostname_entry.get()
        device_ip=device_ip_entry.get()

        ip_validation=is_ipv4_address(device_ip)      

        if ip_validation==False:
            messagebox.showwarning("IP not valid","IP address not valid. Please try again")
        else:
            accept_confirmation=messagebox.askquestion("Accept", "Are you sure you want to create the device?")

            if accept_confirmation=="yes":

                new_device=device()
        
                new_device.set_hostname(device_hostname)
                new_device.set_ip(device_ip)

                # Use "device_create" function to create device on db
                device_create()

                create.destroy()
            
            else:
                create.destroy()
            
    def clear():
        print ("Clear")
        #device_ip.set("")
        device_ip_entry.delete(0,'end')
        #device_hostname.set("")
        hostname_entry.delete(0,'end')

    def device_create():
    
        db_connection=sqlite3.connect("devices")
    
        db_cursor=db_connection.cursor()

        try:
            db_cursor.execute(" INSERT INTO devices VALUES(NULL, '" + hostname_entry.get() + 
            "','" + device_ip_entry.get() + "')")

            db_connection.commit()

            messagebox.showinfo("DB", "Device successfully created")
        except:
            messagebox.showinfo("DB", "Device was not created")

    #####################################################################################################
    
    #create=Tk()
    create=tk.Toplevel()
    create.title("Create Device")
    create.attributes("-topmost", True)
    #create.iconbitmap("net_ico.ico")


    ####### Top Frame ########################################################################################

    top_frame=Frame(create)
    top_frame.pack()

    ### Labels ########################################################################################

    hostname_label=Label(top_frame, text="Hostname: ")
    hostname_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)

    device_ip_label=Label(top_frame, text="Device IP: ")
    device_ip_label.grid(row=1, column=0, sticky="e", padx=10, pady=10)

    ### Entry ########################################################################################

    #device_hostname=StringVar()
    #device_ip=StringVar()
  
    #hostname_entry=ttk.Entry(top_frame, textvariable=device_hostname)
    hostname_entry=ttk.Entry(top_frame)
    hostname_entry.grid(row=0, column=1, padx=10, pady=10)
    hostname_entry.config(justify="right")

    #device_ip_entry=ttk.Entry(top_frame, textvariable=device_ip)
    device_ip_entry=ttk.Entry(top_frame)
    device_ip_entry.grid(row=1, column=1, padx=10, pady=10)
    device_ip_entry.config(justify="right")


     ####### Bottom Frame ########################################################################################

    bottom_frame=Frame(create)
    bottom_frame.pack()

    ### Buttons ########################################################################################

    accept_button=Button(bottom_frame, text="Accept", command=accept)
    accept_button.grid(row=1, column=0, sticky="e", padx=10, pady=10)


    cancel_button=Button(bottom_frame, text="Cancel", command=cancel)
    cancel_button.grid(row=1, column=1, sticky="e", padx=10, pady=10)

    clear_button=Button(bottom_frame, text="Clear", command=clear)
    clear_button.grid(row=1, column=2, sticky="e", padx=10, pady=10)

    create.mainloop()