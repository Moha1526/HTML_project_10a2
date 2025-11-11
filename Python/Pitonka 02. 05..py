#DEF-es feladatocskák
'''
#Feladat 1
def vmi():
    a=int(input('Kérek egy számot:'))
    print('A négyszerese:', a*4)
vmi()        

#Feladat 2
def vmi2():
    a=int(input('Kérem a téglalap a oldalát'))
    b=int(input('Kérem a téglalap b oldalát'))
    ker=a*2+b*2
    ter=a*b
    print(f'A téglalap kerülete:', ker)
    print(f'A téglalap területe:', ter)
vmi2()

#Feladat 3
a=input()
b=input()

def vmi3:
    ker=2*a+2*b
    ter=a*b
    return(ker,ter)

print('A téglalap kerülete', vmi3(a,b)[0])
print('A téglalap területe', vmi3(a,b)[1])
'''
#Számok kiküszöbölése: NO negative, NO another character
'''

#Feladat 4
szam=int(input('Kérek egy számot:'))

i=0
while i<5:
    if szam<0:
        print('Negatív számot kaptál, próbáld újra!')
        i+=1
    else:
        print('A szám négyszerese:',4*szam)
    i+=1

#Feladat 5
i=0
while i<5:
    try:
        szam=int(input('Kérek egy számot:'))
        print('A szám négyszerese:', szam*4)
    except:
        print('Nem számot kaptam, próbáld újra!')
    i+=1
'''
