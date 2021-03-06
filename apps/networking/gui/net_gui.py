from tkinter import * # for UI
from tkinter import messagebox
from tkinter import ttk
from db.db_devices import *
from ios_scripts.sh_ip_int import *
from gui.create_devices_gui import *
from gui.list_devices_gui import *
from gui.crud_devices_gui import *



def gui():

    ####### Functions ###################################################################################

    def exit_app():
        exit_confirmation=messagebox.askquestion("Exit", "Exit Application?")

        if exit_confirmation=="yes":
            root.destroy()

    def clear():
        my_ip.set("")
        my_username.set("")
        name.delete(0,'end')
        my_password.set("")
        command_text.delete(1.0, END)

    def get_device():
        device_ip=list_devices_gui()
        print("DeviceIP: ", device_ip)
        my_ip.set(device_ip)


    #####################################################################################################
    
    root=Tk()
    root.title("Networking GUI")
    #root.iconbitmap("net_ico.ico")

    ####### Menu ########################################################################################

    menu_bar=Menu(root)
    root.config(menu=menu_bar, width=1000,height=300)

    file_menu=Menu(menu_bar,tearoff=0)
    file_menu.add_command(label="Clear", command=clear)
    file_menu.add_command(label="Exit", command=exit_app)

    devices_menu=Menu(menu_bar,tearoff=0)
    devices_menu.add_command(label="Create Devices DB", command=db_create)
    devices_menu.add_command(label="Create Device", command=create_devices_gui)
    devices_menu.add_command(label="CRUD Device", command=crud_devices_gui)

    commands_menu=Menu(menu_bar,tearoff=0)
    commands_menu.add_command(label="Show Running")
    commands_menu.add_command(label="Show Interface Status", command=sh_int_status)


    help_menu=Menu(menu_bar,tearoff=0)
    help_menu.add_command(label="Documentation")
    help_menu.add_command(label="About")

    menu_bar.add_cascade(label="File", menu=file_menu)
    menu_bar.add_cascade(label="Devices", menu=devices_menu)
    menu_bar.add_cascade(label="Commands", menu=commands_menu)
    menu_bar.add_cascade(label="Help", menu=help_menu)

    ####### Top Frame ########################################################################################

    top_frame=Frame(root)
    top_frame.pack()

    ### Labels ########################################################################################

    device_ip_label=Label(top_frame, text="Device IP: ")
    device_ip_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)

    username_label=Label(top_frame, text="Username: ")
    username_label.grid(row=1, column=0, sticky="e", padx=10, pady=10)

    password_label=Label(top_frame, text="Password: ")
    password_label.grid(row=2, column=0, sticky="e", padx=10, pady=10)


    ### Entry ########################################################################################

    my_ip=StringVar()
    my_username=StringVar()
    my_password=StringVar()

    device_ip_entry=ttk.Entry(top_frame, textvariable=my_ip)
    device_ip_entry.grid(row=0, column=1, padx=10, pady=10)
    device_ip_entry.config(justify="right")

    username_entry=ttk.Entry(top_frame, textvariable=my_username)
    username_entry.grid(row=1, column=1, padx=10, pady=10)
    username_entry.config(justify="right")

    password_entry=ttk.Entry(top_frame, textvariable=my_password)
    password_entry.grid(row=2, column=1, padx=10, pady=10)
    password_entry.config(show="?", justify="right")



    ### Buttons ########################################################################################

    get_button=Button(top_frame, text="Get Device", command=get_device)
    get_button.grid(row=0, column=2, sticky="e", padx=10, pady=10)


    ####### Middle Frame ########################################################################################

    middle_frame=Frame(root)
    middle_frame.pack()

    ## Command Text

    command_label=Label(middle_frame, text="Command List: ")
    command_label.grid(row=3, column=0, sticky="e", padx=10, pady=10)

    command_text=Text(middle_frame, width=20, height=5)
    command_text.grid(row=3, column=1, padx=10, pady=10)

    command_scroll=Scrollbar(middle_frame, command=command_text.yview)
    command_scroll.grid(row=3, column=2, sticky="nsew")

    #command_scroll=ttk.Scrollbar(top_frame, orient=VERTICAL, command=listbox.yview)
    #listbox.configure(yscrollcommand=s.set)

    command_text.config(yscrollcommand=command_scroll)


    ####### Bottom Frame ########################################################################################

    bottom_frame=Frame(root)
    bottom_frame.pack()

    ### Buttons ########################################################################################

    command1_button=Button(bottom_frame, text="Show Run")
    command1_button.grid(row=1, column=0, sticky="e", padx=10, pady=10)

    command2_button=Button(bottom_frame, text="Show Int Status")
    command2_button.grid(row=1, column=1, sticky="e", padx=10, pady=10)

    clear_button=Button(bottom_frame, text="Clear", command=clear)
    clear_button.grid(row=1, column=2, sticky="e", padx=10, pady=10)

    root.mainloop()

