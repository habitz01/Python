from tkinter import * # for UI
from tkinter import messagebox
from tkinter import ttk
from db.db_devices import *
from ios_scripts.sh_ip_int import *
from gui.create_devices_gui import *
from gui.list_devices_gui import *
from gui.crud_devices_gui import *
from ios_scripts.sh_run import *



def gui_wrapper():

    ####### Functions ###################################################################################

    def exit_app():
        exit_confirmation=messagebox.askquestion("Exit", "Exit Application?")

        if exit_confirmation=="yes":
            root.destroy()

    def clear():
        my_ip.set("")
        my_username.set("")
        my_password.set("")

    def get_device():
        device_ip=list_devices_gui()
        print("DeviceIP: ", device_ip)
        my_ip.set(device_ip)

    def sh_ip_int():
        clear_text()
        output_sh_ip_int=sh_ip_int_brief()
        command_text.insert(tk.END, output_sh_ip_int)

    def sh_running():
        clear_text()
        output_sh_run=show_run()
        command_text.insert(tk.END, output_sh_run)       
    
    def clear_text():
        command_text.delete(1.0, END)



    #####################################################################################################
    
    root=Tk()
    root.title("Networking GUI")
    root.iconbitmap('C:/Users/rh682g/Google Drive/github/Python/apps/networking/gui/net_ico.ico')

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
    commands_menu.add_command(label="Show Interface Status", command=sh_ip_int)


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

    ### Wrappers ########################################################################################

    wrapper1=LabelFrame(top_frame, text="Device / Authentication")
    wrapper2=LabelFrame(top_frame, text="Commands")
    wrapper3=LabelFrame(top_frame, text="Result")

    wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
    wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
    wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

    ### Labels ########################################################################################

    device_ip_label=Label(wrapper1, text="Device IP: ")
    device_ip_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)

    username_label=Label(wrapper1, text="Username: ")
    username_label.grid(row=1, column=0, sticky="e", padx=10, pady=10)

    password_label=Label(wrapper1, text="Password: ")
    password_label.grid(row=2, column=0, sticky="e", padx=10, pady=10)


    ### Entry ########################################################################################

    my_ip=StringVar()
    my_username=StringVar()
    my_password=StringVar()

    device_ip_entry=ttk.Entry(wrapper1, textvariable=my_ip)
    device_ip_entry.grid(row=0, column=1, padx=10, pady=10)
    device_ip_entry.config(justify="right")

    username_entry=ttk.Entry(wrapper1, textvariable=my_username)
    username_entry.grid(row=1, column=1, padx=10, pady=10)
    username_entry.config(justify="right")

    password_entry=ttk.Entry(wrapper1, textvariable=my_password)
    password_entry.grid(row=2, column=1, padx=10, pady=10)
    password_entry.config(show="?", justify="right")



    ### Buttons #######

    get_button=Button(wrapper1, text="Get Device", command=get_device)
    get_button.grid(row=0, column=2, sticky="e", padx=10, pady=10)

    clear_button=Button(wrapper1, text="Clear", command=clear)
    clear_button.grid(row=0, column=3, sticky="e", padx=10, pady=10)

    #### Command ##################################################################################


    ### Buttons #######

    command1_button=Button(wrapper2, text="Show Running Config", command=sh_running)
    command1_button.grid(row=1, column=0, sticky="e", padx=10, pady=10)

    command2_button=Button(wrapper2, text="Show IP Interface Brief", command=sh_ip_int)
    command2_button.grid(row=1, column=1, sticky="e", padx=10, pady=10)

    clear_text_button=Button(wrapper2, text="Clear Result", command=clear_text)
    clear_text_button.grid(row=1, column=2, sticky="e", padx=10, pady=10)



    #### Result ##################################################################################

     ## scroll

    command_scroll=Scrollbar(wrapper3)
    command_scroll.pack(side=RIGHT, fill=Y)

    ## Result Text

    command_text=Text(wrapper3, yscrollcommand=command_scroll.set, width=100, height=20)
    command_text.pack(expand=True, fill='both')
    #command_text.grid(row=1, column=1, padx=10, pady=10)

    ## scroll config

    command_scroll.config(command=command_text.yview)

    #clear_text_button=Button(wrapper3, text="Clear", command=clear_text)
    #clear_text_button.pack(side=RIGHT)
    #clear_text_button.grid(row=2, column=1, sticky="e", padx=10, pady=10)

    root.mainloop()

