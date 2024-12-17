import os
import sys
import tkinter as tk #Importing the GUI libary
import asyncio #Import sync libary
import asyncpg #Database connection thingy ma jig
import hashlib #Impoting encryption libary

from tkinter import ttk
from tkinter import messagebox
from asyncpg.pool import create_pool #Import the database connection function

from Apikeys import DB #Get the database class with login information

# Make a placeholder text for a text area
class TkForge_Entry(tk.Entry):
    def __init__(self, master=None, placeholder="Enter text", placeholder_fg='grey', **kwargs):
        super().__init__(master, **kwargs)
        
        self.p, self.p_fg, self.fg = placeholder, placeholder_fg, self.cget("fg")
        self.putp()
        self.bind("<FocusIn>", self.toggle)
        self.bind("<FocusOut>", self.toggle)

    def putp(self):
        self.delete(0, tk.END)
        self.insert(0, self.p)
        self.config(fg=self.p_fg)
        self.p_a = True

    def toggle(self, event):
        if self.p_a:
            self.delete(0, tk.END)
            self.config(fg=self.fg)
            self.p_a = False
        elif not self.get(): self.putp()

    def get(self): return '' if self.p_a else super().get()

    def is_placeholder(self, b):
        self.p_a = b
        self.config(fg=self.p_fg if b == True else self.fg)

    def get_placeholder(self): return self.p

# Make a placeholder text for a text area
class TkForge_Textarea(tk.Text):
    def __init__(self, master=None, placeholder="Enter text", placeholder_fg='grey', **kwargs):
        super().__init__(master, **kwargs)
        
        self.p, self.p_fg, self.fg = placeholder, placeholder_fg, self.cget("fg")
        self.putp()
        self.bind("<FocusIn>", self.toggle)
        self.bind("<FocusOut>", self.toggle)

    def putp(self):
        self.delete('1.0', tk.END)
        self.insert('1.0', self.p)
        self.config(fg=self.p_fg)
        self.p_a = True

    def toggle(self, event):
        if self.p_a:
            self.delete('1.0', tk.END)
            self.config(fg=self.fg)
            self.p_a = False
        elif self.get('1.0', tk.END).replace(' ', '').replace('\n', '') == '': self.putp()

    def get(self, i1='1.0', i2=tk.END): return '' if self.p_a else super().get(i1, i2)

    def is_placeholder(self, b):
        self.p_a = b
        self.config(fg=self.p_fg if b == True else self.fg)

    def get_placeholder(self): return self.p

class App:
    async def __init__(self, master):
        self.master = master
        self.master.geometry("500x350")
        self.master.configure(bg="#ffffff")
        self.master.title("AssetManager")
        #self.Login_menu()
        self.Main_menu() #DEBUG

    #Load assets so the program can use them
    def Load_asset(self, path):
        base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        assets = os.path.join(base, "assets")
        full_path = os.path.join(assets, path)
        
        #DEBUG Control if file exists
        if not os.path.exists(full_path):
            print(f"Fel: Filen {full_path} finns inte!")
        return full_path
    
    #FIXME add login to DB check
    #Check login details
    def Login_check(self, password, user):
        print(password, user)
        if password in ["admin", "Admin"] and password.lower() == user.lower(): #DEBUG make a DB check
            print("accepted")
            self.Main_menu()
        else:
            messagebox.showerror("Error", "Login details doesn't match!") 
        return

    #FIXME add real code
    #Create account
    def Create_account(self, Password, Password_confirm, Email, Username):
        if any(char.isspace() for char in [Password, Email, Username]):
            messagebox.showerror("Error", "Spaces are not allowed in password, email, or username")
        elif Password != Password_confirm:
            messagebox.showerror("Error", "Passwords don't match")
        else:
            confirmation = self.Confirm_admin_action()
            if confirmation:
                print(f"password: {Password}, password confirm: {Password_confirm}, email: {Email}, username: {Username}")
                self.Main_menu()  # Access main menu after successful account creation


    def Confirm_admin_action(self):
        popup = tk.Toplevel(self.master)  # Create a child window for confirmation
        popup.title("Confirm Choice")
        popup.geometry("250x105")
        center_window(popup)

        Confirm_admin_action_label = tk.Label(popup, text="Enter admin password to make an account")
        Confirm_admin_action_label.pack()

        Confirm_admin_action_entry = tk.Entry(popup, show="*")  # Hide password characters
        Confirm_admin_action_entry.pack()
        
        # Check login
        def admin_login_check():
            password = Confirm_admin_action_entry.get()

            if password.lower() == "admin": #DEBUG add DB thingy
                popup.destroy()
                print("yay!")
            else:
                messagebox.showerror("Error", "Login details don't match!")
        
        confirm_button = tk.Button(popup, text="Confirm", command=admin_login_check)
        confirm_button.pack(pady=5)

        Cancel_button = tk.Button(popup, text="Cancel", command=lambda: popup.destroy())
        Cancel_button.pack()
          
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

        Email_entry = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            fg="#000000",
            insertbackground="#000000",
            highlightthickness=0
        )

        Email_entry.place(x=230, y=147, width=230, height=30)

        Username_entry = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            fg="#000000",
            insertbackground="#000000",
            highlightthickness=0
        )

        Username_entry.place(x=230, y=90, width=230, height=30)

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

        Create_account_button = tk.Button(
            image=self.create_button_img,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.Create_account(Password_entry.get(), Password_confirm_entry.get(), Email_entry.get(), Username_entry.get()) #FIXME
        )

        Create_account_button.place(x=275, y=302, width=140, height=37)

        canvas.create_text(
            275,
            301,
            anchor="nw",
            text="",
            fill="#000000",
            font=("Default Font", 12 * -1)
        )

        Password_entry = tk.Entry(
            show="*",
            bd=0,
            bg="#d9d9d9",
            fg="#000000",
            insertbackground="#000000",
            highlightthickness=0
        )

        Password_entry.place(x=230, y=203, width=230, height=30)

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

        Password_confirm_entry = tk.Entry(
            show="*",
            bd=0,
            bg="#d9d9d9",
            fg="#000000",
            insertbackground="#000000",
            highlightthickness=0
        )

        Password_confirm_entry.place(x=230, y=260, width=230, height=30)

        #Main menu screen
    def Main_menu(self):
        for i in self.master.winfo_children():
            i.destroy()

        #Ladda bilder och håll en referens
        self.computers_image = tk.PhotoImage(file=self.Load_asset("computers.png"))
        self.add_button_img = tk.PhotoImage(file=self.Load_asset("add_button.png"))
        self.show_button_img = tk.PhotoImage(file=self.Load_asset("show_button.png"))

        canvas = tk.Canvas(
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

        button_1 = tk.Button(
            image=self.add_button_img,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=self.Add_asset
        )

        button_1.place(x=245, y=140, width=185, height=38)

        canvas.create_text(
            244,
            137,
            anchor="nw",
            text="",
            fill="#000000",
            font=("Default Font", 12 * -1)
        )

        button_2 = tk.Button(
            image=self.show_button_img,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command= self.Show_assets
        )

        button_2.place(x=245, y=178, width=185, height=38)

        canvas.create_text(
            245,
            178,
            anchor="nw",
            text="",
            fill="#000000",
            font=("Default Font", 12 * -1)
        )

        #Show assets screen
    def Show_assets(self):
        for i in self.master.winfo_children():
            i.destroy()

        #Ladda bilder och håll en referens
        self.edit_button_img = tk.PhotoImage(file=self.Load_asset("edit_button.png"))
        self.back_button_img = tk.PhotoImage(file=self.Load_asset("back_button.png"))

        canvas = tk.Canvas(
            bg = "#ffffff",
            width = 500,
            height = 350,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x=0, y=0)

        canvas.create_rectangle(0, 0, 500, 350, fill='#5a5a5a', outline="")

        canvas.create_text(
            164,
            18,
            anchor="nw",
            text="AssetManager",
            fill="#f5f5f5",
            font=("Istok Web", 24 * -1)
        )

        button_1 = tk.Button(
            image=self.edit_button_img,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=self.Edit_asset
        )

        button_1.place(x=158, y=312, width=185, height=38)

        canvas.create_text(
            158,
            312,
            anchor="nw",
            text="",
            fill="#000000",
            font=("Default Font", 12 * -1)
        )

        button_2 = tk.Button(
            image=self.back_button_img,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=self.Main_menu
        )

        button_2.place(x=1, y=0, width=99, height=29)

        canvas.create_text(
            1,
            0,
            anchor="nw",
            text="",
            fill="#000000",
            font=("Default Font", 12 * -1)
        )

        listbox_1 = tk.Listbox(width=32, height=16)

        # Creating a Scrollbar and  
        # attaching it to root window 
        scrollbar_1 = tk.Scrollbar()
        scrollbar_1.place(x=345, y=55, height=259)

        listbox_1.config(yscrollcommand = scrollbar_1.set)

        scrollbar_1.config(command = listbox_1.yview) 

        for i in range(100):
            listbox_1.insert(tk.END, f"Item {i}")

        listbox_1.place(x=150, y=55)

        #Edit asset screen #FIXME
    def Edit_asset(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.edit_button_img = tk.PhotoImage(file=self.Load_asset("edit_button.png"))
        self.back_button_img = tk.PhotoImage(file=self.Load_asset("back_button.png"))

        canvas = tk.Canvas(
            bg = "#ffffff",
            width = 500,
            height = 350,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x=0, y=0)

        canvas.create_rectangle(0, 0, 500, 350, fill='#5a5a5a', outline="")

        canvas.create_text(
            164,
            18,
            anchor="nw",
            text="AssetManager",
            fill="#f5f5f5",
            font=("Istok Web", 24 * -1)
        )

        button_1 = tk.Button(
            image=self.edit_button_img,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 has been pressed!") #FIXME
        )

        button_1.place(x=158, y=312, width=185, height=38)

        canvas.create_text(
            158,
            312,
            anchor="nw",
            text="",
            fill="#000000",
            font=("Default Font", 12 * -1)
        )

        button_2 = tk.Button(
            image=self.back_button_img,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=self.Show_assets
        )

        button_2.place(x=1, y=0, width=99, height=29)

        canvas.create_text(
            1,
            0,
            anchor="nw",
            text="",
            fill="#000000",
            font=("Default Font", 12 * -1)
        )

        textbox_1 = TkForge_Entry(
            bd=0,
            bg="#d9d9d9",
            fg="#ffffff",
            placeholder="#FIXME",
            insertbackground="#ffffff",
            highlightthickness=0
        )

        textbox_1.place(x=256, y=77, width=180, height=25)

        textbox_2 = TkForge_Entry(
            bd=0,
            bg="#d9d9d9",
            fg="#ffffff",
            placeholder="#FIXME",
            insertbackground="#ffffff",
            highlightthickness=0
        )

        textbox_2.place(x=66, y=77, width=180, height=25)

        textarea_1 = TkForge_Textarea(
            bd=0,
            bg="#d9d9d9",
            fg="#ffffff",
            placeholder="#FIXME",
            insertbackground="#ffffff",
            highlightthickness=0
        )

        textarea_1.place(x=256, y=173, width=180, height=127)

        textbox_3 = TkForge_Entry(
            bd=0,
            bg="#d9d9d9",
            fg="#ffffff",
            placeholder="#FIXME",
            insertbackground="#ffffff",
            highlightthickness=0
        )

        textbox_3.place(x=66, y=125, width=180, height=25)

        textbox_4 = TkForge_Entry(
            bd=0,
            bg="#d9d9d9",
            fg="#ffffff",
            placeholder="#FIXME",
            insertbackground="#ffffff",
            highlightthickness=0
        )

        textbox_4.place(x=256, y=125, width=180, height=25)

        textbox_5 = TkForge_Entry(
            bd=0,
            bg="#d9d9d9",
            fg="#ffffff",
            placeholder="#FIXME",
            insertbackground="#ffffff",
            highlightthickness=0
        )

        textbox_5.place(x=66, y=173, width=180, height=25)

        textbox_6 = TkForge_Entry(
            bd=0,
            bg="#d9d9d9",
            fg="#ffffff",
            placeholder="#FIXME",
            insertbackground="#ffffff",
            highlightthickness=0
        )

        textbox_6.place(x=67, y=274, width=180, height=25)

        textbox_7 = TkForge_Entry(
            bd=0,
            bg="#d9d9d9",
            fg="#ffffff",
            placeholder="#FIXME",
            insertbackground="#ffffff",
            highlightthickness=0
        )

        textbox_7.place(x=67, y=223, width=180, height=25)

        canvas.create_text(
            116,
            102,
            anchor="nw",
            text="Service Tag",
            fill="#ffffff",
            font=("Istok Web", 14 * -1)
        )

        canvas.create_text(
            288,
            102,
            anchor="nw",
            text="End Of Warranty",
            fill="#ffffff",
            font=("Istok Web", 14 * -1)
        )

        canvas.create_text(
            107,
            150,
            anchor="nw",
            text="Purchase Date",
            fill="#ffffff",
            font=("Istok Web", 14 * -1)
        )

        canvas.create_text(
            326,
            150,
            anchor="nw",
            text="Notes",
            fill="#ffffff",
            font=("Istok Web", 14 * -1)
        )

        canvas.create_text(
            104,
            248,
            anchor="nw",
            text="Location/Office",
            fill="#ffffff",
            font=("Istok Web", 14 * -1)
        )

        canvas.create_text(
            111,
            196,
            anchor="nw",
            text="Model Name",
            fill="#ffffff",
            font=("Istok Web", 14 * -1)
        )

        canvas.create_text(
            116,
            51,
            anchor="nw",
            text="Asset Name",
            fill="#ffffff",
            font=("Istok Web", 14 * -1)
        )

        canvas.create_text(
            291,
            51,
            anchor="nw",
            text="Asset Owner",
            fill="#ffffff",
            font=("Istok Web", 14 * -1)
        )

        #Add asset screen
    def Add_asset(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.add_button_img = tk.PhotoImage(file=self.Load_asset("add_button.png"))
        self.back_button_img = tk.PhotoImage(file=self.Load_asset("back_button.png"))

        canvas = tk.Canvas(
            bg = "#ffffff",
            width = 500,
            height = 350,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x=0, y=0)

        canvas.create_rectangle(0, 0, 500, 350, fill='#5a5a5a', outline="")

        canvas.create_text(
            164,
            18,
            anchor="nw",
            text="AssetManager",
            fill="#f5f5f5",
            font=("Istok Web", 24 * -1)
        )

        button_1 = tk.Button(
            image=self.add_button_img,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 has been pressed!") #FIXME
        )

        button_1.place(x=158, y=311, width=185, height=38)

        canvas.create_text(
            157,
            309,
            anchor="nw",
            text="",
            fill="#000000",
            font=("Default Font", 12 * -1)
        )

        button_2 = tk.Button(
            image=self.back_button_img,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=self.Main_menu
        )

        button_2.place(x=1, y=0, width=99, height=29)

        canvas.create_text(
            1,
            0,
            anchor="nw",
            text="",
            fill="#000000",
            font=("Default Font", 12 * -1)
        )

        textbox_1 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            fg="#ffffff",
            insertbackground="#ffffff",
            highlightthickness=0
        )

        textbox_1.place(x=256, y=77, width=180, height=25)

        textbox_2 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            fg="#ffffff",
            insertbackground="#ffffff",
            highlightthickness=0
        )

        textbox_2.place(x=66, y=77, width=180, height=25)

        textarea_1 = tk.Text(
            bd=0,
            bg="#d9d9d9",
            fg="#ffffff",
            insertbackground="#ffffff",
            highlightthickness=0
        )

        textarea_1.place(x=256, y=173, width=180, height=127)

        textbox_3 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            fg="#ffffff",
            insertbackground="#ffffff",
            highlightthickness=0
        )

        textbox_3.place(x=66, y=125, width=180, height=25)

        textbox_4 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            fg="#ffffff",
            insertbackground="#ffffff",
            highlightthickness=0
        )

        textbox_4.place(x=256, y=125, width=180, height=25)

        textbox_5 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            fg="#ffffff",
            insertbackground="#ffffff",
            highlightthickness=0
        )

        textbox_5.place(x=66, y=173, width=180, height=25)

        textbox_6 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            fg="#ffffff",
            insertbackground="#ffffff",
            highlightthickness=0
        )

        textbox_6.place(x=67, y=274, width=180, height=25)

        textbox_7 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            fg="#ffffff",
            insertbackground="#ffffff",
            highlightthickness=0
        )

        textbox_7.place(x=67, y=223, width=180, height=25)

        canvas.create_text(
            116,
            102,
            anchor="nw",
            text="Service Tag",
            fill="#ffffff",
            font=("Istok Web", 14 * -1)
        )

        canvas.create_text(
            288,
            102,
            anchor="nw",
            text="End Of Warranty",
            fill="#ffffff",
            font=("Istok Web", 14 * -1)
        )

        canvas.create_text(
            107,
            150,
            anchor="nw",
            text="Purchase Date",
            fill="#ffffff",
            font=("Istok Web", 14 * -1)
        )

        canvas.create_text(
            326,
            150,
            anchor="nw",
            text="Notes",
            fill="#ffffff",
            font=("Istok Web", 14 * -1)
        )

        canvas.create_text(
            104,
            248,
            anchor="nw",
            text="Location/Office",
            fill="#ffffff",
            font=("Istok Web", 14 * -1)
        )

        canvas.create_text(
            111,
            196,
            anchor="nw",
            text="Model Name",
            fill="#ffffff",
            font=("Istok Web", 14 * -1)
        )

        canvas.create_text(
            116,
            51,
            anchor="nw",
            text="Asset Name",
            fill="#ffffff",
            font=("Istok Web", 14 * -1)
        )

        canvas.create_text(
            291,
            51,
            anchor="nw",
            text="Asset Owner",
            fill="#ffffff",
            font=("Istok Web", 14 * -1)
        )

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