from tkinter import *


aken = Tk()
aken.title("Joonistamine")

kujund=Canvas(aken, width=500, height=500)
kujund.pack()




kujund.create_rectangle(10, 10, 400, 60,
                                outline = "aqua", 
                                width = 250)





aken.mainloop()