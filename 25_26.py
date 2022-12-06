Lista = ["alma", "banán", "cseresznye"]
print(Lista)

#-----------------------------------------------------------------

Lista = ["alma", "banán", "cseresznye", "alma", "banán"]
print(Lista)

#-----------------------------------------------------------------

Lista = ["alma", "banán", "cseresznye"]
print(len(Lista))

#-----------------------------------------------------------------

lista1 = ["alma", "banán", "cseresznye"]
lista2 = [1, 5, 7, 9, 3]
lista3 = [True, False, False]
print(lista1)
print(lista2)
print(lista3)

#-----------------------------------------------------------------

lista1 = ["abc", 34, True, 40, "férfi"]
print(lista1)

#-----------------------------------------------------------------

lista5 = ["alma", "banán", "cseresznye"]
print(type(lista5))

#-----------------------------------------------------------------

lista = list(("alma", "banán", "cseresznye"))
print(lista)

#-----------------------------------------------------------------

lista = ["alma", "banán", "cseresznye"]
print(lista[1])

#-----------------------------------------------------------------

lista = ["alma", "banán", "cseresznye"]
print(lista[-1])

#-----------------------------------------------------------------

lista = ["alma-0", "banan-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mango-6"]
print(lista[2:5])
print(lista[1:6])

#-----------------------------------------------------------------

lista = ["alma-0", "banan-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mango-6"]
print(lista[:4])

#-----------------------------------------------------------------

lista = ["alma-0", "banan-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mango-6"]
print(lista[2:])

#-----------------------------------------------------------------

lista = ["alma-0", "banan-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mango-6"]
print(lista[-4:-1])
 
#-----------------------------------------------------------------

lista = ["alma-0", "banan-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mango-6"]
if "banan-1" in lista:
    print("igen banan-1 szerepel a listaba")

#-----------------------------------------------------------------

lista = ["alma-0", "banan-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mango-6"]
if "banan" not in lista:
    print("igen banan elem nem szerepel a listaban")

#-----------------------------------------------------------------

lista = ["alma-0", "banan-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mango-6"]
lista[1] = 'kivi'
print(lista)

#-----------------------------------------------------------------

lista = ["alma-0", "banan-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mango-6"]
lista[1:3] = ['körte', 'szilva']
print(lista)

#-----------------------------------------------------------------

lista = ["alma-0", "banan-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mango-6"]
lista[1:2] = ['körte', 'szilva']
print(lista)

#-----------------------------------------------------------------

lista = ["alma-0", "banan-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mango-6"]
lista[1:3] = ['körte']
print(lista)

#-----------------------------------------------------------------

lista = ["alma-0", "banan-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mango-6"]
lista.insert(2,"körte")
print(lista)

#-----------------------------------------------------------------

lista = ["alma", "banán", "cseresznye"]
lista.append("körte")
print(lista)