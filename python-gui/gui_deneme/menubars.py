import tkinter as tk

# Functions
def open_file():
    pass

def save_file():
    pass

def edit_cut():
    pass

def edit_copy():
    pass

def edit_redo():
    pass
# Screens
window = tk.Tk()


# Menus
# ana kısım
menubar = tk.Menu(master=window)
window.config(menu=menubar)

# file menu
file_menu = tk.Menu(
    master=menubar,
    tearoff=False
)

menubar.add_cascade(
    label="File",
    menu=file_menu
)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=exit)

# edit menu
edit_menu = tk.Menu(
    master=menubar,
    tearoff=False
)
menubar.add_cascade(
    label="Edit",
    menu=edit_menu
)
edit_menu.add_command(label="Cut",command=edit_cut)
edit_menu.add_command(label="Copy",command=edit_copy)
edit_menu.add_command(label="Redo",command=edit_redo)
window.mainloop()