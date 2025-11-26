import DruemmerCharacterClass
import DruemmerGameWindow

world = DruemmerGameWindow.window("","",None,None,None,None).testraum1()
char = DruemmerCharacterClass.character()

#Möchte man spielen? Ja/Nein



#Start des Spieles          <<<<<DONE>>>>>

def game_start():
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

#Spielkörper

def game_play():
    global world
    global current_raum
    spiel_gewonnen = False
    while spiel_gewonnen == False:
        print("---------------------------")
        print(world.place)
        print(world.description)
        if world.north != False:
            print(">>>North")
        if world.east != False:
            print(">>>East")
        if world.south != False:
            print(">>>South")
        if world.west != False:
            print(">>>West")
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
            current_raum = world.north
        elif decision == "east":
            world.east()
        elif decision == "south":
            world.south()
        elif decision == "west":
            world.west()
        elif decision == "ende": #TESTING <<>> DELETE LATER / TESTING <<>> DELETE LATER / TESTING <<>> DELETE LATER / 
            spiel_gewonnen = True
        else:
            print("Bitte nochmal")


game_start()
current_raum = world.testraum1() #TEST/TEST/TEST/TEST/TEST/TEST/TEST/TEST/TEST/TEST/TEST/TEST/TEST/TEST/TEST
game_play()