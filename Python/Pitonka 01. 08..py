'''
#Ismétlés - négyzet kerület, terület
print('Adja meg a négyzet a oldalát!')
a=int(input())
ker=4*a
ter=a*a
print(f'A négyzet kerülete', {ker})
print(f'A négyzet területe', {ter})

if ker>ter:
    print('A kerület nagyobb!')
elif ker<ter:
    print('A terület nagyobb!')
else:
    print('Egyenlőek!')

#Try és except parancs:

for i in range(5):
    try:
        a=int(input('Kérem az a oldalt:'))
        print('A négyzte kerülete', 4*a)
    except:
        print('Nem számot kaptam!')

i=0
while i<len(range(7)):
    try:
        a=int(input('Kérem az a oldalt:'))
        print('A négyzet kerülete', 4*a)
    except:
        print('Nem számot kaptam!')
    i+=1

#Darabszám ismétlése
lista1=[2, 6, 5, 6, 7]

print(len(lista1))

db=0
for i in lista1:
    db=db+1
print(i)

db=0
for i in range(len(lista1)):
    db=db+1
print(i)

i=0
db=0
while i<len(lista1):
    db=db+1
    i+=0
print(i)

#Maximum, minimum:

max=0
for i in lista1:
    if i<max:
        max=i
print(max)

min=100
for i in lista1:
    if i>min:
        min=i
print(min)

#Random szám
import random
szám=random.randint(1,6)
print('A szám a következő:',szám)
'''



































    
    
