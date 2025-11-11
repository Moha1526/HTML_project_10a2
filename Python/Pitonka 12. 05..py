'''
#String létrehozása

szoveg="Phyton programozás"

#Hozzáférés karakterekhez

elso karakter=szoveg[0] #Első karakter: "P"
utolso karakter=szoveg[-1] #Utolsó karakter: "s"

#Szöveg hosszának meghatározása

hossz=len(szoveg) #Hossz: 18

#Kis- és nagybetűk átalakítása

kisbetus=szoveg1.lower() #Kisbetűs változat: "phyton"
nagybetus=szoveg2.upper() #Nagybetűs változat: "PHYTON"

#Karakterek cseréje:

modositott=szoveg1.replace("P","J") #Módosított szöveg: "Jhyton"

#Szöveg darabolása szavakra

mondat="Tanuljuk*a*Phyton*programozást"
szavak=mondat.split("*") #["Tanuljuk","a","Phyton","programozást"]


csapat=" Zte 10 hely 13 pont 5 győzelem"
csapat[0]=csapat[0].upper()
csapat[1]=int(csapat[1])-2
csapat[3]=int(csapat[3])+2
csapat[5]=int(csapat[5])+2

print(csapat)

fcsapat=" Vte 6 hely 20 pont 7 győzelem"
fcsapat[0]=fcsapat[0].lower()
fcsapat[1]=int(fcsapat[1])+3
fcsapat[3]=int(fcsapat[3])-10
fcsapat[5]=int(fcsapat[5])-2

print(fcsapat)
'''

