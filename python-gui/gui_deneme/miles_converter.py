import tkinter as tk 

def converter():
    mile = float(number_input.get())
    kilometer = mile * 1.609
    result_str.set(f"{kilometer} kilometers")


window = tk.Tk()
window.title("Mile To Km")

window_width = 360
window_height = 180

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

main_text = tk.Label(master = window, text = "MİLES TO KİLOMETERS" , font = "Calibri 24 bold")

user_frame = tk.Frame(master = window)
entry_int = tk.IntVar()
number_input = tk.Entry(master = user_frame, textvariable = entry_int)

convert_button = tk.Button(master = user_frame, text = "Convert", bg = "red", command = converter)
convert_button.bind("<return>", converter)

result_str = tk.StringVar()
result_text = tk.Label(master = window, font = "Calibri", textvariable = result_str, text = "kilometers")

main_text.pack(pady = 5)
number_input.pack(side = "left", padx = 5, pady = 10)
convert_button.focus()
convert_button.pack(side = "left", padx = 5 )
user_frame.pack()
result_text.pack()
window.mainloop()
