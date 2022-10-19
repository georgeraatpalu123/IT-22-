#George Raatpalu
#17.10.22
#Harjutus04
import random


#Pank
konto = 10000
intress = 0.05
periood = 5

for i in range(1,periood+1):
    print(f"{i} {konto} {round(konto*intress,2)} {round(konto+konto*intress,2)}")
    konto = konto+konto*intress
print(f"Konto seiss: {round(konto,2)}")
print(f"kasum: {round(konto-10000,2)}")




#Arvamismäng
#loop = 1
#skoor = 0
#while loop==1:
    #suvarv = random.randint(1,10)
    #print(suvarv)
    #for i in rage(3):
        #valik = int(input("Vali arv 1-10: "))
        #if valik ==a:
            #print("WINNER!")
                #skoor+=1
                #break
            #else:
                #print("WRONG!")
        #loop= int(input("Veel (1/0)? "))
#print("GAME OVER")
#print(f"Skoor {skoor}")

#Viisikud
for i in range(1,101):
    if i%5==0:
        print(i)






#Pisike korrutustabel
arv = 5
for i in range(1,11):
    summa = arv * i
    print(f"{arv}X{i}={summa}")


        



#Paaris ja Paaritu
for i in range(1,11):
    if i%2==0:        
        print(i,"paaris")
    else:
        print(i,"paaritu")




#loto
for i in range(5):
    suv = random.randint(0,9)
    print(suv, end="")


#tärnid
arv = 1
for i in range (5):
    print("* " * 5)
    arv = arv + 1
    arv -= 1
nr=5
for i in range (5):
    print("* " * 5)
    


#jalka
vanus=16
sugu = "m"


if vanus>16 and vanus<=18 and sugu=="m":
     print("sobib meeskonda")
else:
        print("ei sobi")
#juubel
sp = "09.08.2006"
aasta =  2022
p,k,a =sp.split(".")
vanus = aasta-int(a)


if vanus%5==0:
    print("juubel")
else:
    print("print ei ole juubel")
    
    
 
 
 
#myyk
hind = 9
if hind<=10:
    ale = 0.1
else:
     ale:0.2
summa = hind-hind*ale    
print(f"Summa: {summa}€")




