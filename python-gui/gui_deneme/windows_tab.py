import tkinter as tk
from tkinter import ttk

window = tk.Tk()

notebook = ttk.Notebook(master=window)

# Frames
tab_1 = tk.Frame(master=notebook)
tab_2 = tk.Frame(master=notebook)

# Notes
notebook.add(tab_1,text="First tab")
notebook.add(tab_2,text="Second tab")

# labels
label_1 = tk.Label(master=tab_1,text="Hello, Everybody this is first tab.",width=25,height=15)
label_2 = tk.Label(master=tab_2,text="Goodbye, this is second tab.",width=25,height=15)

notebook.pack()
label_1.pack()
label_2.pack()
window.mainloop()