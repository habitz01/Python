from tkinter import *
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

        device_hostname.set("test")
        device_ip.set("192.168.1.1")


        print ("Hostname: ", device_hostname.get(), "IP: ", device_ip.get())
        accept_confirmation=messagebox.askquestion("Accept", "Are you sure you want to create the device?")

        if accept_confirmation=="yes":
            print("Hostname: ", device_hostname.get(), "\nIP: ", device_ip.get())

            new_device=device()
        
            new_device.set_hostname(device_hostname.get())
            new_device.set_ip(device_ip.get())

            new_device.device_info()


            messagebox.showinfo("Create Device", "Device created successfully")
            root.destroy()

            
        else:
            root.destroy()
            
    def clear():
        print ("Clear")
        device_ip.set("")
        device_hostname.set("")

    #####################################################################################################
    
    root=Tk()
    root.title("Create Device")
    root.attributes("-topmost", True)
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

    device_hostname=StringVar()
    device_ip=StringVar()
  

    device_ip_entry=Entry(top_frame, textvariable=device_ip)
    device_ip_entry.grid(row=0, column=1, padx=10, pady=10)
    device_ip_entry.config(justify="right")

    hostname_entry=Entry(top_frame, textvariable=device_hostname)
    hostname_entry.grid(row=1, column=1, padx=10, pady=10)
    hostname_entry.config(justify="right")


     ####### Bottom Frame ########################################################################################

    bottom_frame=Frame(root)
    bottom_frame.pack()

    ### Buttons ########################################################################################

    accept_button=Button(bottom_frame, text="Accept", command=accept)
    accept_button.grid(row=1, column=0, sticky="e", padx=10, pady=10)


    cancel_button=Button(bottom_frame, text="Cancel", command=cancel)
    cancel_button.grid(row=1, column=1, sticky="e", padx=10, pady=10)

    clear_button=Button(bottom_frame, text="Clear", command=clear)
    clear_button.grid(row=1, column=2, sticky="e", padx=10, pady=10)

    root.mainloop()