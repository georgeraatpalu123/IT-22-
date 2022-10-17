#George Raatpalu
#11.10.22
#harjutus03



#palindroom





#tundide ajad
algus = "8:30"
lopp = "14:15"

hh1,mm1 = algus.split(":")
minutid1 = int(hh1)*60+int(mm1)
hh2,mm2 = lopp.split(":")
minutid2 = int(hh2)*60+int(mm2)

minutid = minutid2-minutid1 # ajavahe
hh = minutid//60#täisarvuline jagamine
mm = minutid%60#jääk



print(f"Ajaline vahe on {hh}:{mm}")














#emaili kontroll true/false
email = input ("sisesta email kontrollimisks; ")
print("@" in email)




#vandumine - teksti sisestamine 
v = input("Vannu sia 'Kurat küll!': ")
print(v.replace("kurat","*****"))


nimi=input("sisesta nimi: ")
puh_nimi = nimi.strip().capitalize()
print("Tere,", puh_nimi+"!")










