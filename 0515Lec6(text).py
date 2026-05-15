import tkinter as tk

def save_file():
    with open("note.txt","w") as f: #"w" 쓰기 모드로 열어야 써짐
        f.write(text.get("1.0", tk.END))
                
root = tk.Tk()
text = tk.Text(root)
text.pack()
button = tk.Button(root, text="Save", command = save_file)
button.pack()
root.mainloop()
