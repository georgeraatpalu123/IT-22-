from tkinter import *

aken=Tk()
aken.title("Käibemaksukalkulaator")
aken.iconbitmap("favicon.ico")
aken.geometry("400x300")


Hind=Label

var=IntVar()
valikukast = Radiobutton(aken,text="9%", variable=var, value=1)
valikukast.grid(row=1, column=1)
valikukast = Radiobutton(aken,text="20%", variable=var, value=2)
valikukast.grid(row=2, column=1)

tekst=Label(aken,
            text="Käibemaksumäär:",
            font="Tahoma 12",
            padx=2,
            pady=2)
tekst.grid(row=1, column=0)

joon=Label(aken,
           text="_________________________",
           font="Tahoma 10",
           padx=2,
           pady=2)
joon.grid(row=3, column=0, columnspan=2)

kiri=Label(aken,
           text="Käibemaks:",
           
           font="Tahoma 12",
           padx=3,
           pady=3)
kiri.grid(row=4,column=0, columnspan=3,sticky="W")

kirjad=Label(aken,
           text="Hind käibemaksuga:",
           
           font="Tahoma 12",
           padx=4,
           pady=4)
kirjad.grid(row=5,column=0, columnspan=4,sticky="w")

euro=Label(aken,
           font="Tahoma 12",
           text="0.00€",
           padx=4,
           pady=4)
euro.grid(row=5,column=2, columnspan=4)

eurod=Label(aken,
           font="Tahoma 12",
           text="0.00€",
           padx=4,
           pady=4)
eurod.grid(row=4,column=2, columnspan=3)
          
          
           



aken.mainloop()