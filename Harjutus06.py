#George Raatpalu
#27.10.22
#Harjutus06

minu_fail = open("s6pru_l6ustaraamatus.txt", "r")

print(minu_fail.close)


#reformikad
reformikad = 0
kesikud = 0
erakonnad = []
for i in minu_fail.readlines():
    enimi,pnimi,er,palk=i.split(" ")
    if er=="KE":
        kesikud+=1
    if er=="RE":
        reformikad+=1
    if er not in erakonnad:
        erakonnad.append(er)
              
print(f"Reformikaid kokku: {reformikad}")
print(f"Kesikuid kokku: {kesikud}")
print(f"Erakondi kokku: {len(erakonnad)}")


minu_fail = open("reformikad".txt","w")
for nr in range(1,2):







