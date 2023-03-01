def eldontes_tetele():
            
        lista = [2, 5, 4, 8, 9, 11, 10, 12]
        
        talalat = False
        index = 0
        while index < len(lista) and not talalat:
            if lista[index] % 3 == 0:
                talalat = True
            index = index + 1
        
        if talalat:
            print('Van a listában hárommal osztható szám.')
        else:
            print('Nincs a listában hárommal osztható szám.')

        
            
    
def kereses_tetele():
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
        
        
        


def kivalasztas_tetele():

        lista = [2, 5, 4, 8, 9, 11, 10, 12]

        talalat = False
        index = 0
        while not talalat:
                if lista[index] % 3 == 0:
                    talalat = True
                index = index + 1

        print('A hárommal osztható szám indexe a listában: ', index-1)
    
        

def osszegzes_tetele():
    napi_ertekesitesek = [3, 12, 3, 4, 7, 15, 1]

    osszesen = 0
    for ertekesites in napi_ertekesitesek:
            osszesen = osszesen + ertekesites

    print("A héten ennyi értékesítés történt: ", osszesen)
    

def szamlalas_tetele():
    lista = [12, 5, 4, 8, 9, 11, 10, 12, 6]

    darab = 0
    for szam in lista:
            if szam % 3 == 0:
                darab = darab + 1

    print('A listában lévő hárommal osztható számok száma: ', darab)
    

def szelsoertek_tetele():
    lista = [12, 5, 4, 8, 9, 11, 10, 12, 6]

    min = lista[0]
    max = lista[0]
    for szam in lista:
            if szam < min:
                min = szam
            if szam > max:
                max = szam

    print('A legkisebb szám a listában: ', min)
    print('A legnagyobb szám a listában: ', max)  

    
while True:
    print("eldontes - 1")
    print("kereses - 2")
    print("kivalasztas - 3")
    print("osszegzes - 4")
    print("szamlalas - 5")
    print("szelsoertek -6")
    
    szam = int(input("add meg az egyik program szamat!"))
    if szam == 1:
        eldontes_tetele()
    if szam == 2:
        kereses_tetele()
    if szam == 3:
        kivalasztas_tetele()
    if szam == 4:
        osszegzes_tetele()
    if szam == 5:
         szamlalas_tetele()
    if szam == 6:
        szelsoertek_tetele()
    elif szam == 0:
        break
        
