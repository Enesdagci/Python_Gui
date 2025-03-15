import tkinter as tk
import sys

text_title ="Python Kurulum Sihirbazına Hoşgeldiniz."
text_1 = "Python olarak, internet üzerinde  tüm python kullanıcıları ile\n kullanabileceksiniz. Ayrıca:"
text_2 = "*Gelecekteki ürünlere hızla erişim"
text_3 = "*Güncellemeler otomatik alacak"
text_4 = "*Kod yazarken arkadaşlarınıza mesaj gönderebilecek"
text_5 = "*Arkadaşlarınız ile en iyi sunucuları bulursunuz"
                                                
screen = tk.Tk()
# Ekranın boyutunun ayarlanması
screen_width = 600
screen_height = 400
# Ekranın pozisyonunun ayarlanması
window_width = screen.winfo_screenwidth()
window_height = screen.winfo_screenheight()

center_x = int(window_width /2 - screen_width /2)
center_y = int(window_height /2 - screen_height /2)

screen.geometry("{}x{}+{}+{}".format(screen_width,screen_height,center_x,center_y))

# Fonksiyonların tanımlanması
def next_func():
    print("Pressed next window.")

def cancel_func():
    sys.exit()
    print("Pressed Canceled.")
    
# Ekran başlığı
screen.title("Python Setup Wizard")
screen.resizable(False,False)

# Ekran ikonu
screen.iconbitmap("./pythontutorial-1.ico")

# Çerçeve ekleme
frame_left = tk.Frame(screen,width=150,height=360,relief="solid",borderwidth=2)
frame_left.place(x=0)

frame_right = tk.Frame(screen,width=450,height=360)
frame_right.place(x=175)

frame_bottom = tk.Frame(screen,width=600,height=40,relief="solid",borderwidth=1)
frame_bottom.pack(side="bottom",fill="x")

# Uygulamanın metinleri ve başlıklarını ekleme
message_title = tk.Label(frame_right,text=text_title,font=("Ariel",16))
message_text_1 = tk.Label(frame_right,text=text_1,font=("Ariel",12))
message_text_2 = tk.Label(frame_right,text=text_2,font=("courier",10))
message_text_3 = tk.Label(frame_right,text=text_3,font=("Courier",10))
message_text_4 = tk.Label(frame_right,text=text_4,font=("courier",10))
message_text_5 = tk.Label(frame_right,text=text_5,font=("Courier",10))

# Uygulamanın butonlarını ekleme (Bottom)
button_next = tk.Button(frame_bottom,text="İleri >",command=next_func)
button_next.pack(side="right",padx=10,ipadx=20)

button_cancel = tk.Button(frame_bottom,text="İptal",command=cancel_func)
button_cancel.pack(side="right",padx=10,ipadx=20,pady=5)

# Uygulamanın metinlerini ve başlıklarının pozisyonlarını ayarlama (Right)
message_title.grid(row=0,pady=20)
message_text_1.grid(row=0,padx=10)
message_text_2.grid(row=1,sticky="w",padx=10,pady=10)
message_text_3.grid(row=2,sticky="w",padx=10)
message_text_4.grid(row=3,sticky="w",padx=10,pady=10)
message_text_5.grid(row=4,sticky="w",padx=10)

# Resim eklenmesi (Left)
image = tk.PhotoImage(file="./python.png")
label_image = tk.Label(frame_left,image=image)
label_image.pack()

screen.mainloop()
