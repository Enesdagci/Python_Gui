import tkinter as tk
from tkinter import ttk
import time

# Functions
def start():
    gb =100
    speed = 1
    download = 0
    while(download < gb):  
        time.sleep(0.05)
        bar["value"] += (speed/gb)*100
        download += speed
        percent.set(str(int(download / speed))+"%")
        text.set(str(download)+"/"+str(gb)+" Gb completed.")
        window.update_idletasks()

window = tk.Tk()

# variable
percent = tk.StringVar()
text = tk.StringVar()
# bar
bar = ttk.Progressbar(master=window,orient="vertical",length=300)

# buttons
button = tk.Button(master=window,text="download",command=start)

# label
label_percent = tk.Label(master=window,textvariable=percent)
label_complete = tk.Label(master=window,textvariable=text)

bar.pack()
label_percent.pack()
label_complete.pack()
button.pack()

window.mainloop()