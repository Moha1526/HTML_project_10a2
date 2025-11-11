
#Fájlkezelés
form=[]
file=open("f1.txt")

for i in file:
    i=i.split()
    i[2]=int(i[2])
    i[4]=int(i[4])
    i[6]=int(i[6])
    form.append(i)
file.close
print(form)

#1. Melyik versenyzőnek van a legtöbb győzelme:
max=0
nev="mmm"
for i in form:
    if i[2]>max:
        max=i[2]
        nev=1[0]
        
print(nev)

#2. Verstappennek hány pontja van összesen:
print(f'{form[0][0]} {(form[0][2]*3)+(form[0][4]*2)+(form[0][6]*1)} pontot szerzett!')

#3. Mennyi pontja van az összes versenyzőnek:
pont=[]
for i in form:
    print('f{i[0]} {(i[2]*3)+(i[4]*2)+(i[6]*1)} pontot szerzett!')
    pont.append((i[2]*3)+(i[4]*2)+(i[6]*1))

p=0

for i in range(len(pont)):
    if pont[i]>p:
        p=pont[i]
        n=i

print(form[n][0])

#4. Hány csapat van összesen:
csap=[]
for i in form:
    if i[1] not in csap:
        csap.append(i[1])
        
print(csap)

#5. Hány csapat győzött:
cspo=0
csp=[]
for n in csap:
    for i in form:
        if n==i[1]:
            cspo=cspo+i[2]
    csp.append(cspo)
    cspo=0

print(csp)
























        
