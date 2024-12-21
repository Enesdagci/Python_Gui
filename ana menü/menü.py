import tkinter as tk

screen = tk.Tk()
# Ekranın boyutunun ayarlanması
screen_width = 360
screen_height = 180
# Ekranın pozisyonunun ayarlanması
window_width = screen.winfo_screenwidth()
window_height = screen.winfo_screenheight()

center_x = int(window_width /2 - screen_width /2)
center_y = int(window_height /2 - screen_height /2)

screen.geometry("{}x{}+{}+{}".format(screen_width,screen_height,center_x,center_y))
# Ekran başlığı
screen.title("Python Setup Wizard")

# Uygulamaya metin başlığı ve metin ekleme
message_title = tk.Label(screen,text="Hoşgeldiniz")
message_title.pack()


screen.mainloop()
