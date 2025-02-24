import tkinter as tk

window = tk.Tk()

def submit():
    print("The temperature is: "+ str(scale.get())+" degrees C")

label_hot = tk.Label(master=window,
                     text="HOT",
                     font=("Calibri",20),
                     fg="#ff0000",
                     bg="#ff6200"
                    )

label_cold = tk.Label(master=window,
                      text="COLD",
                      font=("Calibri",20),
                      fg="#1864ab",
                      bg="#5c7cfa",
                    )

scale = tk.Scale(master=window,
                 from_=100,
                 to=0,
                 length=500,
                 troughcolor="light blue",
                 fg="#FF1C00",
                 bg="#111111",
                 orient="vertical",
                 font=("Ariel",12),
                 tickinterval=10, # yazıların aralıklarını indexler 10-10, 20-20
                 resolution=2 # ... kadar adım ilerler

                )

button = tk.Button(master=window,
                   text="Submit",
                   command=submit
                   )


label_hot.pack()
scale.pack()
label_cold.pack()
button.pack()
window.mainloop()