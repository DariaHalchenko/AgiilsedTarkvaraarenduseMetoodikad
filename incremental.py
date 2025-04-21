class Patsient:
    def __init__(self, nimi, vanus):
        self.nimi = nimi
        self.vanus = vanus
        self.regAeg = ""
Patsient1 = Patsient("Thomas", 77)

class Haigla:
    patsiendiList = []
    arstideList = []
    def patsienditeKuuvamine(self):
        for index,elem in enumerate(self.patsiendiList):
            print('id: ', index, "Nimi: ", elem.nimi, "Vanus: ", elem.vanus)
    def arstideeKuuvamine(self):
        for index,elem in enumerate(self.arstideList):
            print('id: ', index, "Nimi: ", elem.nimi, "Vanus: ", elem.vanus)
    def kohtumineTegimine(self):
        patsiendiIndex = 0
        patsientiNimi = input("sisesta patsientiNimi: ")
        arstiNimi = input("Sisesta arsti nimi: ")
        for elem in self.patsiendiList:
            if elem.nimi == patsientiNimi:
                patsiendiIndex = self.patsiendiList.index(elem)

        for elem in self.arstideList:
            if elem.nimi == arstiNimi and len(elem.aeg) > 0:
                self.patsiendiList[patsiendiIndex].regAeg = elem.aeg[0]
        for elem in self.patsiendiList:
            print("Nimi: ", elem.nimi, "aeg: ", elem.regAeg)

class Arst:
    def __init__(self, nimi, vanus, eriala, aeg):
        self.nimi = nimi
        self.vanus = vanus
        self.eriala = eriala
        self.aeg = aeg

Patsient2 = Patsient("Piter", 27)
Arst1 = Arst("Muhamad", 25, "allergoloog", ['10:00', '11:00', '12:00'])

haigla = Haigla()
haigla.patsiendiList.append(Patsient1)
haigla.patsiendiList.append(Patsient2)
haigla.arstideList.append(Arst1)
haigla.patsienditeKuuvamine()
haigla.arstideeKuuvamine()
haigla.kohtumineTegimine()
