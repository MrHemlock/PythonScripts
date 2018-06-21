from tkinter import *
import requests

root=Tk()
#root.geometry("1215x717")

e=Entry(root)
e.grid(row=0)
e.focus_set()


e1=Entry(root)
e1.grid(row=1)

def enter():
    value=str(e.get())
    value2=str(e1.get())
    e.delete(0, END)
    e1.delete(0, END)
    skinid=value2
    champion = str.title(value)
    if champion == "Wukong":
        champion = "MonkeyKing"
    new_champion = champion.replace(' ', '')
    imgurl = "http://ddragon.leagueoflegends.com/cdn/img/champion/splash/" + new_champion + "_{}.jpg".format(skinid)
    raw=requests.get(imgurl).open()
    

print(raw)
b=Button(root,text="Enter",command=enter)
b.grid(row=0,column=1)

root.mainloop()