import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
       
        self.title("Replace")
        self.geometry("400x150")
        self.attributes("-toolwindow",True)

        # Column configure
        self.columnconfigure(0,weight=4)
        self.columnconfigure(1,weight=1)

        # Adding Frames
        input_frame = InputFrame(self)
        input_frame.grid(row=0,column=0)

        button_frame = ButtonFrame(self)
        button_frame.grid(row=0,column=1)




class InputFrame(tk.Frame):
    def __init__(self,frame):
        super().__init__(frame)

        # Column configure
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=3)

        # Labels
        self.label_find = tk.Label(master=self,text="Find what: ")
        self.label_replace = tk.Label(master=self,text="Replace with: ")

        # Entry boxes
        self.entry_find = tk.Entry(master=self,width=30)
        self.entry_replace = tk.Entry(master=self,width=30)

        # checkboxes 
        self.check_match = tk.Checkbutton(master=self,text="Match case")
        self.check_wrap = tk.Checkbutton(master=self,text="Wrap around")

        # packing
        self.label_find.grid(row=0,column=0,sticky="w")
        self.entry_find.grid(row=0,column=1)
        self.label_replace.grid(row=1,column=0,sticky="w")
        self.entry_replace.grid(row=1,column=1)
        self.check_match.grid(row=2,columnspan=2,sticky="w")
        self.check_wrap.grid(row=3,columnspan=2,sticky="w")

        for widget in self.winfo_children():
            widget.grid(padx=0,pady=5)




class ButtonFrame(tk.Frame):
    def __init__(self,frame):
        super().__init__(frame)

        self.columnconfigure(0,weight=1)

        # buttons
        self.button_find = tk.Button(master=self,text="Find Next",width=10)
        self.button_replace = tk.Button(master=self,text="Replace",width=10)
        self.button_rep_all = tk.Button(master=self,text="Replace All",width=10)
        self.button_cancel = tk.Button(master=self,text="Cancel",width=10)

        # packing
        self.button_find.grid(row=0,column=0)
        self.button_replace.grid(row=1,column=0)
        self.button_rep_all.grid(row=2,column=0)
        self.button_cancel.grid(row=3,column=0)

        for widget in self.winfo_children():
            widget.grid(padx=0,pady=3)


if __name__ == "__main__":
    app = App()
    app.mainloop()