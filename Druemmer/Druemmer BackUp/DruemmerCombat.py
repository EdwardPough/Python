#Druemmer Combat File
#<<<Imports>>>
import random
import DruemmerItemsEquipments
import DruemmerCharacterClass
import DruemmerAbilities
import DruemmerGameWindow
import inspect
import os #os.system("cls" if os.name == "nt" else "clear")

#Variablen
equips = DruemmerItemsEquipments.equipments
char = DruemmerCharacterClass
abi = DruemmerAbilities

#<<<Combat Function>>>
    #Klassen Krieger = 0 | Ritter = 1 | Magier = 2 | Kleriker = 3
def combat(a,b,y,hp,mp): #<<< a = enemyrange_a | b = enemyrange_z | w = Raum | x = Gegner | y = Klasse | hp = Current Hitpoints | mp = Current Manapoints >>>
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
        if enemy.hp > enemy.maxhp:
            enemy.hp = enemy.maxhp
        if hp > char_kl.MaxHP:
            hp = char_kl.MaxHP
        if mp > char_kl.MaxMana:
            mp = char_kl.MaxMana
        hitchance = random.randint(1,100) #damage calc = weap.base + (weap.base*(((char.str * weap.strscl)/3)/100)) + (weap.base*(((char.dex * weap.dexscl)/3)/100)) + (weap.base*(((char.arc * weap.arcscl)/3)/100)) + (weap.base*(((char.fai * weap.faiscl)/3)/100))
        critchance = random.randint(1,100)
        dmgmain = round(weap.base + (weap.base*(((char_kl.Str * weap.strscl)/3)/100)) + (weap.base*(((char_kl.Dex * weap.dexscl)/3)/100)) + (weap.base*(((char_kl.Arc * weap.arcscl)/3)/100)) + (weap.base*(((char_kl.Fai * weap.faiscl)/3)/100)),2)
        dmgside = round(side.base + (side.base*(((char_kl.Str * side.strscl)/3)/100)) + (side.base*(((char_kl.Dex * side.dexscl)/3)/100)) + (side.base*(((char_kl.Arc * side.arcscl)/3)/100)) + (side.base*(((char_kl.Fai * side.faiscl)/3)/100)),2)
        dmg = round(dmgmain + dmgside/2,2)
        if critchance <= weap.crit:
            dmg *= 2
        ent1 = 0
        while ent1 == 0:
            os.system("cls" if os.name == "nt" else "clear")
            print(enemy.name)
            print(f"{round(enemy.hp,2)}|{enemy.maxhp}")
            edec = random.randint(1,3)
            if edec == 1: #Attacking
                print(f"The {enemy.name} intends on attacking!")
            elif edec == 2: #Defending
                print(f"The {enemy.name} intends on blocking!")
            elif edec == 3: #Dodging and Countering
                print(f"The {enemy.name} is awaiting an attack!")
            print("------------------")
            print(char_kl.name)
            print(f"HP: {hp}|{char_kl.MaxHP}")
            print(f"Mana: {mp}|{char_kl.MaxMana}")
            print("What will you do?")
            print("1)Attack | 2)Defend | 3)Ability | 4)Item(Not Implemented)")
            pent = 0
            pdec = input().lower().replace(" ","")
            if pdec == "attack" or pdec == "1":
                pent = 1
            elif pdec == "defend" or pdec == "2":
                pent = 2
            elif pdec == "ability" or pdec == "3":
                pent = 3
            else:
                print("Try again")
            if pent != 0:
                descloop = True
                while descloop:
                    situation = pent + 5*(edec)
                    match situation:
                        #<<< Player Attacking>>>
                        #Player = Attack 1 + Enemy = Attack 5 = 6
                        case 6:
                            hp -= enemy.damage
                            if hitchance <= weap.hit:
                                enemy.hp -= dmg
                                if critchance <= weap.crit:
                                    print("You critically hit the enemy!")
                                print(f"You attacked and dealt {dmg} damage!")
                                print(f"The {enemy.name} attacked and dealt {enemy.damage} damage!")
                                input()
                                descloop = False
                                ent1 = 1
                            else:
                                print("You missed!")
                                print(f"The {enemy.name} attacked and dealt {enemy.damage} damage!")
                                input()
                                descloop = False
                                ent1 = 1
                        #Player = Attack 1 + Enemy = Defend 10 = 11
                        case 11:
                            if hitchance <= weap.hit:
                                enemy.hp -= dmg - enemy.defense
                                if critchance <= weap.crit:
                                    print("You critically hit the enemy!")
                                print(f"The {enemy.name} blocked and you only dealt {round(dmg-enemy.defense,2)} damage!")
                                input()
                                descloop = False
                                ent1 = 1
                            else:
                                print("You missed!")
                                print(f"The {enemy.name} blocked and you only dealt {round(dmg-enemy.defense,2)} damage!")
                                input()
                                descloop = False
                                ent1 = 1
                        #Player = Attack 1 + Enemy = Counter 15 = 16
                        case 16:
                            if hitchance <= weap.hit:
                                chance = random.randint(1,100)
                                dodge = enemy.dodgechance * 2
                                if dodge >= chance:
                                    hp -= enemy.damage
                                    print(f"The {enemy.name} dodged your attack and retaliates!")
                                    print(f"You take {enemy.damage} damage!")
                                    input()
                                    descloop = False
                                    ent1 = 1
                                else:
                                    enemy.hp -= dmg
                                    if critchance <= weap.crit:
                                        print("You critically hit the enemy!")
                                    print(f"The {enemy.name} is unable to dodge and you hit it for {dmg} damage")
                                    input()
                                    descloop = False
                                    ent1 = 1
                            else:
                                print("You missed!")
                                hp -= enemy.damage
                                print(f"The {enemy.name} dodged your attack and retaliates!")
                                print(f"You take {enemy.damage} damage!")
                                input()
                                descloop = False
                                ent1 = 1
                        #<<< Player Defending>>>
                        #Player = Defend 2 + Enemy = Attack 5 = 7
                        case 7:
                            dmgenm = enemy.damage - arm.basedef
                            if dmgenm < 0:
                                dmgenm = 0
                            hp -= dmgenm
                            print(f"You blocked the attack of the {enemy.name} and only took {dmgenm} damage!")
                            input()
                            descloop = False
                            ent1 = 1
                        #Player = Defend 2 + Enemy = Defend 10 = 12
                        case 12:
                            print(f"The {enemy.name} blocked and so did you!")
                            print("Nothing happens...")
                            input()
                            descloop = False
                            ent1 = 1
                        #Player = Defend 2 + Enemy = Counter 15 = 17
                        case 17:
                            print(f"You saw through the trick of {enemy.name}!")
                            print("You narrowly avoid its counterattack!")
                            input()
                            descloop = False
                            ent1 = 1
                        #<<< Player Using Ability>>>
                        #Player = Ability 3 + Enemy = Attack 5 = 8
                        case 8:
                            y = 1
                            while y == 1:
                                hitti = weap.hit
                                critti = weap.crit
                                os.system("cls" if os.name == "nt" else "clear")
                                desc = input(f"Which Ability: ({weap.ability1}|{weap.ability2}|{weap.ability3} or Back?) ").lower().replace(" ","")
                                if desc == weap.ability1.lower().replace(" ","") or desc == weap.ability2.lower().replace(" ","") or desc == weap.ability3.lower().replace(" ",""):    
                                    run = False
                                    abi = DruemmerAbilities.abilities()
                                    abimethods = [target for target, method in inspect.getmembers(DruemmerAbilities.abilities, predicate=inspect.isfunction)     
                                        if not target.startswith("_")]
                                    abiindex = abimethods.index(desc)
                                    currentabi = abimethods[abiindex]
                                    getattr(abi, currentabi)(hp, mp, dmg, char_kl.Str, char_kl.Dex, char_kl.Arc, char_kl.Fai, weap.hit, weap.crit, run)
                                    loop = True
                                    while loop == True:
                                        print(f"Effect: {abi.effect}")
                                        print(f"Costs: HP = {abi.hpcost} | MP = {abi.mpcost}")
                                        print(f"Scaling: STR = {abi.strscl}% | DEX = {abi.dexscl}%")
                                        print(f"         ARC = {abi.arcscl}% | FAI = {abi.faiscl}%")
                                        desc = input("1)Yes | 2)No | 3)Back: ").lower().replace(" ","")
                                        if desc == "yes" or desc == "1":
                                            if abi.mpcost <= mp:
                                                run = True
                                                hpcheck = hp
                                                mpcheck = mp
                                                hp, mp, dmg, char_kl.Str, char_kl.Dex, char_kl.Arc, char_kl.Fai, weap.hit, weap.crit = getattr(abi, currentabi)(hp, mp, dmg, char_kl.Str, char_kl.Dex, char_kl.Arc, char_kl.Fai, weap.hit, weap.crit, run)
                                                hp -= enemy.damage
                                                if hp > hpcheck:
                                                    print(f"You regenerated {hp-hpcheck} Health!")
                                                    print(f"The {enemy.name} attacked and dealt {enemy.damage} damage!")
                                                    input()
                                                    descloop = False
                                                    ent1 = 1
                                                elif mp > mpcheck:
                                                    print(f"You regenerated {mp-mpcheck} Mana!")
                                                    print(f"The {enemy.name} attacked and dealt {enemy.damage} damage!")
                                                    input()
                                                    descloop = False
                                                    ent1 = 1
                                                else:
                                                    if hitchance <= weap.hit:
                                                        enemy.hp -= dmg
                                                        if critchance <= weap.crit:
                                                            print("You critically hit the enemy!")
                                                        print(f"You attacked and dealt {dmg} damage!")
                                                        print(f"The {enemy.name} attacked and dealt {enemy.damage} damage!")
                                                        input()
                                                        descloop = False
                                                        ent1 = 1
                                                    else:
                                                        print("You missed!")
                                                        print(f"The {enemy.name} attacked and dealt {enemy.damage} damage!")
                                                        input()
                                                        descloop = False
                                                        ent1 = 1
                                                weap.hit = hitti
                                                weap.crit = critti
                                                y = 0
                                                loop = False
                                            else:
                                                print("You don't have enough mana!")
                                                loop = False
                                                input()
                                        elif desc == "no" or desc == "2":
                                            loop = False
                                        elif desc == "back"  or desc == "3":
                                            y = 0
                                            loop = False
                                        else:
                                            print("Try again")
                                            input()
                                elif desc == "back":
                                    y = 0
                                    descloop = False
                                else:
                                    print("Try again")
                                    input()
                        #Player = Ability 3 + Enemy = Defend 10 = 13
                        case 13:
                            y = 1
                            while y == 1:
                                hitti = weap.hit
                                critti = weap.crit
                                os.system("cls" if os.name == "nt" else "clear")
                                desc = input(f"Which Ability: ({weap.ability1}|{weap.ability2}|{weap.ability3} or Back?) ").lower().replace(" ","")
                                if desc == weap.ability1.lower().replace(" ","") or desc == weap.ability2.lower().replace(" ","") or desc == weap.ability3.lower().replace(" ",""):    
                                    run = False
                                    abi = DruemmerAbilities.abilities()
                                    abimethods = [target for target, method in inspect.getmembers(DruemmerAbilities.abilities, predicate=inspect.isfunction)     
                                        if not target.startswith("_")]
                                    abiindex = abimethods.index(desc)
                                    currentabi = abimethods[abiindex]
                                    getattr(abi, currentabi)(hp, mp, dmg, char_kl.Str, char_kl.Dex, char_kl.Arc, char_kl.Fai, weap.hit, weap.crit, run)
                                    loop = True
                                    while loop == True:
                                        print(f"Effect: {abi.effect}")
                                        print(f"Costs: HP = {abi.hpcost} | MP = {abi.mpcost}")
                                        print(f"Scaling: STR = {abi.strscl}% | DEX = {abi.dexscl}%")
                                        print(f"         ARC = {abi.arcscl}% | FAI = {abi.faiscl}%")
                                        desc = input("1)Yes | 2)No | 3)Back: ").lower().replace(" ","")
                                        if desc == "yes" or desc == "1":
                                            if abi.mpcost <= mp:
                                                run = True
                                                hpcheck = hp
                                                mpcheck = mp
                                                hp, mp, dmg, char_kl.Str, char_kl.Dex, char_kl.Arc, char_kl.Fai, weap.hit, weap.crit = getattr(abi, currentabi)(hp, mp, dmg, char_kl.Str, char_kl.Dex, char_kl.Arc, char_kl.Fai, weap.hit, weap.crit, run)
                                                if hp > hpcheck:
                                                    print(f"You regenerated {hp-hpcheck} Health!")
                                                    print(f"The {enemy.name} blocked nothing!")
                                                    input()
                                                    descloop = False
                                                    ent1 = 1
                                                elif mp > mpcheck:
                                                    print(f"You regenerated {mp-mpcheck} Mana!")
                                                    print(f"The {enemy.name} blocked nothing!")
                                                    input()
                                                    descloop = False
                                                    ent1 = 1
                                                else:
                                                    if hitchance <= weap.hit:
                                                        enemy.hp -= dmg
                                                        if critchance <= weap.crit:
                                                            print("You critically hit the enemy!")
                                                        print(f"You attacked and dealt {dmg} damage!")
                                                        print(f"The {enemy.name} blocked and you only dealt {round(dmg-enemy.defense,2)} damage!")
                                                        input()
                                                        descloop = False
                                                        ent1 = 1
                                                    else:
                                                        print("You missed!")
                                                        print(f"The {enemy.name} blocked and you only dealt {round(dmg-enemy.defense,2)} damage!")
                                                        input()
                                                        descloop = False
                                                        ent1 = 1
                                                weap.hit = hitti
                                                weap.crit = critti
                                                y = 0
                                                loop = False
                                            else:
                                                print("You don't have enough mana!")
                                                loop = False
                                                input()
                                        elif desc == "no" or desc == "2":
                                            loop = False
                                        elif desc == "back" or desc == "3":
                                            y = 0
                                            loop = False
                                        else:
                                            print("Try again")
                                            input()
                                elif desc == "back":
                                    y = 0
                                    descloop = False
                                else:
                                    print("Try again")
                                    input()
                        #Player = Ability 3 + Enemy = Counter 15 = 18
                        case 18:
                            y = 1
                            while y == 1:
                                hitti = weap.hit
                                critti = weap.crit
                                os.system("cls" if os.name == "nt" else "clear")
                                desc = input(f"Which Ability: ({weap.ability1}|{weap.ability2}|{weap.ability3} or Back?) ").lower().replace(" ","")
                                if desc == weap.ability1.lower().replace(" ","") or desc == weap.ability2.lower().replace(" ","") or desc == weap.ability3.lower().replace(" ",""):    
                                    run = False
                                    abi = DruemmerAbilities.abilities()
                                    abimethods = [target for target, method in inspect.getmembers(DruemmerAbilities.abilities, predicate=inspect.isfunction)     
                                        if not target.startswith("_")]
                                    abiindex = abimethods.index(desc)
                                    currentabi = abimethods[abiindex]
                                    getattr(abi, currentabi)(hp, mp, dmg, char_kl.Str, char_kl.Dex, char_kl.Arc, char_kl.Fai, weap.hit, weap.crit, run)
                                    loop = True
                                    while loop == True:
                                        print(f"Effect: {abi.effect}")
                                        print(f"Costs: HP = {abi.hpcost} | MP = {abi.mpcost}")
                                        print(f"Scaling: STR = {abi.strscl}% | DEX = {abi.dexscl}%")
                                        print(f"         ARC = {abi.arcscl}% | FAI = {abi.faiscl}%")
                                        desc = input("1)Yes | 2)No | 3)Back: ").lower().replace(" ","")
                                        if desc == "yes" or desc == "1":
                                            if abi.mpcost <= mp:
                                                run = True
                                                hpcheck = hp
                                                mpcheck = mp
                                                hp, mp, dmg, char_kl.Str, char_kl.Dex, char_kl.Arc, char_kl.Fai, weap.hit, weap.crit = getattr(abi, currentabi)(hp, mp, dmg, char_kl.Str, char_kl.Dex, char_kl.Arc, char_kl.Fai, weap.hit, weap.crit, run)
                                                if hp > hpcheck:
                                                    print(f"You regenerated {hp-hpcheck} Health!")
                                                    print("You narrowly avoid its counterattack!")
                                                    input()
                                                    descloop = False
                                                    ent1 = 1
                                                elif mp > mpcheck:
                                                    print(f"You regenerated {mp-mpcheck} Mana!")
                                                    print("You narrowly avoid its counterattack!")
                                                    input()
                                                    descloop = False
                                                    ent1 = 1
                                                else:
                                                    if hitchance <= weap.hit:
                                                        chance = random.randint(1,100)
                                                        dodge = enemy.dodgechance * 2
                                                        if dodge >= chance:
                                                            hp -= enemy.damage
                                                            print(f"The {enemy.name} dodged your attack and retaliates!")
                                                            print(f"You take {enemy.damage} damage!")
                                                            input()
                                                            descloop = False
                                                            ent1 = 1
                                                        else:
                                                            enemy.hp -= dmg
                                                            if critchance <= weap.crit:
                                                                print("You critically hit the enemy!")
                                                            print(f"The {enemy.name} is unable to dodge and you hit it for {dmg} damage")
                                                            input()
                                                            descloop = False
                                                            ent1 = 1
                                                weap.hit = hitti
                                                weap.crit = critti
                                                y = 0
                                                loop = False
                                            else:
                                                print("You don't have enough mana!")
                                                input()
                                                loop = False
                                        elif desc == "no" or desc == "2":
                                            loop = False
                                        elif desc == "back" or desc == "3":
                                            y = 0
                                            loop = False
                                        else:
                                            print("Try again")
                                            input()
                                elif desc == "back":
                                    y = 0
                                    descloop = False
                                else:
                                    print("Try again")
                                    input()
                        case _:
                            print("What happened?")

            if enemy.hp < 0:
                enemy.hp = 0
            if hp < 0:
                hp = 0
            if enemy.hp == 0:
                print("You won!")
                input()
                return hp, mp
            elif hp == 0:
                return hp, mp
            else:
                pass

#<<<Enemy Ranges>>>
#0-4 Spiders | Spiderling - ???
#5-?
#?-?
#?-?


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
        self.hp = 26 #Hit Points des Monsters
        self.maxhp = 26 #Max Hit Points des Monsters
        self.mana = 3 #Mana des Monsters
        self.maxmana = 3 #Max Mana des Monsters
        self.damage = 5 #Schaden den das Monster verursacht
        self.defense = 3 #Rüstungswert des Monster der den Schaden reduziert
        self.dodgechance = 20 #Chance zum Ausweichen
        self.hitchance = 95 #Chance mit einer Attacke zu Treffen
        self.critchance = 10 #Chance auf einen kritischen Treffer

    def btwoheadedspider(self):
        self.name = "Twoheaded Spider"
        self.hp = 38 #Hit Points des Monsters
        self.maxhp = 38 #Max Hit Points des Monsters
        self.mana = 3 #Mana des Monsters
        self.maxmana = 3 #Max Mana des Monsters
        self.damage = 7 #Schaden den das Monster verursacht
        self.defense = 5 #Rüstungswert des Monster der den Schaden reduziert
        self.dodgechance = 15 #Chance zum Ausweichen
        self.hitchance = 90 #Chance mit einer Attacke zu Treffen
        self.critchance = 20 #Chance auf einen kritischen Treffer

    def cbroodmother(self):
        self.name = "Broodmother"
        self.hp = 92 #Hit Points des Monsters
        self.maxhp = 92 #Max Hit Points des Monsters
        self.mana = 3 #Mana des Monsters
        self.maxmana = 3 #Max Mana des Monsters
        self.damage = 2 #Schaden den das Monster verursacht
        self.defense = 0 #Rüstungswert des Monster der den Schaden reduziert
        self.dodgechance = 5 #Chance zum Ausweichen
        self.hitchance = 85 #Chance mit einer Attacke zu Treffen
        self.critchance = 0 #Chance auf einen kritischen Treffer

        
#Testing
#combat(0,2,0,3)
