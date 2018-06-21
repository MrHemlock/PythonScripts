# Imports
import tkinter as tk
from tkinter import ttk

# Create window object
win = tk.Tk()

# create counter tk variable 
counter = tk.IntVar()

# Add a title
win.title("Clicker Test")

# Add the counter label

counter_label = ttk.Label(win, textvariable=counter)
counter_label.grid(column=0, row=0)

# Define click function
def click_me():
    counter.set(counter.get() + 1)


clicker = ttk.Button(win, text="Click Me", command=click_me)
clicker.grid(column=0, row=1)

win.mainloop()



