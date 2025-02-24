import tkinter as tk
from tkinter import filedialog

"""
Dosya yollarını doğru yazılmasına rağmen hatalı gösteriyor.
pythonun ya da windows ta slaslar ile ilgili sıkıntıları var

"""

# Functions
def open_file():
    files = filedialog.askopenfilename(initialdir=r"C:\Users\enesd\Desktop\python\python-gui\gui_deneme",title="Open File",filetypes=(("text files","*.txt"),("all files","*.*")))
    file = open(files,"r")
    print(file.read())
    file.close()


window = tk.Tk()

# Buttons
button = tk.Button(
    master=window,
    text="Click to open file",
    command=open_file
)

button.pack()
window.mainloop()

