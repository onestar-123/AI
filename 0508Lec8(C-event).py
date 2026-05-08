from tkinter import*
from tkinter import messagebox

def Enter(event):
    messagebox.showinfo("마우스", "올라감")

window = Tk()

window.bind("<Enter>", Enter)

window.mainloop()
