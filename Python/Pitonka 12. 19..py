'''
lista1=[45, 7, 22, 31, 3, 8]

#Darabszám
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
db=0
i=0
while i<len(lista1):
    db=db+1
    i+=1
print(db)

#Összeg
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
ossz=0
i=0
while i<len(lista1):
    ossz=ossz+lista1[i]
    i+=1
print(ossz)

#Maximum
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
    if max<lista1[i]:
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

#Minimum
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
    if min>lista1[i]:
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

#Feladat -> Ne legyen benne 2x a 3 és az 5
lst=[3,5,8,2,1,3,5]

aa=[]
for i in lst:
    if i not in aa:
        aa.append(i)
print(aa)

a=set(lst)
print(a)
lst1=list(a)
print(lst1)
'''
