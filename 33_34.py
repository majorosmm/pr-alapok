#1.1 masodik
'''
valtozo = str(input("adj meg egy szavat!"))
print(valtozo.upper())
'''
#1.2 masodik
'''
lista = ['alma', 'banan', 'korte', 'szölő']
convertalt_lista = [x.upper() for x in lista]
print(convertalt_lista)
'''
#1.3 masodik

'''
lista = ['alma', 'korte', 'banan','fa', 'fű']
lista1 = [elem.upper() for elem in lista if len(elem) > 3]
print(lista)
print(lista1)
'''

#1.4 masodik
'''
lista = ['alma','KÖRTE', 'BaNaN']
lista2 = [elem.swapcase() for elem in lista]
print(lista)
print(lista2)
'''
#1.1 elso
'''
lista = ['fekete', 'fehér', 'barna']

szin = input('Szín: ')
if szin in lista:
    print('A', szin, 'már', 'szerepel a listában:' )
    print(lista)
else:
    print('A', szin, 'még nem', 'szerepel a listában:' )
    print(lista)
'''
#1.2 elso

