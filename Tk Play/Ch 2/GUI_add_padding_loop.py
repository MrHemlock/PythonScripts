# IMPORTS
import tkinter as tk
from tkinter import ttk, scrolledtext

# Radiobutton Globals
colors = ["Blue", "Gold", "Red"]

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


# Radiobutton Callback
def rad_call():
    rad_sel = radVar.get()
    if rad_sel == 0:
        win.configure(background=colors[0])
    elif rad_sel == 1:
        win.configure(background=colors[1])
    elif rad_sel == 2:
        win.configure(background=colors[2])


# Create three Radiobuttons using one variable
radVar = tk.IntVar()

# Selecting non-existing index value for radVar
radVar.set(99)

# Creating all Radiobutton widgets within one loop
for col in range(3):
    curRad = tk.Radiobutton(win, text=colors[col], variable=radVar,
                            value=col, command=rad_call)
    curRad.grid(column=col, row=5, sticky=tk.W)

# Using a scrolled Text control
scrol_w = 30
scrol_h = 3
scr = scrolledtext.ScrolledText(win, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)

# Create a container to hold labels
buttons_frame = ttk.LabelFrame(win, text=' Labels in a Frame ')
buttons_frame.grid(column=0, row=7, padx=20, pady=40)
# buttons_frame.grid(column=1, row=7)       # Now in col 1


# Place labels into the container element
ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label2").grid(column=0, row=1, sticky=tk.W)
ttk.Label(buttons_frame, text="Label3").grid(column=0, row=2, sticky=tk.W)

for child in buttons_frame.winfo_children():
    child.grid_configure(padx=8, pady=4)

# Places cursor on name entry on program start
name_entered.focus()

# Start GUI
win.mainloop()
