import tkinter as tk
from tkinter import colorchooser

def clicked():
    color = colorchooser.askcolor()
    window["bg"]=color[1]



window = tk.Tk()
window.geometry("360x360")

button = tk.Button(
    master=window,
    text="Click",
    command=clicked
)
button.pack()
window.mainloop()