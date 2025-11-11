'''
#Háromszög kerülete:
a=float(input('Kérem a háromszög a oldalát:'))
b=float(input('Kérem a háromszög b oldalát:'))
c=float(input('Kérem a háromszög c oldalát:'))

def harom(a,b,c):
    kerület=a+b+c
    return kerület

print('Háromszög kerülete:',harom(a,b,c))

#Téglalap kerülete ---:
a=float(input('Kérem a téglalap a oldalát:'))
b=float(input('Kérem a téglalap b oldalát:'))

def téglalap(a,b):
    ker=2*(a+b)
    return ker
    
print('A téglalap kerülete:', (téglalap(a,b)[1]))

#Téglalap területe ---:
a=float(input('Kérem a téglalap a oldalát:'))
b=float(input('Kérem a téglalap b oldalát:'))

def téglalap(a,b):
    ter=a*b
    return ter

print('A téglalap területe:', (téglalap(a,b)[1]))

#Négyzet kerülete, területe ---:
a=float(input('Kérem a négyzet oldalát:'))

def negy(a):
    ker=4*a
    ter=a*a
    return negy
print('A négyzet kerülete, területe:',negy(a)[0])

#Téglatest térfogata, felszín:

a=float(input('Kérem a téglatest a oldalát:'))
b=float(input('Kérem a téglatest b oldalát:'))
c=float(input('Kérem a téglatest c oldalát:'))


def téglatest(a,b,c):
    f=2*(a*b+b*c+a*c)
    t=a*b*c
    return f,t

print('A téglatest felszíne:', (téglatest(a,b,c)[0]))
print('A téglatest térfogata:', (téglatest(a,b,c)[1]))

r=float(input('Kérem a kör sugarát:'))
pi=3.14

def kör(r,pi):
    ker=2*r*pi
    ter=r*r*pi
    return ker, ter

print('A kör területe, kerülete:', kör(r,pi)[0])
'''
