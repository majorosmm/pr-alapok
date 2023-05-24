import rollers
ujRoller = rollers.Eroller("Akai F10",25,250)
print(ujRoller.ToString())


roller_nev = input(f"add meg a roller nevét: ")
roller_seb = input(f"add meg a roller sebességét: ")
roller_telj = input(f"add meg a roller teljesitmenet: ")

eroller1 = rollers.Eroller(roller_nev,roller_seb,roller_telj)
print(eroller1.ToString())

eroller1.szovegbe_ki()


rollerek = []
ujNev = " "
while ujNev != "":
    ujNev = input("Kérem, adja meg a következő roller márkáját: ")
    if ujNev != "":
            ujSeb = input("Kérem, adja meg a roller maximális sebességét: ")
            ujTelj = input("Kérem, adja meg a roller teljesítményét: ")
            rollerek.append(rollers.Eroller(ujNev,ujSeb,ujTelj))
            print('Sikeres rögzítés')
with open('tobbmint500.txt', 'w', encoding='utf-8') as kimenet:
    for roller in rollerek:
        if roller.teljesitmeny > 500:
            kimenet.write(f"{roller.marka}\n")