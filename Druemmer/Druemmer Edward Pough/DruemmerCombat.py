#Druemmer Combat File
#<<<Imports>>>
import random
import DruemmerItemsEquipments
import DruemmerCharacterClass
import DruemmerGameWindow
import inspect
import os #os.system("cls" if os.name == "nt" else "clear")

#Variablen
equips = DruemmerItemsEquipments.equipments
char = DruemmerCharacterClass

#<<<Combat Function>>>
    #Klassen Krieger = 0 | Ritter = 1 | Magier = 2 | Kleriker = 3
def combat(a,b,w,y, hp): #<<< a = enemyrange_a | b = enemyrange_z | w = Raum | x = Gegner | y = Klasse | hp = Current Hitpoints >>>
    #---------Determining Character Class---------
    char_kl = DruemmerCharacterClass.character()
    classmethods = [target for target, method in inspect.getmembers(char.character, predicate=inspect.isfunction)     
        if not target.startswith("_")]
    currentclass = classmethods[y]
    getattr(char_kl, currentclass)()
    #---------Determining Weapon---------
    waffe = DruemmerItemsEquipments.realequipped[0]
    weap = DruemmerItemsEquipments.equipments()
    weapmethods = [target for target, method in inspect.getmembers(equips, predicate=inspect.isfunction)     
        if not target.startswith("_")]
    waffeindex = weapmethods.index(waffe)
    currentweap = weapmethods[waffeindex]
    getattr(weap, currentweap)()
    #---------Determining Sidearm---------
    sidearm = DruemmerItemsEquipments.realequipped[1]
    side = DruemmerItemsEquipments.equipments()
    sidemethods = [target for target, method in inspect.getmembers(equips, predicate=inspect.isfunction)     
        if not target.startswith("_")]
    sideindex = sidemethods.index(sidearm)
    currentside = sidemethods[sideindex]
    getattr(side, currentside)()
    #---------Determining Armor---------
    armor = DruemmerItemsEquipments.realequipped[2]
    arm = DruemmerItemsEquipments.equipments()
    armmethods = [target for target, method in inspect.getmembers(equips, predicate=inspect.isfunction)     
        if not target.startswith("_")]
    armindex = armmethods.index(armor)
    currentarm = armmethods[armindex]
    getattr(arm, currentarm)()
    #---------Choosing Enemy---------
    enemy = enemies()
    enemiesmethods = [target for target, method in inspect.getmembers(enemies, predicate=inspect.isfunction)     
        if not target.startswith("_")]
    enemyrange = random.randint(a, b)
    currentenemy = enemiesmethods[enemyrange]
    getattr(enemy, currentenemy)()
    #---------Combat---------
    while (enemy.hp > 0 and hp > 0) == True:
        os.system("cls" if os.name == "nt" else "clear")
        if enemy.hp > enemy.maxhp:
            enemy.hp = enemy.maxhp
        if hp > char_kl.MaxHP:
            hp = char_kl.MaxHP
        print(enemy.name)
        print(f"{round(enemy.hp,2)}|{enemy.maxhp}")
        edec = random.randint(0,2)
        if edec == 0: #Attacking
            print(f"The {enemy.name} intends on attacking!")
        elif edec == 1: #Defending
            print(f"The {enemy.name} intends on blocking!")
        elif edec == 2: #Dodging and Countering
            print(f"The {enemy.name} is awaiting an attack!")
        print("------------------")
        print(char_kl.name)
        print(f"HP: {hp}|{char_kl.MaxHP}")
        print(f"Mana: {char_kl.Mana}|{char_kl.MaxMana}")
        ent = 0
        while ent == 0:
            print("What will you do?")
            print("1)Attack | 2)Defend | 3)Ability | 4)Item(Not Implemented)")
            pdec = input().lower().replace(" ","")
            if pdec == "attack": #damage calc = weap.base + (weap.base*(((char.str * weap.strscl)/3)/100)) + (weap.base*(((char.dex * weap.dexscl)/3)/100)) + (weap.base*(((char.arc * weap.arcscl)/3)/100)) + (weap.base*(((char.fai * weap.faiscl)/3)/100))
                dmgmain = round(weap.base + (weap.base*(((char_kl.Str * weap.strscl)/3)/100)) + (weap.base*(((char_kl.Dex * weap.dexscl)/3)/100)) + (weap.base*(((char_kl.Arc * weap.arcscl)/3)/100)) + (weap.base*(((char_kl.Fai * weap.faiscl)/3)/100)),2)
                dmgside = round(side.base + (side.base*(((char_kl.Str * side.strscl)/3)/100)) + (side.base*(((char_kl.Dex * side.dexscl)/3)/100)) + (side.base*(((char_kl.Arc * side.arcscl)/3)/100)) + (side.base*(((char_kl.Fai * side.faiscl)/3)/100)),2)
                dmg = round(dmgmain + dmgside/2,2)
                if edec == 0: #Player = Attack | Enemy = Attack
                    enemy.hp -= dmg
                    hp -= enemy.damage
                    print(f"You attacked and dealt {dmg} damage!")
                    print(f"The {enemy.name} attacked and dealt {enemy.damage} damage!")
                    ent = 1
                    input()
                elif edec == 1: #Player = Attack | Enemy = Defend
                    enemy.hp -= dmg - enemy.defense
                    print(f"The {enemy.name} blocked and you only dealt {round(dmg-enemy.defense,2)} damage!")
                    ent = 1
                    input()
                elif edec == 2: #Player = Attack | Enemy = Counter
                    chance = random.randint(1,100)
                    dodge = enemy.dodgechance * 2
                    if dodge >= chance:
                        hp -= enemy.damage
                        print(f"The {enemy.name} dodged your attack and retaliates!")
                        print(f"You take {enemy.damage} damage!")
                        ent = 1
                        input()
                    else:
                        enemy.hp -= dmg
                        print(f"The {enemy.name} is unable to dodge and you hit it for {dmg} damage")
                        ent = 1
                        input()
            elif pdec == "defend": #Player = Defend | Enemy = Attack
                if edec == 0:
                    dmgenm = enemy.damage - arm.basedef
                    if dmgenm < 0:
                        dmgenm = 0
                    hp -= dmgenm
                    print(f"You blocked the attack of the {enemy.name} and only took {dmgenm} damage!")
                    ent = 1
                    input()
                elif edec == 1: #Player = Defend | Enemy = Defend
                    print(f"The {enemy.name} blocked and so did you!")
                    print("Nothing happens...")
                    ent = 1
                    input()
                elif edec == 2: #Player = Defend | Enemy = Counter
                    print(f"You saw through the trick of {enemy.name}!")
                    print("You narrowly avoid its counterattack!")
                    ent = 1
                    input()
            else:
                print("Try again")
        if enemy.hp < 0:
            enemy.hp = 0
        if hp < 0:
            hp = 0
        if enemy.hp == 0:
            print("Ihr habt gesiegt!")
            input()
            return hp
        elif hp == 0:
            return hp
        else:
            pass

#<<<Enemy Ranges>>>
#0-4 Spiders | Spiderling - ???




#<<<Enemy Class>>>
class enemies():
    def __init__(self):
        self.name = ""
        self.hp = 0 #Hit Points des Monsters
        self.maxhp = 0 #Max Hit Points des Monsters
        self.mana = 0 #Mana des Monsters
        self.maxmana = 0 #Max Mana des Monsters
        self.damage = 0 #Schaden den das Monster verursacht
        self.defense = 0 #Rüstungswert des Monster der den Schaden reduziert
        self.dodgechance = 0 #Chance zum Ausweichen
        self.hitchance = 0 #Chance mit einer Attacke zu Treffen
        self.critchance = 0 #Chance auf einen kritischen Treffer

    def aspiderling(self):
        self.name = "Spiderling"
        self.hp = 13 #Hit Points des Monsters
        self.maxhp = 13 #Max Hit Points des Monsters
        self.mana = 3 #Mana des Monsters
        self.maxmana = 3 #Max Mana des Monsters
        self.damage = 5 #Schaden den das Monster verursacht
        self.defense = 3 #Rüstungswert des Monster der den Schaden reduziert
        self.dodgechance = 20 #Chance zum Ausweichen
        self.hitchance = 95 #Chance mit einer Attacke zu Treffen
        self.critchance = 10 #Chance auf einen kritischen Treffer

    def btwoheadedspider(self):
        self.name = "Twoheaded Spider"
        self.hp = 15 #Hit Points des Monsters
        self.maxhp = 15 #Max Hit Points des Monsters
        self.mana = 3 #Mana des Monsters
        self.maxmana = 3 #Max Mana des Monsters
        self.damage = 7 #Schaden den das Monster verursacht
        self.defense = 5 #Rüstungswert des Monster der den Schaden reduziert
        self.dodgechance = 10 #Chance zum Ausweichen
        self.hitchance = 90 #Chance mit einer Attacke zu Treffen
        self.critchance = 20 #Chance auf einen kritischen Treffer

    def cbroodmother(self):
        self.name = "Broodmother"
        self.hp = 46 #Hit Points des Monsters
        self.maxhp = 46 #Max Hit Points des Monsters
        self.mana = 3 #Mana des Monsters
        self.maxmana = 3 #Max Mana des Monsters
        self.damage = 2 #Schaden den das Monster verursacht
        self.defense = 0 #Rüstungswert des Monster der den Schaden reduziert
        self.dodgechance = 0 #Chance zum Ausweichen
        self.hitchance = 85 #Chance mit einer Attacke zu Treffen
        self.critchance = 0 #Chance auf einen kritischen Treffer

#Testing
#combat(0,2,0,3)
