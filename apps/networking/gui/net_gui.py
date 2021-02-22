
from tkinter import * # for UI
from tkinter import messagebox
from db.db_devices import *
from ios_scripts.sh_ip_int import *



def gui():

    ####### Functions ###################################################################################

    def exit_app():
        exit_confirmation=messagebox.askquestion("Exit", "Exit Application?")

        if exit_confirmation=="yes":
            root.destroy()

    def clear():
        my_ip.set("")
        my_username.set("")
        my_password.set("")
        command_text.delete(1.0, END)

    #####################################################################################################
    
    root=Tk()
    root.title("Networking GUI")
    #root.iconbitmap("net_ico.ico")

    ####### Menu ########################################################################################

    menu_bar=Menu(root)
    root.config(menu=menu_bar, width=300,height=300)

    file_menu=Menu(menu_bar,tearoff=0)
    file_menu.add_command(label="Clear", command=clear)
    file_menu.add_command(label="Exit", command=exit_app)

    devices_menu=Menu(menu_bar,tearoff=0)
    devices_menu.add_command(label="Create Devices DB", command=db_create)
    devices_menu.add_command(label="Create Device")
    devices_menu.add_command(label="List Device")

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

    command_label=Label(top_frame, text="Command List: ")
    command_label.grid(row=3, column=0, sticky="e", padx=10, pady=10)

    ### Entry ########################################################################################

    my_ip=StringVar()
    my_username=StringVar()
    my_password=StringVar()

    device_ip_entry=Entry(top_frame, textvariable=my_ip)
    device_ip_entry.grid(row=0, column=1, padx=10, pady=10)
    device_ip_entry.config(justify="right")

    username_entry=Entry(top_frame, textvariable=my_username)
    username_entry.grid(row=1, column=1, padx=10, pady=10)
    username_entry.config(justify="right")

    password_entry=Entry(top_frame, textvariable=my_password)
    password_entry.grid(row=2, column=1, padx=10, pady=10)
    password_entry.config(show="?", justify="right")

    command_text=Text(top_frame, width=20, height=5)
    command_text.grid(row=3, column=1, padx=10, pady=10)

    command_scroll=Scrollbar(top_frame, command=command_text.yview)
    command_scroll.grid(row=3, column=2, sticky="nsew")

    command_text.config(yscrollcommand=command_scroll)

    ####### Bottom Frame ########################################################################################

    bottom_frame=Frame(root)
    bottom_frame.pack()

    ### Buttons ########################################################################################

    command1_button=Button(bottom_frame, text="Show Run")
    command1_button.grid(row=1, column=0, sticky="e", padx=10, pady=10)

    command2_button=Button(bottom_frame, text="Show Int Status")
    command2_button.grid(row=1, column=2, sticky="e", padx=10, pady=10)

    root.mainloop()