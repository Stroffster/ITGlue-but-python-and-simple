# Code generated by TkForge <https://github.com/axorax/tkforge>
# Donate to support TkForge! <https://www.patreon.com/axorax>

import os
import sys
import tkinter as tk

def load_asset(path):
    base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    assets = os.path.join(base, "assets")
    return os.path.join(assets, path)

window = tk.Tk()
window.geometry("500x350")
window.configure(bg="#ffffff")
window.title("Untitled")

canvas = tk.Canvas(
    window,
    bg = "#ffffff",
    width = 500,
    height = 350,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x=0, y=0)

image_1 = tk.PhotoImage(file=load_asset("computers.png"))

canvas.create_image(100, 175, image=image_1)

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
    fg="#ffffff",
    insertbackground="#ffffff",
    highlightthickness=0
)

textbox_1.place(x=230, y=175, width=230, height=30)

textbox_2 = tk.Entry(
    bd=0,
    bg="#d9d9d9",
    fg="#ffffff",
    insertbackground="#ffffff",
    highlightthickness=0
)

textbox_2.place(x=230, y=110, width=230, height=30)

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

button_1_image = tk.PhotoImage(file=load_asset("1.png"))

button_1 = tk.Button(
    image=button_1_image,
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 has been pressed!")
)

button_1.place(x=275, y=212, width=140, height=37)

canvas.create_text(
    275,
    212,
    anchor="nw",
    text="",
    fill="#000000",
    font=("Default Font", 12 * -1)
)

button_2_image = tk.PhotoImage(file=load_asset("2.png"))

button_2 = tk.Button(
    image=button_2_image,
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 has been pressed!")
)

button_2.place(x=287, y=252, width=115, height=30)

canvas.create_text(
    287,
    252,
    anchor="nw",
    text="",
    fill="#000000",
    font=("Default Font", 12 * -1)
)

window.resizable(False, False)
window.mainloop()
