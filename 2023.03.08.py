#Majoros Máté
#2023.03.08
#b csoport 

szam_sorozat = [15,4,5,19,]

def eljaras():
    min = szam_sorozat[0]
    max = szam_sorozat[0]
    for szam in szam_sorozat:
        if szam_sorozat < min:
            min = szam
    
        if szam_sorozat > max:
            max = szam
    

    print(f'a listaban levo legkisseb szam {min}')
    print(f'a listaban levo legnagyobb szam {max}')







eljaras()