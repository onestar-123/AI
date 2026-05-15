'''
from tkinter import*
root = Tk()
모듈 전체를 읽어오는 것
'''
import tkinter as tk

def say_hello():
    name = entry.get()
    label.config(text="Hellow! {}".format(name))

root = tk.Tk()
# 모든 이벤트 처리는 root = tk.TK(), root.mainloop() 사이에서 이루어짐
entry = tk.Entry(root) # 입력창 만들기
entry.pack()

button = tk.Button(root,text = "Click Me", command = say_hello)
button.pack()

label = tk.Label(root, text="No Input")
label.pack()

root.mainloop()
