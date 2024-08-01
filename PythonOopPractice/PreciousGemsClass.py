class PreciousGems:
    gems = []
    count = 0

    def __init__(self, name):
        self.name = name
        PreciousGems.count += 1
        if PreciousGems.count <= 5:
            PreciousGems.gems.append(self)
        else:
            PreciousGems.gems.pop(0)
            PreciousGems.gems.append(self)

    def myGemCollection(self):
        for gem in PreciousGems.gems:
            print(gem.name, end = ' ')
        print()

preciousGems1 = PreciousGems('Ruby')
preciousGems1.myGemCollection()

preciousGems2  = PreciousGems("Emerald")
preciousGems3  = PreciousGems("Sapphire")
preciousGems4  = PreciousGems("Diamond")
preciousGems5  = PreciousGems("Amber")
preciousGems5.myGemCollection()

preciousGems6 = PreciousGems("Onyx")
preciousGems6.myGemCollection()

preciousGems7  = PreciousGems("Diamond")
preciousGems8  = PreciousGems("Diamond")
preciousGems9  = PreciousGems("Diamond")
preciousGems10  = PreciousGems("Diamond")
preciousGems10.myGemCollection()
preciousGems11  = PreciousGems("Diamond")
preciousGems11.myGemCollection()