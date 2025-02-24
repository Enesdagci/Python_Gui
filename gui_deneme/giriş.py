# Giriş ekranı

import tkinter as tk

def info():
    print("Wellcome {} and your password is {}".format(name.get(),password.get()))
screen = tk.Tk()
screen.geometry("360x360+780+360")
screen.title("Sign in")
screen.iconbitmap("./pythontutorial-1.ico")

# Karşılama metni
text_title = tk.Label(screen,text="Hoşgeldiniz...",font=("Calibri",20))
text_title.pack()

# İsim metni
text_name  = tk.Label(screen,text="Adınız: ",font=("Calibri",14))
text_name.pack(anchor="w")

# İsim girilen kısım
name = tk.StringVar()
text_entry_name = tk.Entry(screen, textvariable=name)
text_entry_name.pack(anchor="w",fill="x")

# Şifre Metni
text_pass_mess = tk.Label(screen,text="Password:",font=("Calibri",14))
text_pass_mess.pack(anchor="w")

# Şifre girilen kısım
password = tk.StringVar()
text_entry_pass = tk.Entry(screen, textvariable=password)
text_entry_pass.pack(anchor="w",fill=tk.X)

text_button = tk.Button(screen,text="Enter",command=info)
text_button.pack()
screen.mainloop()
