# IMPORTS
import tkinter as tk
from tkinter import ttk

# Create window object
win = tk.Tk()

# Create title
win.title("More Complex")


# Modified Button Click Function
def click_me():
    action.configure(text=f"Hello {name.get()} {number_chosen.get()}")


# Text box label
ttk.Label(win, text="Enter a name:").grid(column=0, row=0)

# Adding a textbox entry widget
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

# Adding a button
action = ttk.Button(win, text="Click me!", command=click_me)
action.grid(column=2, row=1)

# Configure Combobox Widget
ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')  # State makes this read only
number_chosen['values'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

# Creating three check buttons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

# Places cursor on name entry on program start
name_entered.focus()

# Start GUI
win.mainloop()
