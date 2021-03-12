from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from classes.device import *
import sqlite3 # for sqlite db support
import tkinter as tk
#from db.db_devices import *



class create_devices_class:

    ####### Functions ###################################################################################

    def is_ipv4_address(self, ip): # Return True if ipv4 address, False if not
    
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

    def cancel(self):
        cancel_confirmation=messagebox.askquestion("Cancel", "Are you sure you want to cancel?")

        if cancel_confirmation=="yes":
            create.destroy()
    
    def accept(self):

        #device_hostname=hostname_entry.get()
        #device_ip=device_ip_entry.get()

        self.ip_validation=self.is_ipv4_address(self.device_ip.get())      

        if self.ip_validation==False:
            messagebox.showwarning("IP not valid","IP address not valid. Please try again")
        else:
            self.accept_confirmation=messagebox.askquestion("Accept", "Are you sure you want to create the device?")

            if self.accept_confirmation=="yes":

                self.new_device=device()
        
                #self.new_device.set_hostname(self.device_hostname)
                #self.new_device.set_ip(self.device_ip)

                # Use "device_create" function to create device on db
                self.device_create()

                self.create.destroy()
            
            else:
                self.create.destroy()
            
    def clear(self):
        #print ("Clear")
        self.device_ip.set("")
        #device_ip_entry.delete(0,'end')
        self.device_hostname.set("")
        #hostname_entry.delete(0,'end')

    def device_create(self):
    
        db_connection=sqlite3.connect("devices")
    
        db_cursor=db_connection.cursor()

        try:
            db_cursor.execute(" INSERT INTO devices VALUES(NULL, '" + self.device_hostname.get() + 
            "','" + self.device_ip.get() + "')")

            #db_cursor.execute(" INSERT INTO devices VALUES(NULL, '" + self.hostname_entry.get() + 
            #"','" + self.device_ip_entry.get() + "')")

            db_connection.commit()

            messagebox.showinfo("DB", "Device successfully created")
        except:
            messagebox.showinfo("DB", "Device was not created")

    #####################################################################################################
    ####### Constructor #############################################################################################


    def __init__(self, create):

        #create=Tk()
        #self.create=tk.Toplevel(self)
        self.create=create
        self.create.title("Create Device")
        self.create.attributes("-topmost", True)
        #create.iconbitmap("net_ico.ico")


        ####### Top Frame ########################################################################################

        self.top_frame=Frame(self.create)
        self.top_frame.pack()

        ### Labels ########################################################################################

        self.hostname_label=Label(self.top_frame, text="Hostname: ")
        self.hostname_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)

        self.device_ip_label=Label(self.top_frame, text="Device IP: ")
        self.device_ip_label.grid(row=1, column=0, sticky="e", padx=10, pady=10)

        ### Entry ########################################################################################

        self.device_hostname=StringVar()
        self.device_ip=StringVar()
  
        self.hostname_entry=ttk.Entry(self.top_frame, textvariable=self.device_hostname)
        #self.hostname_entry=ttk.Entry(self.top_frame)
        self.hostname_entry.grid(row=0, column=1, padx=10, pady=10)
        self.hostname_entry.config(justify="right")

        self.device_ip_entry=ttk.Entry(self.top_frame, textvariable=self.device_ip)
        #self.device_ip_entry=ttk.Entry(self.top_frame)
        self.device_ip_entry.grid(row=1, column=1, padx=10, pady=10)
        self.device_ip_entry.config(justify="right")


        ####### Bottom Frame ########################################################################################

        self.bottom_frame=Frame(self.create)
        self.bottom_frame.pack()

        ### Buttons ########################################################################################

        self.accept_button=Button(self.bottom_frame, text="Accept", command=self.accept)
        self.accept_button.grid(row=1, column=0, sticky="e", padx=10, pady=10)


        self.cancel_button=Button(self.bottom_frame, text="Cancel", command=self.cancel)
        self.cancel_button.grid(row=1, column=1, sticky="e", padx=10, pady=10)

        self.clear_button=Button(self.bottom_frame, text="Clear", command=self.clear)
        self.clear_button.grid(row=1, column=2, sticky="e", padx=10, pady=10)

        self.create.mainloop()