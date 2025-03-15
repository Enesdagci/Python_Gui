import tkinter as tk

window = tk.Tk()

# Frames

frame = tk.Frame(master=window,bg="red",relief="ridge",bd=3)

button_w = tk.Button(
    master=frame,
    text="W",
    font=("Ariel",20,),
    width=3
)

button_s = tk.Button(
    master=frame,
    text="S",
    font=("Ariel",20,),
    width=3
)

button_a = tk.Button(
    master=frame,
    text="A",
    font=("Ariel",20,),
    width=3
)

button_d = tk.Button(
    master=frame,
    text="D",
    font=("Ariel",20,),
    width=3
)


button_w.pack(side="top")
button_a.pack(side="left")
button_d.pack(side="right")
button_s.pack(side="bottom")
frame.pack()
window.mainloop()