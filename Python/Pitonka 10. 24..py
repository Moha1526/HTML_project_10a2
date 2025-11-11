#2024.10.24.
'''
lista1=[4,3,4,5,1,13,5,6]

#Lista kiíratása 3 féle képpen:
print('1:')
for i in lista1:
    print(i)

print('2:')
for i in range(len(lista1)):
    print(lista1[i])

print('3:-')
def prt1():
    i=0
    while i<len(lista1):
        i=i+1
        print(lista1)
prt1()

#Darabszám:
print('1:')
print(len(lista1))

print('2:')
db=0
for i in lista1:
    db=db+1
print(db)

print('3:')
db=0
for i in range(len(lista1)):
    db=db+1
print(db)

print('4:')
def prt2():
    db=0
    i=0
    while i<len(lista1):
        db=db+1
        i=i+1
    print(db)
prt2()

#Sum(összeg)
print('1:')
print(sum(lista1))

print('2:')
ossz=0
for i in lista1:
    ossz=ossz+i
print(ossz)

print('3:')
ossz=0
for i in range(len(lista1)):
    ossz=ossz+lista1[i]
print(ossz)

print('4:')
def prt3():
    ossz=0
    i=0
    while i<len(lista1):
        ossz=ossz+lista1[i]
        i=i+1
    print(ossz)
prt3()

#Maximum
print('1:')
print(max(lista1))

print('2:')
max=0
for i in lista1:
    if max<i:
        max=i
print(max)

print('3:')
max=0
for i in range(len(lista1)):
    if lista1[i]>max:
        max=lista1[i]
print(max)

print('4:-')
'''
