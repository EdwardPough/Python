#<<<Imports>>>
import DruemmerCharacterClass
import inspect

#<<<Variablen>>>
char = DruemmerCharacterClass
cha = DruemmerCharacterClass.character()

#<<<Funktionen>>>
# def damagecalc(y): #x = Equipped Item aus Inventory | y = Klassenwahl aus Combat (Variable = y)
#     #---------Determining Character Class---------
#     char_kl = DruemmerCharacterClass.character()
#     classmethods = [target for target, method in inspect.getmembers(char.character, predicate=inspect.isfunction)     
#         if not target.startswith("_")]
#     currentclass = classmethods[y]
#     getattr(char_kl, currentclass)()
#     #---------Damage Calculation---------


# def defensecalc():
#     pass

#<<<---------Everything regarding Items and Equipments--------->>>
#<<<Equipments>>>
class equipments():
    def __init__(self):
        self.name = ""
        self.slot = 0 #Main = 0 | Side = 1 | Armor = 2 |
        self.base = 0
        self.hit = 0 #From 0 - 100
        self.crit = 0 #From 0 - 100
        self.strw = "" #Scaling A = 14% | B = 8% | C = 6% | D = 4% | E = 2%
        self.strscl = 0
        self.dexw = ""
        self.dexscl = 0
        self.arcw = ""
        self.arcscl = 0
        self.faiw = ""
        self.faiscl = 0
        self.ability1 = ""
        self.ability2 = ""
        self.ability3 = ""

    def amace(self):                #Starter Weapon Warrior | Nummer 0
        self.name = "Mace"
        self.slot = 0 #Main
        self.base = 5
        self.hit = 90
        self.crit = 5
        self.strw = "A"
        self.strscl = 14
        self.dexw = "C"
        self.dexscl = 6
        self.arcw = "-"
        self.arcscl = 0
        self.faiw = "-"
        self.faiscl = 0
        self.ability1 = "Overhead Smash"
        self.ability2 = "Upper Cut"
        self.ability3 = ""
        self.type = "weap"

    def bshortsword(self):          #Starter Weapon Knight | Nummer 1
        self.name = "Shortsword"
        self.slot = 0 #Main
        self.base = 5
        self.hit = 90
        self.crit = 10
        self.strw = "B"
        self.strscl = 8
        self.dexw = "C"
        self.dexscl = 6
        self.arcw = "-"
        self.arcscl = 0
        self.faiw = "-"
        self.faiscl = 0
        self.ability1 = "Lunge"
        self.ability2 = ""
        self.ability3 = ""
        self.type = "weap"

    def cmagicwand(self):          #Starter Weapon Wizard | Nummer 2
        self.name = "Magicwand"
        self.slot = 0 #Main
        self.base = 2
        self.hit = 90
        self.crit = 0
        self.strw = "E"
        self.strscl = 2
        self.dexw = "E"
        self.dexscl = 2
        self.arcw = "B"
        self.arcscl = 8
        self.faiw = "-"
        self.faiscl = 0
        self.ability1 = "Missile"
        self.ability2 = "Dagger"
        self.ability3 = "ManaRegen"
        self.type = "weap"

    def dholysymbol(self):          #Starter Weapon Cleric | Nummer 3
        self.name = "Holysymbol"
        self.slot = 0 #Main
        self.base = 2
        self.hit = 90
        self.crit = 0
        self.strw = "E"
        self.strscl = 2
        self.dexw = "E"
        self.dexscl = 2
        self.arcw = "-"
        self.arcscl = 0
        self.faiw = "B"
        self.faiscl = 8
        self.ability1 = "Heal"
        self.ability2 = "Lightflash"
        self.ability3 = "LowerManaRegen"
        self.type = "weap"

    def edagger(self):          #Starter Weapon Everyone
        self.name = "Dagger"
        self.slot = 1 #Side
        self.base = 2
        self.hit = 90
        self.crit = 10
        self.strw = "B"
        self.strscl = 8
        self.dexw = "C"
        self.dexscl = 6
        self.arcw = "-"
        self.arcscl = 0
        self.faiw = "-"
        self.faiscl = 0
        self.ability1 = ""
        self.ability2 = ""
        self.ability3 = ""
        self.type = "weap"

    def fhalfplate(self):          #Starter Armor Knight | Nummer 1
        self.name = "Halfplate"
        self.slot = 2 #Armor
        self.basedef = 7
        self.type = "arm"

    def gchainmail(self):          #Starter Armor Warrior | Nummer 1
        self.name = "Chainmail"
        self.slot = 2 #Armor
        self.basedef = 5
        self.type = "arm"

    def hleatherarmor(self):          #Starter Armor Wizard/Cleric | Nummer 1
        self.name = "Leatherarmor"
        self.slot = 2 #Armor
        self.basedef = 3
        self.type = "arm"
        
#<<<Items>>>
class items():
    def __init__(self):
        self.name = ""



#<<<---------Everything regarding Inventory--------->>>
equipped = []
realequipped = []
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
    equipped.pop(newslot)
    equipped.insert(newslot, x.capitalize())
    # for i in range(len(equipmethods)):
    #     cequ = equipments()
    #     curequip = equipmethods[i]
    #     getattr(cequ, curequip)()
    #     oldslot = cequ.slot
    #     if oldslot == newslot:
    #         realequipped.pop(oldslot)
    #         realequipped.insert(newslot, newequip)
    realequipped.pop(newslot)
    realequipped.insert(newslot, newequip)

def info(x): # X = fake equipment
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
    if equ.type == "weap":
        print(f"Name: {equ.name}")
        print(f"Strength: {equ.strw}")
        print(f"Dexterity: {equ.dexw}")
        print(f"Arcane: {equ.arcw}")
        print(f"Faith: {equ.faiw}")
        print(f"Abilities: {equ.ability1}, {equ.ability2}, {equ.ability3}")
    else:
        print(f"Name: {equ.name}")
        print(f"Defense: {equ.basedef}")
