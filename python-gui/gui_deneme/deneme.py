import tkinter as tk

window = tk.Tk()
window.geometry("360x180")
window.title("First Gui Program")
window.resizable(False,False)
window.config(background="#5cfcff")

photo = tk.PhotoImage(file="indir.png")
window.iconbitmap("./pythontutorial-1.ico")

label = tk.Label(master=window,
                 text="Hello fuckers",
                 font=("Ariel",20),
                 fg="red",
                 bg="yellow",
                 relief="raised",
                 border=5,
                )

label.pack(side="top",anchor="center")

window.mainloop()