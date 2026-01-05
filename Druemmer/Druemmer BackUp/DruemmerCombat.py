#Druemmer Combat File
#<<<Imports>>>
import random
import DruemmerCharacterClass
import DruemmerGameWindow
import inspect
import os #os.system("cls" if os.name == "nt" else "clear")

#Variablen
char = DruemmerCharacterClass

#<<<Combat Function>>>
    #Klassen Krieger = 0 | Ritter = 1 | Magier = 2 | Kleriker = 3
def combat(a,b,w,y): #<<< a = enemyrange_a | b = enemyrange_z | w = Raum | x = Gegner | y = Klasse | z = Equipment(Not Implemented Yet) >>>
    #---------Determining Character Class---------
    char_kl = DruemmerCharacterClass.character()
    classmethods = [target for target, method in inspect.getmembers(char.character, predicate=inspect.isfunction)     
        if not target.startswith("_")]
    currentclass = classmethods[y]
    getattr(char_kl, currentclass)()
    #---------Choosing Enemy---------
    enemy = enemies()
    enemiesmethods = [target for target, method in inspect.getmembers(enemies, predicate=inspect.isfunction)     
        if not target.startswith("_")]
    enemyrange = random.randint(a, b)
    currentenemy = enemiesmethods[enemyrange]
    getattr(enemy, currentenemy)()
    #---------Combat---------
    while enemy.hp > 0:
        os.system("cls" if os.name == "nt" else "clear")
        print(enemy.name)
        print(f"{enemy.hp}|{enemy.maxhp}")
        edec = random.randint(0,2)
        if edec == 0: #Attacking
            print(f"The {enemy.name} intends on attacking!")
        elif edec == 1: #Defending
            print(f"The {enemy.name} intends on blocking!")
        elif edec == 2: #Dodging and Countering
            print(f"The {enemy.name} is awaiting an attack!")
        print("------------------")
        print(char_kl.name)
        print(f"HP: {char_kl.HP}|{char_kl.MaxHP}")
        print(f"Mana: {char_kl.Mana}|{char_kl.MaxMana}")
        ent = 0
        while ent == 0:
            print("What will you do?")
            print("1)Attack | 2)Defend | 3)Item(Not Implemented)")
            pdec = input().lower().replace(" ","")
            if pdec == "attack":
                if edec == 0:
                    enemy.hp -= char_kl.Str
                    char_kl.HP -= enemy.damage
                    print(f"You attacked and dealt {char_kl.Str} damage!")
                    print(f"The {enemy.name} attacked and dealt {enemy.damage} damage!")
                    ent = 1
                    input()
                elif edec == 1:
                    enemy.hp -= char_kl.Str - enemy.defense
                    print(f"The {enemy.name} blocked and you only dealt {char_kl.Str-enemy.defense} damage!")
                    ent = 1
                    input()
                elif edec == 2:
                    chance = random.randint(1,100)
                    dodge = enemy.dodgechance * 2
                    if dodge >= chance:
                        char_kl.HP -= enemy.damage
                        print(f"The {enemy.name} dodged your attack and retaliates!")
                        print(f"You take {enemy.damage} damage!")
                        ent = 1
                        input()
                    else:
                        enemy.hp -= char_kl.Str
                        print(f"The {enemy.name} is unable to dodge and you hit it for {char_kl.Str} damage")
                        ent = 1
                        input()
            elif pdec == "defend":
                if edec == 0:
                    char_kl.HP -= enemy.damage - 5 #PROBEWERT
                    print(f"You blocked the attack of the {enemy.name} and only took {enemy.damage} damage!")
                    ent = 1
                    input()
                elif edec == 1:
                    print(f"The {enemy.name} blocked and so did you!")
                    print("Nothing happens...")
                    ent = 1
                    input()
                elif edec == 2:
                    print(f"You saw through the trick of {enemy.name}!")
                    print("You narrowly avoid its counterattack!")
                    ent = 1
                    input()
            else:
                print("Try again")
        print("Ihr habt gesiegt!")

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
combat(0,2,0,3)