import tkinter
 

aken = tkinter.Tk()
aken.title("jukebox.txt")
aken.geometry("800x100")
 
sample_text = tkinter.Entry(aken)
sample_text.pack()
 


def set_text_by_button():
    sample_text.delete(0,"end")
     
    
    
 

set_up_button = tkinter.Button(aken, height=1, width=10, text="Vali muusika")
set_up_button2 = tkinter.Button(aken, padx=50, height=1, width=10, text="Vali Järjekorra number")

 
set_up_button.pack()
set_up_button2.pack()

aken.mainloop()


jrk = 1
a = input("Sisesta faili nimi: ")
ava = open(a)
for i in ava:
    print(f" {jrk}. {i} ", end="")
    jrk+=1
j = int(input("\nValige laulu järjekorra nr: "))
ava.close()
jrk = 1
ava = open(a)
for i in ava:
    if j==jrk:
        print(f"{i}. {jrk} ", end="")
    jrk+=1
ava.close