import tkinter as tk

with open(file="./setup wizard/text.txt",mode="r",encoding="utf-8") as file:
    text = file.readline()

with open(file="./setup wizard/sozlesme.txt",mode="r",encoding="utf-8") as file_soz:
    sozlesme = file_soz.readlines()

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
screen.resizable(False,False)
screen.iconbitmap("./setup wizard/pythontutorial-1.ico")

# Çerçeve ekleme
frame_top = tk.Frame(screen,width=600,height=60,relief="solid",borderwidth=1)
frame_top.place(x=0,y=0)

# Üst çerçeveye görsel eklenmesi
image = tk.PhotoImage(file="./setup wizard/Python.png")

# Üst çerçeveye eklenecekler
text_message = tk.Label(frame_top,text=text,font=("Ariel",12),image=image,compound="left")
text_message.pack(pady=10)


screen.mainloop()
