import math

szam1 = input('Adj meg egy számot 1-100 között: ')
szam1 = int(szam1)
szam2 = input('Adj meg egy számot 1-100 között: ')
szam2 = int(szam2)
 
kulonbseg = (szam2) - (szam1) 

ak = abs(kulonbseg)
if szam1 == szam2:
    print(' A két szám egyenlő')

if szam1 < szam2:
    print('A két szam nem egyezik!')
    print( szam1, 'kisseb mint', szam2, ak, 'al/el')

if szam1 > szam2:
    print('a két szam nem egyezik!')
    print (szam1, 'nagyobb mint', szam2, ak, 'al/el')

print('vege')

    
    
   
