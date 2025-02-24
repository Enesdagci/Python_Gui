import tkinter as tk

window = tk.Tk()

def submit():
    username = entry.get()
    print(username)

def deleter():
    entry.delete(0)

send = tk.Button(master=window,
                   text="Submit",
                   command=submit,             
                )

deletes = tk.Button(master=window,
                   text="delete",
                   command=deleter
                )

entry = tk.Entry(font=("Ink Free",50),
                 bg="#000000",
                 fg="#00FF00",
                 width=10,
                 show="*"
                )

deletes.pack(side="right")
send.pack(side="right")
entry.pack()

window.mainloop()
