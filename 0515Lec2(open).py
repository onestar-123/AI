from tkinter import*
from tkinter.filedialog import*
    
root = Tk()
root.geometry("600x600")

label1 = Label(root, text = "선택된 파일 이름")
label1.pack()

filename = askopenfilename(parent = root, filetypes =(("GIF 파일", "*gif"), ("모든 파일", "*.*")))

label1.configure(text = str(filename))

root.mainloop()

