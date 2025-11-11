'''
#Gyakorló feladat - Try és except
i=0
while i<5:
    try:
        a=int(input('Kérem az a oldalát:'))
        print('Az oldal fele:', a/2)
        i=5
    except:
        print('Nem számot kaptam!')
        i+=1

#Listás feladatok -> Darabszám
lista1=(2, 76, 93, 43, 27, 3, 8)

print('Simán:')
print(len(lista1))

print('Forral:')
db=0
for i in lista1:
    db=db+1
print(db)

print('While-al:')
i=0
db=0
while i<len(lista1):
    db=db+1
    i+=1
print(db)

#-> Összeg
print('Simán:')
print(sum(lista1))

print('Forral:')
osszeg=0
for i in lista1:
    osszeg=osszeg+i
print(osszeg)

print('While-al')
i=0
osszeg=0
while i<len(lista1):
    osszeg=osszeg+lista1[i]
    i+=0
print(osszeg)

#-> Maximum
print('Simán:')
print(max(lista1))

print('Forral:')
max=0
for i in lista1:
    if max<i:
        max=i
print(max)

print('While-al:')
i=0
max=0
while i<len(lista1):
    if max<lista1[i]:
        max=lista1[i]
    i+=1
print(max)

#-> Minimum
print('Simán:')
print(min(lista1))

print('Forral:')
min=100
for i in lista1:
    if min>i:
        min=i
print(min)

print('While-al:')
min=100
i=0
while i<len(lista1):
    if min>lista1[i]:
        min=lista1[i]
    i+=1
print(min)
'''
