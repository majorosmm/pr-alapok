

from encodings import utf_8


forrasfajl = open('szoveg.txt')

for sor in forrasfajl:
    print(sor)
forrasfajl.close()


print('----------------------------------')

forrasfajl = open('szoveg.txt')
for sor in forrasfajl:
    sor = sor.strip()
    print(sor)
    forrasfajl.close

print('----------------------------------')


with open('szoveg.txt', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        print(f'{sor}' )

print('----------------------------------')

with open('kimenet.txt', 'w', encoding='utf-8') as celfajl:
    print('asdasddsds33', file=celfajl)

