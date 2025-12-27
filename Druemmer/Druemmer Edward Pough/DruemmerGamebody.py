import DruemmerCharacterClass
import DruemmerGameWindow
import DruemmerInvestigate
import inspect
import os

inves = DruemmerInvestigate
world = DruemmerGameWindow
char = DruemmerCharacterClass.character()
room = world.window()

#Clear Terminal Function >>> os.system("cls" if os.name == "nt" else "clear") <<<

#----------------------------------------------Start des Spieles---------------------------------------------

def game_start():
    y = 1
    while y == 1:
        os.system("cls" if os.name == "nt" else "clear")
        print("Willkommen bei der Testversion von Druemmer")
        print("Welche Klasse wollen sie spielen?")
        klasse = str(input("(Krieger/Ritter/Magier/Kleriker) ")).lower()
        if klasse == "krieger":
            print("Sie spielen einen Krieger!")
            char.classwarrior()
            print("Das wären ihre Stats:")
            print("HP:", char.HP)
            print("Mana:", char.Mana)
            print("Strength:", char.Str)
            print("Dexterity:", char.Dex)
            print("Arcana:",char.Arc)
            print("Faith:", char.Fai)
            x = 1
            while x == 1:
                sicher = str(input("Sind Sie sich sicher? ")).lower()
                if sicher == "ja":
                    print("Viel Spaß!")
                    y = 2
                    break
                elif sicher == "nein":
                    print("Bitte wählen Sie eine neue Klasse!")
                    x = 2
                else:
                    print("Bitte versuchen sie es nochmal!")
        elif klasse == "ritter":
            print("Sie spielen einen Ritter!")
            char.classknight()
            print("Das wären ihre Stats:")
            print("HP:", char.HP)
            print("Mana:", char.Mana)
            print("Strength:", char.Str)
            print("Dexterity:", char.Dex)
            print("Arcana:",char.Arc)
            print("Faith:", char.Fai)
            x = 1
            while x == 1:
                sicher = str(input("Sind Sie sich sicher? ")).lower()
                if sicher == "ja":
                    print("Viel Spaß!")
                    y = 2
                    break
                elif sicher == "nein":
                    print("Bitte wählen Sie eine neue Klasse!")
                    x = 2
                else:
                    print("Bitte versuchen sie es nochmal!")
        elif klasse == "magier":
            print("Sie spielen einen Magier!")
            char.classwizard()
            print("Das wären ihre Stats:")
            print("HP:", char.HP)
            print("Mana:", char.Mana)
            print("Strength:", char.Str)
            print("Dexterity:", char.Dex)
            print("Arcana:",char.Arc)
            print("Faith:", char.Fai)
            x = 1
            while x == 1:
                sicher = str(input("Sind Sie sich sicher? ")).lower()
                if sicher == "ja":
                    print("Viel Spaß!")
                    y = 2
                    break
                elif sicher == "nein":
                    print("Bitte wählen Sie eine neue Klasse!")
                    x = 2
                else:
                    print("Bitte versuchen sie es nochmal!")
        elif klasse == "kleriker":
            print("Sie spielen einen Kleriker!")
            char.classcleric()
            print("Das wären ihre Stats:")
            print("HP:", char.HP)
            print("Mana:", char.Mana)
            print("Strength:", char.Str)
            print("Dexterity:", char.Dex)
            print("Arcana:",char.Arc)
            print("Faith:", char.Fai)
            x = 1
            while x == 1:
                sicher = str(input("Sind Sie sich sicher? ")).lower()
                if sicher == "ja":
                    print("Viel Spaß!")
                    y = 2
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
    raummethods = [place for place, method in inspect.getmembers(world.window, predicate=inspect.isfunction) 
               if not place.startswith("_")]
    currentraum = raummethods[0] #Works now :)
    spiel_gewonnen = False
    
    #<<<Gameloop>>>
    
    while spiel_gewonnen == False:
        os.system("cls" if os.name == "nt" else "clear")
        
        #Getting Attributes of the room and printing them
        
        room = world.window()
        raummethods = [place for place, method in inspect.getmembers(world.window, predicate=inspect.isfunction) 
               if not place.startswith("_")]
        getattr(room, currentraum)()
        print("---------------------------")
        print("Klasse:", char.name)
        print("HP:", char.HP, "/", char.MaxHP)
        print("Mana:", char.Mana, "/", char.MaxMana)
        print("---------------------------")
        print(room.place)
        print(room.description)
        
        #<<<Options in Rooms>>>
        
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
        
        #<<<Investigate>>>
        
        if decision == "investigate":
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

#------------------------------------------------------------------------------------------------------------
game_start()
game_play()