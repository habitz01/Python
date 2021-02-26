from tkinter import * # for UI
from tkinter import messagebox
from classes.device import *
from db.db_devices import *



def create_devices_gui():

    ####### Functions ###################################################################################

    def cancel():
        cancel_confirmation=messagebox.askquestion("Cancel", "Are you sure you want to cancel?")

        if cancel_confirmation=="yes":
            root.destroy()
    
    def accept():

        print ("Hostname: ", hostname.get(), "IP: ", ip.get())
        accept_confirmation=messagebox.askquestion("Accept", "Are you sure you want to create the device?")

        if accept_confirmation=="yes":
            print("Hostname: ", hostname.get(), "\nIP: ", ip.get())

            new_device=device()
        
            new_device.set_hostname=hostname.get()
            new_device.set_ip=ip.get()

            new_device.device_info()

            root.destroy()
        else:
            root.destroy()
            



    #####################################################################################################
    
    root=Tk()
    root.title("Create Device")
    #root.iconbitmap("net_ico.ico")


    ####### Top Frame ########################################################################################

    top_frame=Frame(root)
    top_frame.pack()

    ### Labels ########################################################################################

    hostname_label=Label(top_frame, text="Hostname: ")
    hostname_label.grid(row=1, column=0, sticky="e", padx=10, pady=10)

    device_ip_label=Label(top_frame, text="Device IP: ")
    device_ip_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)

    ### Entry ########################################################################################

    hostname=StringVar()
    ip=StringVar()
  

    device_ip_entry=Entry(top_frame, textvariable=ip)
    device_ip_entry.grid(row=0, column=1, padx=10, pady=10)
    device_ip_entry.config(justify="right")

    username_entry=Entry(top_frame, textvariable=hostname)
    username_entry.grid(row=1, column=1, padx=10, pady=10)
    username_entry.config(justify="right")

     ####### Bottom Frame ########################################################################################

    bottom_frame=Frame(root)
    bottom_frame.pack()

    ### Buttons ########################################################################################

 #   accept_button=Button(bottom_frame, text="Accept")
    #print ("Hostname: ", hostname.get(), "IP: ", ip.get())
    accept_button=Button(bottom_frame, text="Accept", command=accept)
    accept_button.grid(row=1, column=0, sticky="e", padx=10, pady=10)


    cancel_button=Button(bottom_frame, text="Cancel", command=cancel)
    cancel_button.grid(row=1, column=2, sticky="e", padx=10, pady=10)

    root.mainloop()

#create_devices_gui()