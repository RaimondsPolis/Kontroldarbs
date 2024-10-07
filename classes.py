class dators:
    def __init__(self, nosaukums, skaits, tips, cena):
        self.name = nosaukums
        self.count = skaits
        self.type = tips
        self.price = cena
    def info(self):
        return "{}, {}, {}, {}".format(self.name, self.count, self.type, self.price)
    def DatorsNopirkts(self):
        self.count -=1
    def Piegade(self):
        self.count +=1


class Detala():

    def __init__(self, nosaukums, razotajs, skaits, tips, cena):
        self.name = nosaukums
        self.count = skaits
        self.type = tips
        self.price = cena
        self.producer = razotajs
    
    def DatorsNopirkts(self):
        self.count -=1
    def Piegade(self):
        self.count +=1
    def info1(self):
        return "{}, {}, {}, {}, {}".format(self.name, self.producer, self.count,
        self.type, self.price)