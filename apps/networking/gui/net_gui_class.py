from tkinter import * # for UI
from tkinter import messagebox
from tkinter import ttk
from ios_scripts.sh_ip_int import *
from gui.create_devices_class import *
from gui.list_devices_class import *
from gui.crud_devices_class import *
from ios_scripts.sh_run import *



class main_gui_class:

    ####### Functions ###################################################################################

    ## Window functions

    def exit_app(self):
        self.exit_confirmation=messagebox.askquestion("Exit", "Exit Application?")

        if self.exit_confirmation=="yes":
            self.root.destroy()

    def clear(self):
        self.my_ip.set("")
        self.my_username.set("")
        self.my_password.set("")

    def clear_text(self):
        self.command_text.delete(1.0, END)

    ## DB functions
    
    def create_db(self):
        db_connection=sqlite3.connect("devices")
    
        db_cursor=db_connection.cursor()

        try:
            db_cursor.execute('''
                CREATE TABLE devices(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                hostname VARCHAR(50),
                ip VARCHAR(15))
                ''')
            messagebox.showinfo("DB", "DB successfully created")
        except:
            messagebox.showinfo("DB", "DB already exist")


    def get_device(self):
        list=tk.Toplevel()
        list.gui=list_devices_class(list)
        self.my_ip=list.gui.get_device_ip

    def create_devices(self):
        create=tk.Toplevel()
        create_gui=create_devices_class(create)

    def crud_devices_gui(self):
        crud=tk.Toplevel()
        crud.gui=crud_devices_class(crud)

        return

    ## Commands functions

    def sh_ip_int(self):
        self.clear_text()
        self.output_sh_ip_int=sh_ip_int_brief()
        self.command_text.insert(tk.END, self.output_sh_ip_int)

    def sh_running(self):
        self.clear_text()
        self.output_sh_run=show_run()
        self.command_text.insert(tk.END, self.output_sh_run)       
    

    ####### Constructor #############################################################################################


    def __init__(self, root):

        ####### Menu ########################################################################################

        self.root=root
        self.menu_bar=Menu(root)
        self.root.config(menu=self.menu_bar, width=1000,height=300)

        self.file_menu=Menu(self.menu_bar,tearoff=0)
        self.file_menu.add_command(label="Clear", command=self.clear)
        self.file_menu.add_command(label="Exit", command=self.exit_app)

        self.devices_menu=Menu(self.menu_bar,tearoff=0)
        self.devices_menu.add_command(label="Create Devices DB", command=self.create_db)
        self.devices_menu.add_command(label="Create Device", command=self.create_devices)
        self.devices_menu.add_command(label="CRUD Device", command=self.crud_devices_gui)

        self.commands_menu=Menu(self.menu_bar,tearoff=0)
        self.commands_menu.add_command(label="Show Running")
        self.commands_menu.add_command(label="Show Interface Status", command=self.sh_ip_int)


        self.help_menu=Menu(self.menu_bar,tearoff=0)
        self.help_menu.add_command(label="Documentation")
        self.help_menu.add_command(label="About")

        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.menu_bar.add_cascade(label="Devices", menu=self.devices_menu)
        self.menu_bar.add_cascade(label="Commands", menu=self.commands_menu)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)

        ####### Top Frame ########################################################################################

        self.top_frame=Frame(self.root)
        self.top_frame.pack()

        ### Wrappers ########################################################################################

        self.wrapper1=LabelFrame(self.top_frame, text="Device / Authentication")
        self.wrapper2=LabelFrame(self.top_frame, text="Commands")
        self.wrapper3=LabelFrame(self.top_frame, text="Result")

        self.wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
        self.wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
        self.wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

        ### Labels ########################################################################################

        self.device_ip_label=Label(self.wrapper1, text="Device IP: ")
        self.device_ip_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)

        self.username_label=Label(self.wrapper1, text="Username: ")
        self.username_label.grid(row=1, column=0, sticky="e", padx=10, pady=10)

        self.password_label=Label(self.wrapper1, text="Password: ")
        self.password_label.grid(row=2, column=0, sticky="e", padx=10, pady=10)


        ### Entry ########################################################################################

        self.my_ip=StringVar()
        self.my_username=StringVar()
        self.my_password=StringVar()

        self.device_ip_entry=ttk.Entry(self.wrapper1, textvariable=self.my_ip)
        self.device_ip_entry.grid(row=0, column=1, padx=10, pady=10)
        self.device_ip_entry.config(justify="right")

        self.username_entry=ttk.Entry(self.wrapper1, textvariable=self.my_username)
        self.username_entry.grid(row=1, column=1, padx=10, pady=10)
        self.username_entry.config(justify="right")

        self.password_entry=ttk.Entry(self.wrapper1, textvariable=self.my_password)
        self.password_entry.grid(row=2, column=1, padx=10, pady=10)
        self.password_entry.config(show="?", justify="right")



        ### Buttons #######

        self.get_button=Button(self.wrapper1, text="Get Device", command=self.get_device)
        self.get_button.grid(row=0, column=2, sticky="e", padx=10, pady=10)

        self.clear_button=Button(self.wrapper1, text="Clear", command=self.clear)
        self.clear_button.grid(row=0, column=3, sticky="e", padx=10, pady=10)

        #### Command ##################################################################################


        ### Buttons #######

        self.command1_button=Button(self.wrapper2, text="Show Running Config", command=self.sh_running)
        self.command1_button.grid(row=1, column=0, sticky="e", padx=10, pady=10)

        self.command2_button=Button(self.wrapper2, text="Show IP Interface Brief", command=self.sh_ip_int)
        self.command2_button.grid(row=1, column=1, sticky="e", padx=10, pady=10)

        self.clear_text_button=Button(self.wrapper2, text="Clear Result", command=self.clear_text)
        self.clear_text_button.grid(row=1, column=2, sticky="e", padx=10, pady=10)



        #### Result ##################################################################################

        ## scroll

        self.command_scroll=Scrollbar(self.wrapper3)
        self.command_scroll.pack(side=RIGHT, fill=Y)

        ## Result Text

        self.command_text=Text(self.wrapper3, yscrollcommand=self.command_scroll.set, width=100, height=20)
        self.command_text.pack(expand=True, fill='both')
        #command_text.grid(row=1, column=1, padx=10, pady=10)

        ## scroll config

        self.command_scroll.config(command=self.command_text.yview)

        #clear_text_button=Button(wrapper3, text="Clear", command=clear_text)
        #clear_text_button.pack(side=RIGHT)
        #clear_text_button.grid(row=2, column=1, sticky="e", padx=10, pady=10)

        self.root.mainloop()

