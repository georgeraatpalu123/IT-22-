from tkinter import *


aken = Tk()
aken.title("Botswana")

kujund=Canvas(aken, width=500, height=290)
kujund.pack()




kujund.create_rectangle(0, 0, 500,100 ,fill="#00FFFF",width=0)

kujund.create_rectangle(0, 100, 500,110 ,fill="white",width=0)

kujund.create_rectangle(0, 110, 500,180,fill="black",width=0)

kujund.create_rectangle(0, 180, 500,190 ,fill="white",width=0)

kujund.create_rectangle(0, 190, 500,290 ,fill="#00FFFF",width=0)


                       


aken.mainloop()