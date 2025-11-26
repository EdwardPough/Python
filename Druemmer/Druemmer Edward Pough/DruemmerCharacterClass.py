#Druemmer Character Class



class character:
    def __init__(self):
        #Main Stats
        self.HP = None #Max = 32
        self.Mana = None #Max = 32
        self.Str = None #Max = 32
        self.Dex = None #Max = 32
        self.Arc = None #Max = 32
        self.Fai = None #Max = 32

    def classwarrior(self): #76 Points
        self.HP = 19
        self.Mana = 5
        self.Str = 24
        self.Dex = 14
        self.Arc = 7
        self.Fai = 9

    def classknight(self): #76 Points
        self.HP = 26
        self.Mana = 5
        self.Str = 18
        self.Dex = 10
        self.Arc = 5
        self.Fai = 12

    def classwizard(self): #76 Points
        self.HP = 10
        self.Mana = 22
        self.Str = 3
        self.Dex = 9
        self.Arc = 22
        self.Fai = 10

    def classcleric(self): #76 Points
        self.HP = 14
        self.Mana = 17
        self.Str = 10
        self.Dex = 9
        self.Arc = 7
        self.Fai = 19