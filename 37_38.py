# Szélso ertek meghatarozása. (Minimum, Maximum)

lista = [12, 5, 4, 8, 9, 11, 10, 12, 6]
print(min(lista))
print(max(lista))

def szelsoertek_10c(munka_lista):
    min = munka_lista[0]
    max = munka_lista[0]

    for szam in lista:
        if szam < min:
            min = szam
        if szam > max:
            max = szam

    print(f'a legkisseb szam  {min}')
    print(f'a legnagyobb szam  {max}')

szelsoertek_10c(lista)