#Napi homerseklet max,min (march22-april20 Emöd)
#A program globalis valtozoi:
napi_maximum = (14,17,21,15,16,13,8,11,12,14,16,16,14,15,13,14,16,16,14,12,12,10,11,13,15,17,19,17,19,20)
napi_minimum = (8,8,9,6,7,1,0,2,3,5,4,4,3,5,4,6,8,6,4,2,1,-1,-1,1,3,5,7,5,7,9)
napi_minimum_db = None
napi_maximum_db = None
#1.feladat hany db min/max ertek van a listákban?

def napimaxdb(napi_maximum_fv):
    darab = 0
    for szam in napi_maximum_fv:
            darab = darab + 1
            napi_maximum_db = darab
    return darab

print(f'A napi max elemszáma: {napimaxdb(napi_maximum)}')

def napimindb(napi_minimum_fv):
    darab = 0
    for szam in napi_minimum_fv:
            darab = darab + 1
            napi_minimum_db =  darab
    return darab

print(f'A napi min elemszáma: {napimaxdb(napi_minimum)}')

#2.feladat max/min atlag

def napimaxatlag(napi_maximum_fv):
    lista_elemeinek_osszege = 0
    for szam in napi_maximum_fv:
            lista_elemeinek_osszege = lista_elemeinek_osszege + szam
    lista_elemeinek_osszege = lista_elemeinek_osszege / len(napi_maximum_fv)
    return lista_elemeinek_osszege
print(f'A napi max atlag {napimaxatlag(napi_maximum)}')

def napiminatlag(napi_minimum_fv):
    lista_elemeinek_osszege = 0
    for szam in napi_minimum_fv:
            lista_elemeinek_osszege = lista_elemeinek_osszege + szam
    lista_elemeinek_osszege = lista_elemeinek_osszege / len(napi_minimum_fv)
    return lista_elemeinek_osszege
print(f'A napi min atlag {napiminatlag(napi_minimum)}')

#3a.feladat 30 napos atlag homerseklet

print(f'a harmincnapos atlag homerseklet erteke : {(napimaxatlag(napi_maximum)+ napiminatlag(napi_minimum)) / 2}')

#3.b 30 napos napiatlag



