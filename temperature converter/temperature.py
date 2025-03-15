import tkinter as tk
from tkinter import messagebox

# fonksiyonlar
def f_to_c():
    result = (int(entry_fahren.get()) - 32) * 10 / 18
    return  value_str.set("{} Fahrenheit = {} Celcius".format(value_int.get(),result))

def button_pushed():
    if messagebox.askyesno(title="Emin misiniz.",message="İşlemin yapılmasından emin misiniz?"):
        f_to_c()
    else:
        messagebox.showinfo(title="admin",message="Sen bilirsin...")

window = tk.Tk()

# Uygulamanın ekran özellikleri
window.title("Temperature Converter")
window.resizable(False,False)

# Veri tiplerinin oluşturulması
value_int = tk.IntVar()
value_str = tk.StringVar()

# Çerçeveler
frame_convert = tk.Frame(master=window)

# Etiketler
label_text = tk.Label(master=frame_convert,text="Fahrenheit: ")
label_result = tk.Label(master=window,text="fonksiyonun sonucu",textvariable=value_str)

# Buttonlar
button_convert = tk.Button(master=frame_convert,text="Convert",command=button_pushed)

# Giriş kutuları
entry_fahren = tk.Entry(master=frame_convert,textvariable=value_int)

# Widgetların yerleştirilmesi
label_text.grid(row=0,column=0)
entry_fahren.grid(row=0,column=1)
button_convert.grid(row=0,column=2,padx=5)
frame_convert.pack(padx=10,pady=5)
label_result.pack(pady=5)



window.mainloop()