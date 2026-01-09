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
completedrooms = []

#Clear Terminal Function >>> os.system("cls" if os.name == "nt" else "clear") <<<

#----------------------------------------------Start des Spieles---------------------------------------------

def game_start():
    global kl
    y = 1
    for i in range(3):
        DruemmerItemsEquipments.equipped.append("-")
        DruemmerItemsEquipments.realequipped.append("-")
    while y == 1:
        os.system("cls" if os.name == "nt" else "clear")
        print("Willkommen bei der Testversion von Druemmer")
        print("Welche Klasse wollen sie spielen?")
        klasse = str(input("(Krieger/Ritter/Magier/Kleriker) ")).lower()
        #---------Krieger---------
        if klasse == "krieger":
            print("Sie spielen einen Krieger!")
            char.aclasswarrior()
            print("Das wären ihre Stats:")
            print("HP:", char.hp)
            print("Mana:", char.Mana)
            print("Strength:", char.Str)
            print("Dexterity:", char.Dex)
            print("Arcana:",char.Arc)
            print("Faith:", char.Fai)
            x = 1
            kl = 0
            while x == 1:
                sicher = str(input("Sind Sie sich sicher? ")).lower()
                if sicher == "ja":
                    print("Viel Spaß!")
                    y = 2
                    inv.append("Dagger")
                    inv.append("Mace")
                    inv.append("Chainmail")
                    DruemmerItemsEquipments.equip_real("mace")
                    DruemmerItemsEquipments.equip_real("chainmail")
                    DruemmerItemsEquipments.equip_real("dagger")
                    break
                elif sicher == "nein":
                    print("Bitte wählen Sie eine neue Klasse!")
                    x = 2
                else:
                    print("Bitte versuchen sie es nochmal!")
        #---------Ritter---------
        elif klasse == "ritter":
            print("Sie spielen einen Ritter!")
            char.bclassknight()
            print("Das wären ihre Stats:")
            print("HP:", char.hp)
            print("Mana:", char.Mana)
            print("Strength:", char.Str)
            print("Dexterity:", char.Dex)
            print("Arcana:",char.Arc)
            print("Faith:", char.Fai)
            x = 1
            kl = 1
            while x == 1:
                sicher = str(input("Sind Sie sich sicher? ")).lower()
                if sicher == "ja":
                    print("Viel Spaß!")
                    y = 2
                    inv.append("Dagger")
                    inv.append("Shortsword")
                    inv.append("Halfplate")
                    DruemmerItemsEquipments.equip_real("shortsword")
                    DruemmerItemsEquipments.equip_real("halfplate")
                    DruemmerItemsEquipments.equip_real("dagger")
                    break
                elif sicher == "nein":
                    print("Bitte wählen Sie eine neue Klasse!")
                    x = 2
                else:
                    print("Bitte versuchen sie es nochmal!")
        #---------Magier---------
        elif klasse == "magier":
            print("Sie spielen einen Magier!")
            char.cclasswizard()
            print("Das wären ihre Stats:")
            print("HP:", char.hp)
            print("Mana:", char.Mana)
            print("Strength:", char.Str)
            print("Dexterity:", char.Dex)
            print("Arcana:",char.Arc)
            print("Faith:", char.Fai)
            x = 1
            kl = 2
            while x == 1:
                sicher = str(input("Sind Sie sich sicher? ")).lower()
                if sicher == "ja":
                    print("Viel Spaß!")
                    y = 2
                    inv.append("Dagger")
                    inv.append("Magicwand")
                    inv.append("Leatherarmor")
                    DruemmerItemsEquipments.equip_real("magicwand")
                    DruemmerItemsEquipments.equip_real("leatherarmor")
                    DruemmerItemsEquipments.equip_real("dagger")
                    break
                elif sicher == "nein":
                    print("Bitte wählen Sie eine neue Klasse!")
                    x = 2
                else:
                    print("Bitte versuchen sie es nochmal!")
        #---------Kleriker---------
        elif klasse == "kleriker":
            print("Sie spielen einen Kleriker!")
            char.dclasscleric()
            print("Das wären ihre Stats:")
            print("HP:", char.hp)
            print("Mana:", char.Mana)
            print("Strength:", char.Str)
            print("Dexterity:", char.Dex)
            print("Arcana:",char.Arc)
            print("Faith:", char.Fai)
            x = 1
            kl = 3
            while x == 1:
                sicher = str(input("Sind Sie sich sicher? ")).lower()
                if sicher == "ja":
                    print("Viel Spaß!")
                    y = 2
                    inv.append("Dagger")
                    inv.append("Holysymbol")
                    inv.append("Leatherarmor")
                    DruemmerItemsEquipments.equip_real("holysymbol")
                    DruemmerItemsEquipments.equip_real("leatherarmor")
                    DruemmerItemsEquipments.equip_real("dagger")
                    break
                elif sicher == "nein":
                    print("Bitte wählen Sie eine neue Klasse!")
                    x = 2
                else:
                    print("Bitte versuchen sie es nochmal!")
        else:
            print("Bitte versuchen sie es nochmal!")

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
                print(room.description)
                char.hp = combat.combat(room.enemyrange_a, room.enemyrange_z, currentraum, kl, char.hp)
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
        print("Klasse:", char.name)
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
        
        decision = str(input("Was machen Sie? ")).lower()
        
        #<<<Inventory>>>

        if decision == "inventory":
            while True:
                os.system("cls" if os.name == "nt" else "clear")
                print(f"Equipped: {equip}")
                print(f"Inventory: {inv}")
                x = input("Equip/Info/Use/Zurück: ").lower().replace(" ","")
                if x == "equip":
                    x = input("Was wollen Sie ausrüsten? ").lower().replace(" ","")
                    if x.capitalize() in inv:
                        DruemmerItemsEquipments.equip_real(x)
                        print("jo ging")
                        input()
                    else:
                        print("jo ging net")
                        input()
                elif x == "info":
                    x = input("Von was wollen Sie die Informationen? ").lower().replace(" ","")
                    if x.capitalize() in inv:
                        os.system("cls" if os.name == "nt" else "clear")
                        DruemmerItemsEquipments.info(x)
                        input()
                    else:
                        print("jo ging net")
                        input()
                elif x == "zurück":
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
                    print("Zurück?")
                    x = str(input("Was wollen sie untersuchen? ")).lower().replace(" ", "")
                    if room.object1 != False:
                        if room.object1.lower().replace(" ", "") == x:
                            inves.investigate(room.object1nr)
                            y == 1
                            input("Weiter?")
                    if room.object2 != False:
                        if room.object2.lower().replace(" ", "") == x:
                            inves.investigate(room.object2nr)
                            y == 1
                            input("Weiter?")
                    if room.object3 != False:
                        if room.object3.lower().replace(" ", "") == x:
                            inves.investigate(room.object3nr)
                            y == 1
                            input("Weiter?")
                    if x == "zurück":
                        break
                else:
                    print("Der Raum ist leer!")
                    input("Weiter? ")
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
            print("Bitte nochmal")
    
    if spiel_gewonnen == True:
        print("Glückwunsch ihr habt gesiegt")
    elif char.hp <= 0:
        print("Ihr seid gestorben")
    else:
        print("Was ist geschehen?")

#------------------------------------------------------------------------------------------------------------
game_start()
game_play()