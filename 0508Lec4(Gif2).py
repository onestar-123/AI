from tkinter import*
window = Tk()
photo1 = PhotoImage(file = "C:/Users/gozil/AI/0508Lec3_Gif.gif")
photo2 = PhotoImage(file = "C:/Users/gozil/AI/0508Lec4_Gif.gif")
label1 = Label(window, image = photo1)
label2 = Label(window, image = photo2)
label1.pack(side=LEFT)
label2.pack()
window.mainloop()
