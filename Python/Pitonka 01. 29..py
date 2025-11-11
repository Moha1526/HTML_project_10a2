'''
#Ismétlés - Try és except
i=0
while i<5:
    try:
        a=int(input('Kérem a négyzet a oldalát:'))
        print('A négyzet kerülete:', 4*a)
        i=5
    except:
        print('Nem számot kaptam, írd be újra!')
        i+=1
'''   
#Szótár -> név, életkor, helyszín
my_dict={'név':'Anna', 'kor':25, 'város':'Budapest'}
my_dict2=dict(név='Bence', kor=30, város='Pécs')

print(my_dict)
print(my_dict2)
print(my_dict['név'])
print(my_dict['kor'])
print(my_dict2['név'])
print(my_dict2['kor'])

#-HIBA: print(my_dict['ország'])-#
print(my_dict.get('ország', 'Nem elérhető'))

my_dict={'név':'Anna', 'kor':26}
print(my_dict)
my_dict={'név':'Timi', 'kor':19}
print(my_dict)

my_dict['város']='Budapest'
print(my_dict)

my_dict['kor']=20
print(my_dict)
my_dict['város']='Keszthely'
print(my_dict)

del my_dict['kor']
print(my_dict)

del my_dict['város']
print(my_dict)
város = my_dict.pop('város')
print(my_dict)
print(város)

my_dict={'név':'Anna', 'kor':25, 'város':'Budapest'}
for i in my_dict:
    print(i)

#Szöveg -> Hány szóbol áll?

szöveg='alma körte alma szilva alma körte'
szavak=szöveg.split()
print(szavak)
szótár={}
for szó in szavak:
    szótár[szó]=szótár.get(szó, 0)+1

print(szótár)







