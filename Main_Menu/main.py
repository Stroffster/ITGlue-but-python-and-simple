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

button_1_image = tk.PhotoImage(file=load_asset("1.png"))

button_1 = tk.Button(
    image=button_1_image,
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 has been pressed!")
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

button_2_image = tk.PhotoImage(file=load_asset("2.png"))

button_2 = tk.Button(
    image=button_2_image,
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 has been pressed!")
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

window.resizable(False, False)
window.mainloop()