import tkinter as tk

# Functions
def submit():
    print(entry_name.get() + " " + entry_password.get())

window = tk.Tk()

# Labels
label_title = tk.Label(master=window,text="Enter Your İnfo")
label_name = tk.Label(master=window,text="User Name: ")
label_password = tk.Label(master=window,text="Password")

# Buttons
button_submit = tk.Button(master=window,text="Submit",command=submit)

# Entry box
entry_name = tk.Entry(master=window)
entry_password = tk.Entry(master=window,show="*")

# Grid
label_title.grid(row=0,columnspan=2)
label_name.grid(row=1,column=0)
entry_name.grid(row=1,column=1)

label_password.grid(row=2,column=0)
entry_password.grid(row=2,column=1)

button_submit.grid(row=3,columnspan=2)

window.mainloop()