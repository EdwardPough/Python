#<<<Imports>>>
import random
import inspect

#<<<Liste an Fähigkeiten>>>
#From Mace: Overhead Smash(D), Uppercut(D)
#From Shortsword: Lunge(D)
#From Magicwand: Missile(D), Ice Knife(D), Mana Regen(D)
#From Holysymbol: Heal(D), Light Flash(D), Lower Mana Regen(D)

#<<<Abilities Class>>>
# class abilities():
#     def __init__(self):
#         self.name = ""
#         self.hpcost = 0 #If hp is part of the cost
#         self.mpcost = 0 #If mp is part of the cost
#         self.basedmg = 0 #base value / start value
#         self.baseheal = 0 #base value / start value
#         self.hitchance = 0 #Addidativ
#         self.critchance = 0 #Multiplikator
#         self.strscl = 0 #Scaling A = 14% | B = 8% | C = 6% | D = 4% | E = 2%
#         self.dexscl = 0
#         self.arcscl = 0
#         self.faiscl = 0

#<<<Abilities Class>>>
class abilities():
    def __init__(self):
        self.name = ""
        self.hpcost = 0
        self.mpcost = 0
        self.finaldmg = 0
        self.finalheal = 0
        self.hitchance = 0
        self.critchance = 0
        self.strscl = "" #Scaling A = 14% | B = 8% | C = 6% | D = 4% | E = 2%
        self.dexscl = "" #Scaling A = 14% | B = 8% | C = 6% | D = 4% | E = 2%
        self.arcscl = "" #Scaling A = 14% | B = 8% | C = 6% | D = 4% | E = 2%
        self.faiscl = "" #Scaling A = 14% | B = 8% | C = 6% | D = 4% | E = 2%
        self.function = None #Function of said Ability

#---------------MACE---------------
    def overheadsmash(self, hp, mp, dmg, str, dex, arc, fai, hit, crit, run):
        self.name = "" #For Display in Combat only
        self.hpcost = 0 #For Display in Combat only | Custom Value
        self.mpcost = 3 #For Display in Combat only | Custom Value
        self.finaldmg = 0
        self.finalheal = 0
        self.hitchance = hit + 0 #For Display in Combat only | Weaponhitchance + Custom Value (if over a hundred print guaranteed)
        self.critchance = crit + 50 #For Display in Combat only | Weaponcritchance + Custom Value (if over a hundred print guaranteed)
        self.strscl = 14 # A | Scaling A = 14% | B = 8% | C = 6% | D = 4% | E = 2% | - = 0%
        self.dexscl = 0 # - | Scaling A = 14% | B = 8% | C = 6% | D = 4% | E = 2% | - = 0%
        self.arcscl = 0 # - | Scaling A = 14% | B = 8% | C = 6% | D = 4% | E = 2% | - = 0%
        self.faiscl = 0 # - | Scaling A = 14% | B = 8% | C = 6% | D = 4% | E = 2% | - = 0%
        if run == True:
            self.function = dmg, str, dex, arc, fai, hit, crit = uppercut(dmg, str, dex, arc, fai, self.hitchance, self.critchance, self.strscl, self.dexscl, self.arcscl, self.faiscl) #Function of said Ability
            hp = hp - self.hpcost
            mp = mp - self.mpcost
            return hp, mp, dmg, str, dex, arc, fai, hit, crit

    def uppercut(self, hp, mp, dmg, str, dex, arc, fai, hit, crit, run):
        self.name = "" #For Display in Combat only
        self.hpcost = 0 #For Display in Combat only | Custom Value
        self.mpcost = 3 #For Display in Combat only | Custom Value
        self.finaldmg = 0
        self.finalheal = 0
        self.hitchance = hit + -10 #For Display in Combat only | Weaponhitchance + Custom Value (if over a hundred print guaranteed)
        self.critchance = crit + 0 #For Display in Combat only | Weaponcritchance + Custom Value (if over a hundred print guaranteed)
        self.strscl = 14 # A | Scaling A = 14% | B = 8% | C = 6% | D = 4% | E = 2% | - = 0%
        self.dexscl = 14 # - | Scaling A = 14% | B = 8% | C = 6% | D = 4% | E = 2% | - = 0%
        self.arcscl = 0 # - | Scaling A = 14% | B = 8% | C = 6% | D = 4% | E = 2% | - = 0%
        self.faiscl = 0 # - | Scaling A = 14% | B = 8% | C = 6% | D = 4% | E = 2% | - = 0%
        if run == True:
            self.function = dmg, str, dex, arc, fai, hit, crit = uppercut(dmg, str, dex, arc, fai, self.hitchance, self.critchance, self.strscl, self.dexscl, self.arcscl, self.faiscl) #Function of said Ability
            hp = hp - self.hpcost
            mp = mp - self.mpcost
            return hp, mp, dmg, str, dex, arc, fai, hit, crit

#---------------SHORTSWORD---------------

#<<<MACE>>>
def overheadsmash(dmg, str, dex, arc, fai, hit, crit, strscl, dexscl, arcscl, faiscl): #hp for hp cost or healing | mp for mana cost or regen | dmg for dmg calc | str,dex,arc,fai stats for scaling
    basedmg = 4
    baseheal = 0
    dmg = round((dmg + basedmg) * (1 + (((strscl * (str / 100)/10)) + ((dexscl * (dex / 100)/10)) + ((arcscl * (arc / 100)/10)) + ((faiscl * (fai / 100)/10)))),2)
    if random.randint(1,100) <= crit:
        dmg *= 2
    return dmg, str, dex, arc, fai, hit, crit

def uppercut(dmg, str, dex, arc, fai, hit, crit, strscl, dexscl, arcscl, faiscl): #hp for hp cost or healing | mp for mana cost or regen | dmg for dmg calc | str,dex,arc,fai stats for scaling
    basedmg = 0
    baseheal = 0
    dmg = round((dmg + basedmg) * (1 + (((strscl * (str / 100)/10)) + ((dexscl * (dex / 100)/10)) + ((arcscl * (arc / 100)/10)) + ((faiscl * (fai / 100)/10)))),2)
    if random.randint(1,100) <= crit:
        dmg *= 2
    return dmg, str, dex, arc, fai, hit, crit



#<<<SHORTSWORD>>>
def lunge(hp, mp, dmg, str, dex, arc, fai, hit, crit): #hp for hp cost or healing | mp for mana cost or regen | dmg for dmg calc | str,dex,arc,fai stats for scaling
    hpcost = 0
    mpcost = 2
    basedmg = 3
    baseheal = 0
    hitchance = 20
    critchance = 0
    strscl = 8 #B
    dexscl = 8 #B
    arcscl = 0 #-
    faiscl = 0 #-
    hit = hit + hitchance
    crit = crit + critchance
    hp = hp - hpcost
    mp = mp - mpcost
    dmg = round((dmg + basedmg) * (((strscl * str) / 100) + ((dexscl * dex) / 100) + ((arcscl * arc) / 100) + ((faiscl * fai) / 100)),2)
    if random.randint(1,100) <= crit:
        dmg *= 2
    return hp, mp, dmg, str, dex, arc, fai, hit, crit

#<<<MAGICWAND>>>
def missile(hp, mp, dmg, str, dex, arc, fai, hit, crit): #hp for hp cost or healing | mp for mana cost or regen | dmg for dmg calc | str,dex,arc,fai stats for scaling
    hpcost = 0
    mpcost = 6
    basedmg = 5
    baseheal = 0
    hitchance = 100
    critchance = -100
    strscl = 0 #-
    dexscl = 0 #-
    arcscl = 8 #B
    faiscl = 0 #-
    hit = hit + hitchance
    crit = crit + critchance
    hp = hp - hpcost
    mp = mp - mpcost
    dmg = round((dmg + basedmg) * (((strscl * str) / 100) + ((dexscl * dex) / 100) + ((arcscl * arc) / 100) + ((faiscl * fai) / 100)),2)
    if random.randint(1,100) <= crit:
        dmg *= 2
    return hp, mp, dmg, str, dex, arc, fai, hit, crit

def iceknife(hp, mp, dmg, str, dex, arc, fai, hit, crit): #hp for hp cost or healing | mp for mana cost or regen | dmg for dmg calc | str,dex,arc,fai stats for scaling
    hpcost = 0
    mpcost = 10
    basedmg = 5
    baseheal = 0
    hitchance = -10
    critchance = -100
    strscl = 0 #-
    dexscl = 0 #-
    arcscl = 14 #A
    faiscl = 0 #-
    hit = hit + hitchance
    crit = crit + critchance
    hp = hp - hpcost
    mp = mp - mpcost
    dmg = round((dmg + basedmg) * (((strscl * str) / 100) + ((dexscl * dex) / 100) + ((arcscl * arc) / 100) + ((faiscl * fai) / 100)),2)
    if random.randint(1,100) <= crit:
        dmg *= 2
    return hp, mp, dmg, str, dex, arc, fai, hit, crit

def manaregen(hp, mp, dmg, str, dex, arc, fai, hit, crit): #hp for hp cost or healing | mp for mana cost or regen | dmg for dmg calc | str,dex,arc,fai stats for scaling
    hpcost = 0
    mpcost = -6
    basedmg = 5
    baseheal = 0
    hitchance = 0
    critchance = 0
    strscl = 0 #-
    dexscl = 0 #-
    arcscl = 14 #A
    faiscl = 0 #-
    hit = hit + hitchance
    crit = crit + critchance
    hp = hp - hpcost
    mp = mp - mpcost
    return hp, mp, dmg, str, dex, arc, fai, hit, crit

#<<<Heal>>>
def heal(hp, mp, dmg, str, dex, arc, fai, hit, crit): #hp for hp cost or healing | mp for mana cost or regen | dmg for dmg calc | str,dex,arc,fai stats for scaling
    hpcost = -8
    mpcost = 8
    basedmg = 5
    baseheal = 0
    hitchance = 0
    critchance = 0
    strscl = 0 #-
    dexscl = 0 #-
    arcscl = 14 #A
    faiscl = 0 #-
    hit = hit + hitchance
    crit = crit + critchance
    hp = hp - hpcost
    mp = mp - mpcost
    return hp, mp, dmg, str, dex, arc, fai, hit, crit

def lightflash(hp, mp, dmg, str, dex, arc, fai, hit, crit): #hp for hp cost or healing | mp for mana cost or regen | dmg for dmg calc | str,dex,arc,fai stats for scaling
    hpcost = 0
    mpcost = 4
    basedmg = 5
    baseheal = 0
    hitchance = 0
    critchance = -100
    strscl = 0 #-
    dexscl = 0 #-
    arcscl = 0 #-
    faiscl = 8 #B
    hit = hit + hitchance
    crit = crit + critchance
    hp = hp - hpcost
    mp = mp - mpcost
    dmg = round((dmg + basedmg) * (((strscl * str) / 100) + ((dexscl * dex) / 100) + ((arcscl * arc) / 100) + ((faiscl * fai) / 100)),2)
    if random.randint(1,100) <= crit:
        dmg *= 2
    return hp, mp, dmg, str, dex, arc, fai, hit, crit

def lowermanaregen(hp, mp, dmg, str, dex, arc, fai, hit, crit): #hp for hp cost or healing | mp for mana cost or regen | dmg for dmg calc | str,dex,arc,fai stats for scaling
    hpcost = 0
    mpcost = -3
    basedmg = 5
    baseheal = 0
    hitchance = 0
    critchance = 0
    strscl = 0 #-
    dexscl = 0 #-
    arcscl = 14 #A
    faiscl = 0 #-
    hit = hit + hitchance
    crit = crit + critchance
    hp = hp - hpcost
    mp = mp - mpcost
    return hp, mp, dmg, str, dex, arc, fai, hit, crit

#Variables
run = False

#-------------TESTING FOR CALCULATION FUNCTIONS---------------
# hp = 20
# mp = 30
# dmg = 13.92
# str = 24
# dex = 18
# arc = 22
# fai = 19
# hit = 90
# crit = 5
# print(hp, mp, dmg, str, dex, arc, fai, hit, crit)
# hp, mp, dmg, str, dex, arc, fai, hit, crit = lightflash(hp, mp, dmg, str, dex, arc, fai, hit, crit)
# print(hp, mp, dmg, str, dex, arc, fai, hit, crit)

#-------------TESTING FOR REWORK---------------
#abili = abilities[1]
# run = False
# abi = abilities()
# abimethods = [target for target, method in inspect.getmembers(abilities, predicate=inspect.isfunction)     
#     if not target.startswith("_")]
# #abiindex = abimethods.index(abili)
# currentabi = abimethods[0]
# getattr(abi, currentabi)(hp, mp, dmg, str, dex, arc, fai, hit, crit, run)
# loop = True
# while loop == True:
#     print(dmg)
#     print(f"Costs: HP = {abi.hpcost} | MP = {abi.mpcost}")
#     print(f"Scaling: STR = {abi.strscl}% | DEX = {abi.dexscl}%")
#     print(f"         ARC = {abi.arcscl}% | FAI = {abi.faiscl}%")
#     desc = input("Ja/Nein: ").lower().replace(" ","")
#     if desc == "ja":
#         run = True
#         hp, mp, dmg, str, dex, arc, fai, hit, crit = getattr(abi, currentabi)(hp, mp, dmg, str, dex, arc, fai, hit, crit, run)
#         print(f"You dealt {dmg}")
#         loop = False
#     else:
#         print("Bist zu dumm?")
