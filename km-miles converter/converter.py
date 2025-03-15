import tkinter as tk

# Convert function
def convert():
    result = int(text_box.get()) * 1.609
    text.set("{} kilometers".format(result))

# window
screen = tk.Tk()
screen.title("Km-Miles Converter")
screen.geometry("300x150")
screen.resizable(False,False)

# title
text_title = tk.Label(screen,text="Miles to Kilometers",font=("Ariel",20))
text_title.pack(pady=5)

# frame
frame = tk.Frame(screen)

# entry box
miles = tk.IntVar()
text_box = tk.Entry(frame,textvariable=miles)
text_box.pack(side="left",padx=10)

# button 
button_convert = tk.Button(frame,text="convert",command=convert) 
button_convert.pack(side="left")

# frame end
frame.pack(pady=15)

text = tk.StringVar()
text_output=tk.Label(screen,text="OUTPUT",font=("Ariel",14),textvariable=text)
text_output.pack()

# run
screen.mainloop()