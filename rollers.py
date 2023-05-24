class Eroller:
    def __init__(self, marka, seb, telj) -> None:
        self.marka = marka #szöveg
        self.maxseb = int(seb) #egész szám, a maximális sebesség km/h -ban
        self.teljesitmeny = int(telj) #a teljesítmény Watt-ban

    def ToString(self):
        kimenet = f"A roller márkája: {self.marka}\n"
        kimenet += f"maximális sebessége: {self.maxseb} km/h\n"
        kimenet += f"teljesítménye: {self.teljesitmeny}"
        return kimenet

    def szovegbe_ki(self):
        kimeneti_szoveg = ""
        while True:
            user_be = input("Adj meg egy entert ha ki szeretnél lépni!")
            kimeneti_szoveg += user_be + "\n"
           
            if user_be == "":
                break
            print(kimeneti_szoveg)
            
