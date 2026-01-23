#<<Imports>>>

import DruemmerCharacterClass
import DruemmerGameWindow
import DruemmerInvestigate
import DruemmerCombat
import DruemmerItemsEquipments
import inspect
import os

#<<<Variablen>>>

inves = DruemmerInvestigate
world = DruemmerGameWindow
char = DruemmerCharacterClass.character()
room = world.window()
combat = DruemmerCombat
inv = DruemmerItemsEquipments.inventory
equip = DruemmerItemsEquipments.equipped
realequ = DruemmerItemsEquipments.realequipped
it = DruemmerItemsEquipments.itemsinv
ite = DruemmerItemsEquipments
show = DruemmerItemsEquipments.showitem
completedrooms = []

#Clear Terminal Function >>> os.system("cls" if os.name == "nt" else "clear") <<<

#----------------------------------------------Start des Spieles---------------------------------------------

def game_start():
    global kl
    y = 1
    ite.appendingitems("Healthpotion")
    ite.appendingitems("Healthpotion")
    for i in range(3):
        DruemmerItemsEquipments.equipped.append("-")
        DruemmerItemsEquipments.realequipped.append("-")
    while y == 1:
        os.system("cls" if os.name == "nt" else "clear")
        print("Welcome to the Testverion of Druemmer")
        print("Which Class do yo choose?")
        klasse = str(input("(Warrior/Knight/Wizard/Cleric) ")).lower()
        #---------Krieger---------
        if klasse == "warrior":
            print("You chose Warrior!")
            char.aclasswarrior()
            print("Warrior Stats:")
            print("HP:", char.hp)
            print("Mana:", char.Mana)
            print("Strength:", char.Str)
            print("Dexterity:", char.Dex)
            print("Arcana:",char.Arc)
            print("Faith:", char.Fai)
            x = 1
            kl = 0
            while x == 1:
                sicher = str(input("Are you sure? ")).lower()
                if sicher == "yes":
                    print("Good luck!")
                    y = 2
                    inv.append("Dagger")
                    inv.append("Mace")
                    inv.append("Chainmail")
                    DruemmerItemsEquipments.equip_real("mace")
                    DruemmerItemsEquipments.equip_real("chainmail")
                    DruemmerItemsEquipments.equip_real("dagger")
                    break
                elif sicher == "no":
                    print("Please choose a new class!")
                    x = 2
                else:
                    print("Try again!")
        #---------Ritter---------
        elif klasse == "knight":
            print("You chose Knight!")
            char.bclassknight()
            print("Knight Stats:")
            print("HP:", char.hp)
            print("Mana:", char.Mana)
            print("Strength:", char.Str)
            print("Dexterity:", char.Dex)
            print("Arcana:",char.Arc)
            print("Faith:", char.Fai)
            x = 1
            kl = 1
            while x == 1:
                sicher = str(input("Are you sure? ")).lower()
                if sicher == "yes":
                    print("Good luck!")
                    y = 2
                    inv.append("Dagger")
                    inv.append("Shortsword")
                    inv.append("Halfplate")
                    DruemmerItemsEquipments.equip_real("shortsword")
                    DruemmerItemsEquipments.equip_real("halfplate")
                    DruemmerItemsEquipments.equip_real("dagger")
                    break
                elif sicher == "no":
                    print("Please choose a new class!")
                    x = 2
                else:
                    print("Try again!")
        #---------Magier---------
        elif klasse == "wizard":
            print("You chose Wizard!")
            char.cclasswizard()
            print("Wizard Stats:")
            print("HP:", char.hp)
            print("Mana:", char.Mana)
            print("Strength:", char.Str)
            print("Dexterity:", char.Dex)
            print("Arcana:",char.Arc)
            print("Faith:", char.Fai)
            x = 1
            kl = 2
            while x == 1:
                sicher = str(input("Are you sure? ")).lower()
                if sicher == "yes":
                    print("Good luck!")
                    y = 2
                    inv.append("Dagger")
                    inv.append("Magicwand")
                    inv.append("Leatherarmor")
                    DruemmerItemsEquipments.equip_real("magicwand")
                    DruemmerItemsEquipments.equip_real("leatherarmor")
                    DruemmerItemsEquipments.equip_real("dagger")
                    break
                elif sicher == "no":
                    print("Please choose a new class!")
                    x = 2
                else:
                    print("Try again!")
        #---------Kleriker---------
        elif klasse == "cleric":
            print("You chose Cleric!")
            char.dclasscleric()
            print("Cleric Stats:")
            print("HP:", char.hp)
            print("Mana:", char.Mana)
            print("Strength:", char.Str)
            print("Dexterity:", char.Dex)
            print("Arcana:",char.Arc)
            print("Faith:", char.Fai)
            x = 1
            kl = 3
            while x == 1:
                sicher = str(input("Are you sure? ")).lower()
                if sicher == "yes":
                    print("Good luck!")
                    y = 2
                    inv.append("Dagger")
                    inv.append("Holysymbol")
                    inv.append("Chainmail")
                    DruemmerItemsEquipments.equip_real("holysymbol")
                    DruemmerItemsEquipments.equip_real("chainmail")
                    DruemmerItemsEquipments.equip_real("dagger")
                    input()
                    break
                elif sicher == "no":
                    print("Please choose a new class!")
                    x = 2
                else:
                    print("Try again!")
        else:
            print("Try again!")

#-----------------------------------------------Spielkörper--------------------------------------------------

def game_play():
    global world
    global currentraum
    global kl
    raummethods = [place for place, method in inspect.getmembers(world.window, predicate=inspect.isfunction) 
               if not place.startswith("_")]
    currentraum = raummethods[0] #Works now :)
    spiel_gewonnen = False
    
    #<<<Gameloop>>>
    
    while spiel_gewonnen == False and char.hp > 0:
        os.system("cls" if os.name == "nt" else "clear")
        
        #Getting Attributes of the room and printing them
        
        room = world.window()
        raummethods = [place for place, method in inspect.getmembers(world.window, predicate=inspect.isfunction) 
               if not place.startswith("_")]
        getattr(room, currentraum)()

        #<<<Initialising Combat if there is>>>
        if (room.place in completedrooms) == False:
            if room.combat != False:
                char.hp, char.Mana = combat.combat(room.enemyrange_a, room.enemyrange_z, kl, char.hp, char.Mana)
                completedrooms.append(room.place)
                os.system("cls" if os.name == "nt" else "clear")
                if char.hp == 0:
                    break
            else:
                pass
        else:
            pass
        
        #<<<Printing Everything>>>
        print("---------------------------")
        print("Class:", char.name)
        print("HP:", char.hp, "/", char.MaxHP)
        print("Mana:", char.Mana, "/", char.MaxMana)
        print("---------------------------")
        print(room.place)
        print(room.description)
        
        #<<<Options in Rooms>>>
        
        print(f">>>Inventory")
        if room.interactable != False:
            print(f">>>Investigate")
        if room.north != False:
            print(f">>>North ({room.north.capitalize()})")
        if room.east != False:
            print(f">>>East ({room.east.capitalize()})")
        if room.south != False:
            print(f">>>South ({room.south.capitalize()})")
        if room.west != False:
            print(f">>>West ({room.west.capitalize()})")
        print("---------------------------")
        
        #<<<Decisions that can be made>>>
        
        decision = str(input("What do you do? ")).lower()
        
        #<<<Inventory>>>

        if decision == "inventory":
            while True:
                os.system("cls" if os.name == "nt" else "clear")
                print(f"Equipped: {equip}")
                print(f"Equipments: {inv}")
                print(f"Items:")
                ite.showitem()
                x = input("Equip/Info/Use/Back: ").lower().replace(" ","")
                if x == "equip":
                    x = input("What do you want to equip? ").lower().replace(" ","")
                    if x.capitalize() in inv:
                        DruemmerItemsEquipments.equip_real(x)
                        print("You equipped it!")
                        input()
                    else:
                        print("Didn't work.")
                        input()
                elif x == "info":
                    x = input("From what equipment do you want the stats? ").lower().replace(" ","")
                    if x.capitalize() in inv:
                        os.system("cls" if os.name == "nt" else "clear")
                        DruemmerItemsEquipments.info(x)
                        input()
                    else:
                        print("Didn't work.")
                        input()
                elif x == "use": #WORK IN PROGRESS
                    x = input("Which Item do you want to use? ").lower().replace(" ","")
                    if x.capitalize() in inv:
                        os.system("cls" if os.name == "nt" else "clear")
                        DruemmerItemsEquipments.info(x)
                        input()
                    else:
                        print("Please choose from the items.")
                        input()
                elif x == "back":
                    break

        
        #<<<Investigate>>>
        
        elif decision == "investigate":
            y = 0
            while y == 0:
                os.system("cls" if os.name == "nt" else "clear")
                if room.interactable != False:
                    if room.object1 != False:
                        print(room.object1)
                    if room.object2 != False:
                        print(room.object2)
                    if room.object3 != False:
                        print(room.object3)
                    print("Back?")
                    x = str(input("What do you want to investigate? ")).lower().replace(" ", "")
                    if room.object1 != False:
                        if room.object1.lower().replace(" ", "") == x:
                            inves.investigate(room.object1nr, currentraum)
                            y == 1
                    if room.object2 != False:
                        if room.object2.lower().replace(" ", "") == x:
                            inves.investigate(room.object2nr, currentraum)
                            y == 1
                    if room.object3 != False:
                        if room.object3.lower().replace(" ", "") == x:
                            inves.investigate(room.object3nr, currentraum)
                            y == 1
                    if x == "back":
                        break
                else:
                    print("The room is empty!")
                    input("Continue? ")
                    break
                        
            
        #<<<Directions>>>
        
        elif decision == "north":
            if room.north != False:
                currentraum = room.north
        elif decision == "east":
            if room.east != False:
                currentraum = room.east
        elif decision == "south":
            if room.south != False:
                currentraum = room.south
        elif decision == "west":
            if room.west != False:
                currentraum = room.west
        elif decision == "ende": #TESTING <<>> DELETE LATER / TESTING <<>> DELETE LATER / TESTING <<>> DELETE LATER / 
            spiel_gewonnen = True
        else:
            print("Try again!")
    

    #<<<Ende Der Loop>>>
    if spiel_gewonnen == True:
        print("Congrats you won!")
    elif char.hp <= 0:
        print("You died!")
    else:
        print("What did you do?")

#------------------------------------------------------------------------------------------------------------
game_start()
game_play()