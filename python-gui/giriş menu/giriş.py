import tkinter as tk

screen = tk.Tk()

screen_width = 360
screen_height = 180

window_width = screen.winfo_screenwidth()
window_height = screen.winfo_screenheight()

center_x = int(window_width /2 - screen_width /2)
center_y = int(window_height /2 - screen_height/2)

def login_show():
    print("Wellcome {}, your password is the {}".format(name.get(),password.get()))

screen.geometry(f"{screen_width}x{screen_height}+{center_x}+{center_y}")
screen.title("Sign in")
screen.resizable(False,False)
screen.iconbitmap("./pythontutorial-1.ico")
screen.columnconfigure(0,weight=1)
screen.columnconfigure(1,weight=3)

text_title = tk.Label(screen, text="Hoşgeldiniz...",font=("Ariel",20))
text_title.grid(column=0,row=0,sticky="w",padx=5)

text_message = tk.Label(screen, text="Kullanıcı: ",font=("Ariel",14))
text_message.grid(column=0,row=1,sticky="w",padx=5)

name = tk.StringVar()
text_name = tk.Entry(screen, textvariable=name)
text_name.grid(column=1,row=1)

text_message_2 = tk.Label(screen, text="Şifre",font=("Ariel",14))
text_message_2.grid(column=0,row=2,sticky="w",padx=5)

password = tk.StringVar()
text_password = tk.Entry(screen, textvariable=password,show=".")
text_password.grid(column=1,row=2)

login = tk.Button(screen,text="Sign In",font=("Ariel",14),command=login_show)
login.grid(column=1,row=3)
screen.mainloop()
