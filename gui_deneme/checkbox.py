import tkinter as tk

window = tk.Tk()

def display():
    if x.get() == 1:
        print("doğrulandı.")
    else:
        print("doğrulanmadı.")

x = tk.IntVar ()
checkbox = tk.Checkbutton(master=window,
                          text="Python",
                          variable=x,
                          onvalue=1,
                          offvalue=0,
                          command=display,
                        )

checkbox.pack()
window.mainloop()