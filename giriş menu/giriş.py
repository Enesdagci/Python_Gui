import tkinter as tk

screen = tk.Tk()

screen_width = 360
screen_height = 360

window_width = screen.winfo_screenwidth()
window_height = screen.winfo_screenheight()

center_x = int(window_width /2 - screen_width /2)
center_y = int(window_height /2 - screen_height/2)

def login_show():
    print("Wellcome {}{}, your password is the {}".format(name.get(),surname.get(),password.get()))

screen.geometry(f"{screen_width}x{screen_height}+{center_x}+{center_y}")
screen.title("Sign in")
screen.resizable(False,False)
screen.iconbitmap("./pythontutorial-1.ico")

text_title = tk.Label(screen, text="Hoşgeldiniz...",font=("Ariel",20))
text_title.pack()

text_message = tk.Label(screen, text="Adınız: ",font=("Ariel",14))
text_message.pack()

name = tk.StringVar()
text_name = tk.Entry(screen, textvariable=name)
text_name.pack(fill="x")

text_message_1 = tk.Label(screen,text="Soyadınız:",font=("Ariel",14))
text_message_1.pack()

surname = tk.StringVar()
text_surname = tk.Entry(screen, textvariable=surname)
text_surname.pack(fill="x")

text_message_2 = tk.Label(screen, text="Şifre",font=("Ariel",14))
text_message_2.pack()

password = tk.StringVar()
text_password = tk.Entry(screen, textvariable=password)
text_password.pack(fill="x")

login = tk.Button(screen,
                  text="Sign In",
                  font=("Ariel",14),
                  command=login_show)
login.pack(ipadx = 10 )
screen.mainloop()
