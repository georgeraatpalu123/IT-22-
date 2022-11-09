#George Raatpalu
#Python is.töö 1
#02.11.22

#tervituss
print("Tere, maailm")

#Aasta liblikas
aasta = 2020
liblikas = ("teelehe-moosaiikliblikas")
lause_keskosa = ("aasta liblikas on")
lause=str(aasta)+lause_keskosa+liblikas
print(lause)

#Pilved

a = input("pilvede alus")
print(a)


#Bussid
input("inimeste arv")
kohad = int(input("Kohtade arv: "))
busse_vaja = (inimesed/kohad)
print(f"Busse on vaja {math.coil(busse_vaja)}")
jaak = inimesed%kohad
if jaak==0:
    print("viimases bussis on inimesi {kohad}")
else: print("viimases bussis on inimesi {jaak}")




a=int(input("Tõuse ja sära "))
for i in range(a):
    print("Tõuse ja sära")
      
      
#Täringud
a=int(input("Sisestage täringute arv" ))

    
      
      




#Male
nisuterad=0.5
a=int(input("Sisetage täisarv "))
i = 0
while i <a:
    i += 1
    
nisuterad*=2
print(nisuterad)

    





fail = open("rebased.txt",encoding="UTF-8")

vastuvoetud=[]
for rida in fail:
aastad = [2011,2012,2013,2014,2015,2016,2017,2018,2019]
    vastuvoetud.append(int(rida))
aasta = int(input("Mis aastat tahad? "))
index = aastad 

print(vastuvoetud[index])


          
