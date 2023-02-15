
"""lista = [2, 5, 4, 8, 19, 11, 10, 12]

talalat = False
index = 0
while not talalat:
        if lista[index] % 3 == 0:
            talalat = True
        index = index + 1

print('A hárommal osztható szám indexe a listában: ', index-1)
    
  """


"""
lista = ['kék', 'zöld', 'piros', 'fehér']

talalat = False
index = 0
while index < len(lista) and not talalat:
        if lista[index] == 'piros':
            talalat = True
        index = index + 1

if talalat:
        print('Van a listában piros szín, az indexe: ', index-1)
else:
        print('Nincs a listában piros szín.')
        """

lista1 = [2, 5, 4, 8, 9, 11, 10, 12]
lista2 = ['kék', 'zöld', 'piros', 'fehér']
lista3 = [2, 5, 4, 8, 9, 11, 10, 12]


def eldontes_tetele(lista_eldontes):
    talalat = False
    index = 0
    while index < len(lista_eldontes) and not talalat:
        if lista_eldontes[index] % 3 == 0:
            talalat = True
        index = index + 1
    
    if talalat:
        print('Van a listában hárommal osztható szám.')
    else:
        print('Nincs a listában hárommal osztható szám.')

def kereses_tetele(lista_kereses):
    talalat = False
index = 0
while index < len(lista_kereses) and not talalat:
        if lista_kereses[index] == 'piros':
            talalat = True
        index = index + 1

if talalat:
        print('Van a listában piros szín, az indexe: ', index-1)
else:
        print('Nincs a listában piros szín.')

def kivalasztas_tetele(lista_kivalasztas):
    talalat = False
index = 0
while not talalat:
        if lista_kivalasztas[index] % 3 == 0:
            talalat = True
        index = index + 1

print('A hárommal osztható szám indexe a listában: ', index-1)


kivalasztas_tetele(lista3)
kereses_tetele(lista2)
eldontes_tetele(lista1)

