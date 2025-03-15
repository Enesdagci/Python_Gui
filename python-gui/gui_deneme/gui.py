import tkinter as tk


screen = tk.Tk()
screen.title("Python Setup Wizard")

def counter():
    print("Dosya yükleniyor...")
def zeroes(event):
    print("Nums : 0 yazdı...")
# Uygulamanın ölçüleri
screen_width = 480
screen_height = 360

# Bilgisayar ekranının ölçüleri 
window_width = screen.winfo_screenwidth()
window_height = screen.winfo_screenheight()

# Koordinat hesabı
center_x = int(window_width / 2 - screen_width /2)
center_y = int(window_height / 2 - screen_height /2)

# Ekran boyut ve konumu vermesi
screen.geometry(f"{screen_width}x{screen_height}+{center_x}+{center_y}")

# Ekranın büyümesini engelleme
screen.resizable(False,False)

# Uygulamaya icon ekleme
screen.iconbitmap("./pythontutorial-1.ico")
text_image = tk.PhotoImage(file="./indir.png")

# Buton ekleme mouse ya da klavye den giriş yapma
install_button = tk.Button(screen,
                           text="Next",
                           command=counter,
                           state="active",
                           image=text_image,
                           compound = "left",
                           padx=5
                        )

#install_button.bind('<Return>', zeroes,add="+")
#install_button.focus()

# Resim bakılacak

# Metin ekleme Resim ile beraber
text_title = tk.Label(screen,text="Pyhton Setup Wizard",font=("Ariel",20))

text_title.pack()
install_button.pack(ipadx=10,
                    ipady=2)

# Tek satırlık metin oluşturma
text_message = tk.Label(screen,text="Password: ",font=("Calibri",14))
text = tk.StringVar()
text_box = tk.Entry(screen,textvariable=text,show=".")
text_message.pack()
text_box.pack()
screen.mainloop()

