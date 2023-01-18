from tkinter import *

import tkinter.filedialog
from tkinter import filedialog as fd

def vali_fail():
    faili_tyyp = [('Python failid', "*.txt"), ('Kõik failid', '*')]
    nimi = tkinter.filedialog.Open(filetypes=faili_tyyp)
    valik = nimi.show()    
    
    with open("jukebox.txt") as f:
        contents = f.read()
        kumm=contents.replace("\n"," ").split(".")
        print(kumm)
 
aken = Tk()
aken.title("jukebox")
aken.geometry("300x300")

rida=Entry(aken)
rida.grid(row=3, column=0, sticky="w")


text = Text(aken, height=10)
text.grid(row=0, column=0, sticky='w')


open_button=Button(aken,text="ava fail",command=vali_fail)
open_button.grid(row=2,column=0, sticky="w")


aken.mainloop()





