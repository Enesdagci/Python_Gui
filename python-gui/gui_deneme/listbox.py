import tkinter as tk

def send():
    food = []
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
    print("You have ordered: ")
    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(),entry_box.get())
    listbox["height"] = listbox.size()

def delete():
    listbox.delete(listbox.curselection())
    listbox["height"] = listbox.size()

window = tk.Tk()
window.title("Food Lists")

entry_box = tk.Entry(master=window)

# Lists boxes
listbox = tk.Listbox(master=window,
                     bg="#f7ffde",
                     font=("Constantia",20),
                     width=20,    
                     selectmode="multiple"             
                    )
listbox.pack()

listbox.insert(1,"Pizza")
listbox.insert(2,"Hamburger")
listbox.insert(3,"Ekmek arası köfte")
listbox.insert(4,"Ekmek arası tavuk")
listbox.insert(5,"Ekmek arası nugget")
listbox.insert(6,"Patso")
listbox.insert(7,"Karışık tost")
listbox.insert(8,"Kaşarlı tost")
listbox.insert(9,"Sucuklu tost")
listbox.insert(10,"İzmir Bomba")
listbox.insert(11,"Bisküvit")
listbox["height"] = listbox.size()

# Buttons
submit = tk.Button(master=window,
                   text="Submit",
                   command=send
                   )

add_button = tk.Button(master=window,
                       text="Add",
                       command=add
                       )

delete_button = tk.Button(master=window,
                          text="Delete",
                          command=delete
                        )

entry_box.pack()
add_button.pack()
delete_button.pack()
submit.pack()

window.mainloop()