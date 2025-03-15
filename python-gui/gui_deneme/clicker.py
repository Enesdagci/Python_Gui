import tkinter as tk

count = 0
def click():
    global count
    count += 1
    label["text"]=count
window = tk.Tk()

window.title("The Clicker")

photo= tk.PhotoImage(file="indir.png")

button = tk.Button(master=window,
                   text="Click Me!",
                   command=click,
                   font=("Ink Free",50,"bold"),
                   bg="#ff6200",
                   fg="#fffb1f",
                   activebackground="#FF0000",
                   activeforeground="#fffb1f",
                   image=photo,
                   compound="bottom",
                   state="normal"
                )

label = tk.Label(master=window,
                 text=count,
                 font=("Monospace",50)
                )

label.pack()
button.pack()

window.mainloop()