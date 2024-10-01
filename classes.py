class dators:
    def __init__(self, nosaukums, skaits, tips, cena):
        self.name = nosaukums
        self.count = skaits
        self.type = tips
        self.price = cena

    def info(self):
        return "{}, {}, {}, {}".format(self.name, self.count, self.type, self.price)
    

    

