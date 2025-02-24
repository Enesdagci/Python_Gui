import tkinter as tk
from tkinter import messagebox

def clicked():
    # Uyarılar ile bilgiler
    messagebox.showinfo(
        title="Information",
        message="Gaylar giremez bilginize..."
    )
    messagebox.showwarning(
        title="Aykırı giriş",
        message="Kullanıcı adı veya şifre hatalı..."
    )
    messagebox.showerror(
        title="Aykırı Kullanıcı",
        message="Geçersiz kullanıcı..."
    )
    # Soru sormak
    messagebox.askokcancel(
        title="İndirmek bağlantısı",
        message="İndirmek istiyormusunuz?"
    )
    messagebox.askyesno(
        title="Onaylama kutusu",
        message="Uygulamayı onaylıyor musunuz?"
    )
    messagebox.askquestion(
        title="Soru",
        message="Bugün ne pişirmeyi düşünüyorsunuz?"
    )
    messagebox.askretrycancel(
        title="Dosya indirme sorunu",
        message="Dosya indirilemedi indirmek içim yeniden başlatın...",
    )
window = tk.Tk()

button = tk.Button(master=window,
                   text="Click",
                   command=clicked
                   )

button.pack()
window.mainloop()