import tkinter as tk

# Functions
def send():
    inputs = text.get("1.0",tk.END)
    print(inputs)


window = tk.Tk()

# texts
text = tk.Text(
    master=window,
    font=("ink free",20),
    height=8,
    width=20,
    bg="light yellow",
    padx = 5,
    pady=5
)

# buttons
submit_button = tk.Button(
    master=window,
    text="Submit",
    command=send
)

text.pack()
submit_button.pack()
window.mainloop()