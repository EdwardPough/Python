from importlib.metadata.diagnose import inspect
import DruemmerCharacterClass
import DruemmerGameWindow
import inspect
import os


world = DruemmerGameWindow
char = DruemmerCharacterClass.character()
room = world.window()

clear = os.system('cls' if os.name == 'nt' else 'clear')

#Möchte man spielen? Ja/Nein



#----------------------------------------------Start des Spieles---------------------------------------------

def game_start():
    clear()
    print("Willkommen bei der Testversion von Druemmer")
    y = 1
    while y == 1:
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
               if not place.startswith('_')]
    currentraum = raummethods[0] #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    spiel_gewonnen = False
    while spiel_gewonnen == False:
        clear()
        room = world.window()
        raummethods = [place for place, method in inspect.getmembers(world.window, predicate=inspect.isfunction) 
               if not place.startswith('_')]
        getattr(room, currentraum)()
        print("---------------------------")
        print(room.place)
        print(room.description)
        if room.north != False:
            print(f">>>North ({room.north.capitalize()})")
        if room.east != False:
            print(f">>>East ({room.east.capitalize()})")
        if room.south != False:
            print(f">>>South ({room.south.capitalize()})")
        if room.west != False:
            print(f">>>West ({room.west.capitalize()})")
        print("---------------------------")
        print("HP:", char.HP)
        print("Mana:", char.Mana)
        print("Strength:", char.Str)
        print("Dexterity:", char.Dex)
        print("Arcana:",char.Arc)
        print("Faith:", char.Fai)
        print("---------------------------")
        decision = str(input("Was machen Sie? ")).lower()
        if decision == "north":
            currentraum = room.north
        elif decision == "east":
            currentraum = room.east
        elif decision == "south":
            currentraum = room.south
        elif decision == "west":
            currentraum = room.west
        elif decision == "ende": #TESTING <<>> DELETE LATER / TESTING <<>> DELETE LATER / TESTING <<>> DELETE LATER / 
            spiel_gewonnen = True
        else:
            print("Bitte nochmal")

#------------------------------------------------------------------------------------------------------------
game_start()
game_play()