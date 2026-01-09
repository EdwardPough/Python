#Druemmer Character Class



class character:
    def __init__(self):
        #Main Stats
        self.name = None
        self.hp = None #Max = 32
        self.MaxHP = None #Max = 32
        self.Mana = None #Max = 32
        self.MaxMana = None #Max = 32
        self.Str = None #Max = 32
        self.Dex = None #Max = 32
        self.Arc = None #Max = 32
        self.Fai = None #Max = 32

    def aclasswarrior(self): #76 Points
        self.name = "Krieger"
        self.hp = 19
        self.MaxHP = 19
        self.Mana = 5
        self.MaxMana = 5
        self.Str = 24
        self.Dex = 14
        self.Arc = 7
        self.Fai = 9

    def bclassknight(self): #76 Points
        self.name = "Ritter"
        self.hp = 26
        self.MaxHP = 26
        self.Mana = 5
        self.MaxMana = 5
        self.Str = 16
        self.Dex = 12
        self.Arc = 5
        self.Fai = 12

    def cclasswizard(self): #76 Points
        self.name = "Magier"
        self.hp = 10
        self.MaxHP = 10
        self.Mana = 22
        self.MaxMana = 22
        self.Str = 3
        self.Dex = 9
        self.Arc = 22
        self.Fai = 10

    def dclasscleric(self): #76 Points
        self.name = "Kleriker"
        self.hp = 14
        self.MaxHP = 14
        self.Mana = 17
        self.MaxMana = 17
        self.Str = 10
        self.Dex = 9
        self.Arc = 7
        self.Fai = 19