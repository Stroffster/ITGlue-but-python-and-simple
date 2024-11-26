import os
import sys
import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x350")
        self.master.configure(bg="#ffffff")
        self.master.title("AssetManager")
        self.Login_menu()

    #Load assets so the program can use them
    def Load_asset(self, path):
        base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        assets = os.path.join(base, "assets")
        full_path = os.path.join(assets, path)
        
        #DEBUG Control if file exists
        if not os.path.exists(full_path):
            print(f"Fel: Filen {full_path} finns inte!")
        return full_path
    
    #FIXME add code
    #Check login details
    def Login_check(self, password, user):
        print(password, user)
        return

    #FIXME add code
    #Create account
    def Create_account(self, password, password_confirm, email, username):
        if password == password_confirm:
            pass
        else:
            pass
    
    #FIXME add code
    #Confirm action
    def Confirm_action(self):
        # Create the popup window
        popup = tk.Tk()
        popup.title("Confirm Choice")
        popup.geometry("250x70")
        center_window(popup)

        # Create a label
        Confirm_action_label = tk.Label(popup, text="Enter admin password to make an account")
        Confirm_action_label.pack()

        # Create an entry field
        Confirm_action_entry = tk.Entry(popup)
        Confirm_action_entry.pack()

        # Create a confirm button
        confirm_button = tk.Button(popup, text="Confirm", command= lambda: self.Login_check(Confirm_action_entry.get(), "Admin"))
        confirm_button.pack()

    #Menus/screens

        #Login screen
    def Login_menu(self):
        for i in self.master.winfo_children():
            i.destroy()

        #Ladda bilder och håll en referens
        self.computers_image = tk.PhotoImage(file=self.Load_asset("computers.png"))
        self.login_button_img = tk.PhotoImage(file=self.Load_asset("login_button.png"))
        self.account_button_img = tk.PhotoImage(file=self.Load_asset("account_button.png"))

        canvas = tk.Canvas(
            self.master,
            bg="#ffffff",
            width=500,
            height=350,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        #Make an image
        canvas.create_image(100, 175, image=self.computers_image)

        #Make an image and add a background to it
        canvas.create_rectangle(200, 0, 500, 350, fill='#5a5a5a', outline="")
        canvas.create_text(
            259,
            20,
            anchor="nw",
            text="AssetManager",
            fill="#f5f5f5",
            font=("Istok Web", 24 * -1)
        )

        #Make an entry feirld
        mail_username_entry = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            fg="#000000",
            insertbackground="#000000",
            highlightthickness=0
        )
        mail_username_entry.place(x=230, y=110, width=230, height=30)

        password_entry = tk.Entry(
            show="*",
            bd=0,
            bg="#d9d9d9",
            fg="#000000",
            insertbackground="#000000",
            highlightthickness=0
        )
        password_entry.place(x=230, y=175, width=230, height=30)

        canvas.create_text(
            230,
            155,
            anchor="nw",
            text="Password",
            fill="#ffffff",
            font=("Istok Web", 14 * -1)
        )

        canvas.create_text(
            231,
            85,
            anchor="nw",
            text="Username/Email",
            fill="#ffffff",
            font=("Istok Web", 14 * -1)
        )

        
        login_button = tk.Button(
            image=self.login_button_img,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command= lambda: self.Login_check(password_entry.get(), mail_username_entry.get())
            )
        
        login_button.place(x=275, y=212, width=140, height=37)

        account_button = tk.Button(
            image=self.account_button_img,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=self.Account_creation
        )
        account_button.place(x=287, y=252, width=115, height=30)

        #Account creation screen
    def Account_creation(self):
        for i in self.master.winfo_children():
            i.destroy()

        #Ladda bilder och håll en referens
        self.computers_image = tk.PhotoImage(file=self.Load_asset("computers.png"))
        self.create_button_img = tk.PhotoImage(file=self.Load_asset("create_button.png"))

        canvas = tk.Canvas(
            root,
            bg = "#ffffff",
            width = 500,
            height = 350,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x=0, y=0)

        canvas.create_image(100, 175, image=self.computers_image)

        canvas.create_rectangle(200, 0, 500, 350, fill='#5a5a5a', outline="")

        canvas.create_text(
            259,
            20,
            anchor="nw",
            text="AssetManager",
            fill="#f5f5f5",
            font=("Istok Web", 24 * -1)
        )

        textbox_1 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            fg="#000000",
            insertbackground="#000000",
            highlightthickness=0
        )

        textbox_1.place(x=230, y=147, width=230, height=30)

        password_confirm = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            fg="#000000",
            insertbackground="#000000",
            highlightthickness=0
        )

        password_confirm.place(x=230, y=90, width=230, height=30)

        canvas.create_text(
            230,
            127,
            anchor="nw",
            text="Email",
            fill="#ffffff",
            font=("Istok Web", 14 * -1)
        )

        canvas.create_text(
            230,
            70,
            anchor="nw",
            text="Username",
            fill="#ffffff",
            font=("Istok Web", 14 * -1)
        )

        button_1 = tk.Button(
            image=self.create_button_img,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.Create_account(password, password_confirm, email, username) #FIXME
        )

        button_1.place(x=275, y=302, width=140, height=37)

        canvas.create_text(
            275,
            301,
            anchor="nw",
            text="",
            fill="#000000",
            font=("Default Font", 12 * -1)
        )

        textbox_3 = tk.Entry(
            show="*",
            bd=0,
            bg="#d9d9d9",
            fg="#000000",
            insertbackground="#000000",
            highlightthickness=0
        )

        textbox_3.place(x=230, y=203, width=230, height=30)

        canvas.create_text(
            230,
            183,
            anchor="nw",
            text="Password",
            fill="#ffffff",
            font=("Istok Web", 14 * -1)
        )

        canvas.create_text(
            230,
            240,
            anchor="nw",
            text="Confirm Password",
            fill="#ffffff",
            font=("Istok Web", 14 * -1)
        )

        textbox_4 = tk.Entry(
            show="*",
            bd=0,
            bg="#d9d9d9",
            fg="#000000",
            insertbackground="#000000",
            highlightthickness=0
        )

        textbox_4.place(x=230, y=260, width=230, height=30)

        #Main menu screen
    def Main_menu(self):
        for i in self.master.winfo_children():
            i.destroy()

        #Show assets screen
    def Show_assets(self):
        for i in self.master.winfo_children():
            i.destroy()

        #Edit asset screen
    def Edit_asset(self):
        for i in self.master.winfo_children():
            i.destroy()

        #Add asset screen
    def Add_asset(self):
        for i in self.master.winfo_children():
            i.destroy()

#Center the window to the center of the screen
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

root = tk.Tk()
root.resizable(False, False)
app_me = App(root)
center_window(root)
root.mainloop()