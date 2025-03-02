import tkinter as tk

# Functions
def create_window():
    new_window = tk.Tk()
    window.destroy()

# Screen
window = tk.Tk()

# Buttons

button = tk.Button(
    master=window,
    text="Create new window",
    command=create_window
)

button.pack()
window.mainloop()