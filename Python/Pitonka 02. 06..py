#Fájl kezelés:
'with open -> Nem kell close'

file1=open("elso.txt","r")#Fájl megnyitása
while true:
    sor=file1.readline() #Egy sor beolvasása
    if len(sor)==0
    break
    print(sor)
file1.close #Fájl lezárása
print('vége')
