'''
#Pitagoras-tétel:
import math
print('Kérem a háromszög a oldalát:')
a=int(input())
print('Kérem a háromszög b oldalát:')
b=int(input())
c=math.sqrt(math.pow(a,2)+math.pow(b,2))
print('A háromszög c oldala:', c)

#Try, except
i=False
while i!=True:
    try:
        a=int(input('Kérem a háromszög a oldalát'))
        b=int(input('Kérem a háromszög b oldalát'))
        i=True
    except:
        print('Nem számot kaptam')

#Magasság-tétel:
import math
print('Kérem a háromszög p részét:')
p=int(input())
print('Kérem a háromszög q részét:')
q=int(input())
m=math.sqrt(p*q)
print('A háromszög magassága:', m)

#Befogó-tétel:
import math
print('Kérem a háromszög c oldalát:')
c=int(input())
print('Kérem a háromszög p részét:')
p=int(input())
b=math.sqrt(c*p)
print('A háromszög b oldala:', b)
'''
