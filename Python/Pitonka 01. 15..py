
#Fájl adatok listába
nb1=[]
file= open("zte.txt")

for i in file:
    i=i.split()
    i[1]=int(i[1])
    i[3]=int(i[3])
    i[5]=int(i[5])
    nb1.append(i)
file.close()
print(nb1)

#Hány csapat van?
print(f'Az nb1-ben {len(nb1)} csapat van!')

#Mennyi az összpontszám?
osszeg=0
for i in nb1:
    osszeg=osszeg+i[3]

print(f'Az nb1-es csapatoknak {osszeg} pontja van')

#Melyik csapatnak van a legtöbb pontja?
max=0
csap='dd'

for i in nb1:
    if i[3]>max:
        max=i[3]
        csap=i[0]

print(f'Az első {csap}')

#Melyik csapatnak van a legkevesebb pontja?
min=100
csap='dd'

for i in nb1:
    if i[3]<min:
        min=i[3]
        csap=i[0]

print(f'Az utolsó {csap}')

#Ki van a negyedik helyen?









