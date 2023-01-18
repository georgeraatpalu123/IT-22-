from tkinter import *
import tkinter.filedialog

aken = Tk()
aken.title("jukebox.txt")
aken.geometry("300x300")
 


rida=Entry(aken)
rida.grid(row=2, padx=50)



def vali_fail():
    faili_tyyp = [("Python failid", ".txt"), ("Kõik failid", "")]
    nimi = tkinter.filedialog.Open(filetypes=faili_tyyp)
    valik = nimi.show()

    if valik != "":
        print(valik)


nupp=Button(aken, text = "Vajuta siia et muusikat valida!", command = vali_fail)
nupp.grid(row=5, padx=50)













aken.mainloop()
          




        


        