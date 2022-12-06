'''szam1 = int(input("kerek egy egesz szamot:"))
szam2 = int(input("kerek egy masik egesz szamot:"))
if szam1 > szam2:
    print("szam1 nagyobb mint szam2")
if szam2 > szam1:
    print("szam2 nagyobb mint szam1")
if szam1 == szam2:
    print("szam1 megenyezik szam2 vel")'''

#---------------------------------------------------------------

'''szam1 = int(input("kerek egy egesz szamot:"))
szam2 = int(input("kerek egy masik egesz szamot:"))
if szam1 > szam2:
    print("szam1 nagyobb mint szam2")
elif szam2 > szam1:
    print("szam2 nagyobb mint szam1")
elif szam1 == szam2:
    print("szam1 megenyezik szam2 vel")'''

#---------------------------------------------------------------

'''szam1 = int(input("kerek egy egesz szamot:"))
szam2 = int(input("kerek egy masik egesz szamot:"))
if szam1 > szam2:
    print("szam1 nagyobb mint szam2")
elif szam2 > szam1:
    print("szam2 nagyobb mint szam1")
else szam1 == szam2:
    print("szam1 megenyezik szam2 vel")'''

#---------------------------------------------------------------

'''x = None
print(x)
print(type(x))

if x:
    print('do u think none is true?')
elif x is False:
    print('do u think none is false?')
else:
    print('none is not true or false, none is just none')'''

#---------------------------------------------------------------
'''jegy = input("kerek egy osztalyzatot")
    if jegy == 5:
        print('jeles')
    elif jegy == 4:
        print('jó')
    elif jegy == 3:
        print('kozepes')
    elif jegy == 2:
        print('elégséges')
    elif jegy == 1:
        print('elegtelen')
    else:
        print('ez a szám nem egy osztalyzat!')'''

#---------------------------------------------------------------

#bekerek 1 pozitiv egesz szamot és irassuk ki hogy paros vagy paratlan

'''szam = int(input('kerek egy pozitive egesz szamot'))
if szam % 2 == 0:
    print('a szam paros')
else:
    print('a szam paratlan')'''

#----------------------------------------------------------------

'''import random

gondolt_szam = random.randint(1,6)
print('sugok', gondolt_szam)
tipp = input('gondoltam egy szamra tippel meg!')
if tipp == gondolt_szam:
    print('eltalaltad')
else:
    print('nem talaltad el ')'''

#---------------------------------------------------------------

#generaljunk egy szamot 1 es 1000 kozt irassuk ki a szamot ha paros es kissebb mint 500 akkor ha  igaz irja ki hogy szam nem felelt meg a felteleknek.





szam = int(input('adjunk meg egy szamot 1 es 1000 kozott'))
if szam  %2 == 0 and szam <=500:
    print('megfelel') 
else:
    print('nem felel meg')
