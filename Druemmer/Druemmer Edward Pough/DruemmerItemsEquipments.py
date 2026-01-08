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
        self.slot = 0 #Main = 0 | Side = 1 | Armor = 2 |
        self.base = 0
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
        self.slot = 0 #Main
        self.base = 5
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
        self.slot = 0 #Main
        self.base = 5
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
        self.name = "MagicWand"
        self.slot = 1 #Side
        self.base = 2
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
        self.name = "HolySymbol"
        self.slot = 1 #Main
        self.base = 2
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

    def edagger(self):          #Starter Weapon Everyone
        self.name = "Dagger"
        self.slot = 0 #Main
        self.base = 2
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

    def fhalfplate(self):          #Starter Armor Knight | Nummer 1
        self.name = "Halfplatearmor"
        self.slot = 2 #Armor
        self.basedef = 7

    def gchainmail(self):          #Starter Armor Warrior | Nummer 1
        self.name = "chainmail"
        self.slot = 2 #Armor
        self.basedef = 5

    def hleatherarmor(self):          #Starter Armor Wizard/Cleric | Nummer 1
        self.name = "leatherarmor"
        self.slot = 2 #Armor
        self.basedef = 3
        

#<<<Items>>>
class items():
    def __init__(self):
        self.name = ""



#<<<---------Everything regarding Inventory--------->>>
equipped = []
realequipped = [2]
inventory = []

def equip_real(x): # X = fake equipment
    equ = equipments()
    equipmethods = [target for target, method in inspect.getmembers(equipments, predicate=inspect.isfunction)     
        if not target.startswith("_")]
    a = None
    for i in range(len(equipmethods)):
        a = str(equipmethods[i])
        strlist = list(a)
        strlist.pop(0)
        test = "".join(strlist).lower().replace(" ","")
        if test == x:
            a = str(equipmethods[i])
            break
        else:
            pass
    c = equipmethods.index(a)
    newequip = equipmethods[c]
    getattr(equ, newequip)()
    newslot = equ.slot
    equipped.pop(0)
    equipped.insert(0, x.capitalize())
    # for i in range(len(equipmethods)):
    #     cequ = equipments()
    #     curequip = equipmethods[i]
    #     getattr(cequ, curequip)()
    #     oldslot = cequ.slot
    #     if oldslot == newslot:
    #         realequipped.pop(oldslot)
    #         realequipped.insert(newslot, newequip)
    realequipped.insert(newslot, newequip)
