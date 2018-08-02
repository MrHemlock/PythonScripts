# Import statements
import tkinter as tk
from tkinter import ttk

# Create instance
win = tk.Tk()

# Add a title
win.title("Textbox Fun")


# Modified Button Click Function
def click_me():
    action.configure(text=f"Hello {name.get()}")


# Changing our Label
ttk.Label(win, text="Enter a name:").grid(column=0, row=0)

# Adding a textbox entry widget
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

# Adding a button
action = ttk.Button(win, text="Click Me!", command=click_me)
action.grid(column=2, row=1)


# Start GUI
win.mainloop()
