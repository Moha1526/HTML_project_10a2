lista1=[2, 6, 9, 12, 34, 6]
'''
#Hossz
print('Simán:')
print(len(lista1))

print('Forral:')
db=0
for i in lista1:
    db=db+1
print(db)

print('Range-el:')
db=0
for i in range(len(lista1)):
    db=db+1
print(db)

print('While-al:')
i=0
db=0
while i<len(lista1):
    db=db+1
    i+=1
print(db)

#Össz
print('Simán:')
print(sum(lista1))

print('Forral:')
ossz=0
for i in lista1:
    ossz=ossz+i
print(ossz)

print('Range-el:')
ossz=0
for i in range(len(lista1)):
    ossz=ossz+lista1[i]
print(ossz)

print('While-al:')
i=0
ossz=0
while i<len(lista1):
    ossz=ossz+lista1[i]
    i+=1
print(ossz)

#Max
print('Simán:')
print(max(lista1))

print('Forral:')
max=0
for i in lista1:
    if max<i:
        max=i
print(max)

print('Range-el:')
max=0
for i in range(len(lista1)):
    if lista1[i]>max:
        max=lista1[i]
print(max)

print('While-al:')
max=0
i=0
while i<len(lista1):
    if max<lista1[i]:
        max=lista1[i]
    i+=1
print(max)

#Min
print('Simán:')
print(min(lista1))

print('Forral:')
min=100
for i in lista1:
    if min>i:
        min=i
print(min)

print('Range-el:')
min=100
for i in range(len(lista1)):
    if lista1[i]<min:
        min=lista1[i]
print(min)

print('While-al:')
min=100
i=0
while i<len(lista1):
    if min>lista1[i]:
        min=lista1[i]
    i+=1
print(min)

#Bekérés ---
szam=input()
if szam in lista1:
    print('A szám benne van a listában!')
else:
    print('A szám nincs benne a listában!')
'''
