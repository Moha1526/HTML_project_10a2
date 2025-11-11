#2024. 11. 13.
'''
#Hol van a ...
lista1=[3, 5, 1, 12, 5, 8, 1]

hely=0
for i in lista1:
    hely=hely+1
    if i==5:
        print(hely)

#Négyzet-terület kerület
a=5
b=6

def feladat(a,b):
    print('A téglalap kerülete', 2*a+2*b)
    print('A négyzet kerülete', 4*a)
feladat(a,b)

#Feladat ,,return" parancs
a=5
b=6

def feladat(a,b):
    ker=2*a+2*b
    return(ker)

print('A téglalap kerülete',feladat(a,b))
'''
#Téglalap területe-kerülete
a=5
b=6

def feladat(a,b):
    ker=2*a+2*b
    ter=a*b
    return(ker, ter)

print('A téglalap kerülete', feladat(a,b)[0])
print('A téglalap területe', feladat(a,b)[1])

if feladat(a,b)[0]>feladat(a,b)[1]:
    print('A kerület a nagyobb.')
else:
    print('A terület a nagyobb.')





