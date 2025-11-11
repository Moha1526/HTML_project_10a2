'''
#Try-except forral:
for i in range(5):
    try:
        a=int(input('Kérem a négyzet a oldalát: '))
        print('A négyzet kerülete:', 4*a)
    except:
        print('Nem számot kaptam!')

print('Vége!')

#Try-except while-al:
i=0
while i<5:
    try:
        a=int(input('Kérem a négyzet a oldalát: '))
        print(f'A négyzet kerülete {4*a} .')
        i=5
    except:
        print('Nem számot kaptam!')
        i=i+1

print('Vége!')
'''
#Fájlkezelés:
nb1=[]
file=open("zte.txt")

for i in file:
    i=i.split()
    i[1]=int(i[1])
    i[3]=int(i[3])
    i[5]=int(i[5])
    nb1.append(i)
file.close
print(nb1)

#1. Hány csapat van?
print(f'Az nb1-ben {len(nb1)} csapat van!')

#2. Hány pontja van az összes foci klubnak?
osszeg=0
for i in nb1:
    osszeg=osszeg+i[3]
print(f'Az nb1-es klubboknak {osszeg} pontja van összesen!')

#3. Melyik csapatnak van a legtöbb pontja?
max=0
csap='bb'
for i in nb1:
    if i[3]>max:
        max=i[3]
        csap=i[0]
        
print(f'A legtöbb pontja a {csap} csapatnak lett!')
        
#4. Melyik csapatnak van a legkevesebb pontja?
min=70
csap='bb'
for i in nb1:
    if i[3]<min:
        min=i[3]
        csap=i[0]
        
print(f'A legkevesebb pontja a {csap} csapatnak lett!')

#5. Melyik csapat van a 4. helyen?
csap='bb'
for i in nb1:
    if i[1]==4:
        csap=i[0]

print(f'A {csap} csapat végzett a negyedik helyen!')








