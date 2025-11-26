import DruemmerCharacterClass

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
    print("HP:", char.HP)
    print("Mana:", char.Mana)
    print("Strength:", char.Str)
    print("Dexterity:", char.Dex)
    print("Arcana:",char.Arc)
    print("Faith:", char.Fai)


game_start()

game_play()