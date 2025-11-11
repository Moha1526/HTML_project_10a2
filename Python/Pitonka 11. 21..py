'''
#Dobókocka
import random
num=random.randint(1,6)
print(num)

#Kockapóker
import random
for i in range(5):
    num=random.randint(1,6)
    print(num)

#3 dobás, ki a nyertes?
#Feladat: Tomi és Peti 3-at dob, dobásukat összegezzük, és nézzük meg ki is nyert!
print('Tamás dobása:')
import random
össz1=0
for i in range(3):
    num1=random.randint(1,6)
    print(num1)
    össz1=össz1+num1
print('Tamás összpontszáma:', össz1)

print('Péter dobása:')
import random
össz2=0
for i in range(3):
    num2=random.randint(1,6)
    print(num2)
    össz2=össz2+num2
print('Péter összpontszáma:', össz2)

if össz1>össz2:
    print('Tamás nyert!')
elif össz1==össz2:
    print('Döntetlen lett!')
else:
    print('Péter nyert!')

#Függvénnyel leírva:
import random
ossz=0
def dobas(ossz):
    for i in range(3):
        num=random.randint(1,6)
        ossz=ossz+num
    return(ossz)

tossz=dobas(ossz)
possz=dobas(ossz)

print('Tamás',(tossz),'dobot!')
print('Péter',(possz),'dobot!')
'''


      
