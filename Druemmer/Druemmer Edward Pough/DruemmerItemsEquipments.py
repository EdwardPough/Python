#<<<Imports>>>
import DruemmerCharacterClass
import inspect

#<<<Variablen>>>
char = DruemmerCharacterClass
cha = DruemmerCharacterClass.character()

#<<<Funktionen>>>
def damagecalc(y): #x = Equipped Item aus Inventory | y = Klassenwahl aus Combat (Variable = y)
    #---------Determining Character Class---------
    char_kl = DruemmerCharacterClass.character()
    classmethods = [target for target, method in inspect.getmembers(char.character, predicate=inspect.isfunction)     
        if not target.startswith("_")]
    currentclass = classmethods[y]
    getattr(char_kl, currentclass)()
    #---------Damage Calculation---------


def defensecalc():
    pass

#<<<---------Everything regarding Items and Equipments--------->>>
#<<<Equipments>>>
class equipments():
    def __init__(self):
        self.name = ""
        self.slot = ""
        self.strw = "" #Scaling A = 14% | B = 8% | C = 6% | D = 4% | E = 2%
        self.strscl = 0
        self.dexw = ""
        self.dexscl = 0
        self.arcw = ""
        self.arcscl = 0
        self.faiw = ""
        self.faiscl = 0
        self.ability1 = ""
        self.abiltiy2 = ""
        self.ability3 = ""

    def amace(self):                #Starter Weapon Warrior | Nummer 0
        self.name = "Mace"
        self.slot = "Main"
        self.strw = "A"
        self.strscl = 14
        self.dexw = "C"
        self.dexscl = 6
        self.arcw = "-"
        self.arcscl = 0
        self.faiw = "-"
        self.faiscl = 0
        self.ability1 = "Overhead Smash"
        self.abiltiy2 = "Upper Cut"
        self.ability3 = ""

    def bshortsword(self):          #Starter Weapon Knight | Nummer 1
        self.name = "Shortsword"
        self.slot = "Main"
        self.strw = "B"
        self.strscl = 8
        self.dexw = "C"
        self.dexscl = 6
        self.arcw = "-"
        self.arcscl = 0
        self.faiw = "-"
        self.faiscl = 0
        self.ability1 = "Lunge"
        self.abiltiy2 = ""
        self.ability3 = ""

    def cmagicwand(self):          #Starter Weapon Wizard | Nummer 2
        self.name = "Magic Wand"
        self.slot = "Side"
        self.strw = "E"
        self.strscl = 2
        self.dexw = "E"
        self.dexscl = 2
        self.arcw = "B"
        self.arcscl = 8
        self.faiw = "-"
        self.faiscl = 0
        self.ability1 = "Missile"
        self.abiltiy2 = "Dagger"
        self.ability3 = "ManaRegen"

    def dholysymbol(self):          #Starter Weapon Cleric | Nummer 3
        self.name = "Holy Symbol"
        self.slot = "Side"
        self.strw = "E"
        self.strscl = 2
        self.dexw = "E"
        self.dexscl = 2
        self.arcw = "-"
        self.arcscl = 0
        self.faiw = "B"
        self.faiscl = 8
        self.ability1 = "Heal"
        self.abiltiy2 = "Lightflash"
        self.ability3 = "LowerManaRegen"

#<<<Items>>>
class items():
    def __init__(self):
        self.name = ""



#<<<---------Everything regarding Inventory--------->>>
equipped = []
inventory = []


print(equipments().name)