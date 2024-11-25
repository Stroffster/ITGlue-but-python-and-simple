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
        
        #Control if file exists
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
    def Create_account(self, password, password_check, email, username):
        if password == password_check:
            pass
        else:
            pass
    
    #FIXME add code
    #Confirm action
    def Confirm_action(self):
        pass

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
            command=self.Login_check(password_entry, mail_username_entry)
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
        self.frame2 = tk.Frame(self.master, width=300, height=300)
        self.frame2.pack()
        self.reg_txt2 = ttk.Label(self.frame2, text='register')
        self.reg_txt2.pack()
        self.login_btn = ttk.Button(self.frame2, text="Go to Login", command=self.Login_menu)
        self.login_btn.pack()

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

root = tk.Tk()
root.resizable(False, False)
app_me = App(root)
root.mainloop()