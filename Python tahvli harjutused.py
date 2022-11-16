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
import random
x=int(input("Täringute arv "))
täring1 = random.randint(1, 6)
täring2 = random.randint(1, 6)
täring3 = random.randint(1, 6)
täring4 = random.randint(1, 6)
täring5 = random.randint(1, 6)
print(täring1,2,3,4,5)

    
      
      




#Male
nisuterad=0.5
a=int(input("Sisetage täisarv "))
i = 0
while i <a:
    i += 1
    
nisuterad*=2
print(nisuterad)

    




#Ülikooli vastuvõetud
fail = open("rebased.txt",encoding="UTF-8")

vastuvoetud=[]
for rida in fail:
aastad = [2011,2012,2013,2014,2015,2016,2017,2018,2019]
    vastuvoetud.append(int(rida))
aasta = int(input("Mis aastat tahad? "))
index = aastad 
print(vastuvoetud[index])



#Jänesed      2.1, 2,2, 2,5
Porgandid=2
a=int(input("Sisestage ringide arv "))
i = 0
while i <a:
    #i += 1
    
Porgandid*=6
print(Porgandid)



#Sissetulekud
f = open("konto.txt")
for line in f
    if re.search("^[0-9]",-line):
         print(line,end="")
        
        
        
#Jukebox
x=input("Millist mussi tahate? " )
file=open(x)
for rida in file:
    print(rida)


print("Osta ja sa ei kahetse!")
a=(int(input("Mitu korda soovite reklaamlauset kuvada? ")))
b=input("Mida soovite kuvada ")
for i in range(a):
    print(b.upper())
    
    
#Õunamahla tegemine

def mahlapakkide_arv(a):
    a = round(a*0.4/3)
    return a
c=float(input("Sisestage õunte kogus kilogrammides: "))
print(mahlapakkide_arv(c))
       
       
#Peo eelarve        
c=int(input("Mitu inimest on kutsutud? "))
x=int(input("Mitu inimest tuleb? "))
def eelarve(a):
    b=a*10+55
    return b

print(eelarve(c))
print(eelarve(x))


#Tervitused mõtisklusega
def tervitus(a):
        print('"Võõrustaja:"Tere!"')
        print(f"Täna {a}.kord tervitada,mõtiskleb võõrustaja")
        print('"Külaline:"Tere,suur tänu kutse eest!"')
x=int(input("Sisestage külaliste arv"))        
for i in range(x):
    tervitus(i+1)
    
#   
def minu(a):
    input("Sisesta kuupäeva kujul ")   
kuud = ["","jaan,"veeb"]
    return kuud[a]
#kuupäev
def ilus(b):
    print(f"11.{u} 2022")
kp=input"Lisa kp:")
p,k,a=kp.split(".")
ilus(minu(int(k)))


        




    








          
