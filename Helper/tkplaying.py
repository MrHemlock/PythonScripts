import tkinter as tk

def clicked():
    lbl.configure(text="Button was clicked!!")

window = tk.Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

lbl = tk.Label(window, text="Hello")
lbl.grid(column=0, row=0)

txt = tk.Entry(window, width=10)
txt.grid(column=1, row=0)

btn = tk.Button(window, text="Click Me", command=clicked)
btn.grid(column=2, row=0)

window.mainloop()
