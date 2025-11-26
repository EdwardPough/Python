import time
import webbrowser
import random

arbeitstag = float(input("Wie lange ist Ihr Arbeitstag(in stunden und dezimalzahl) "))
arbeiten = float(input("Wie lange Arbeiten(in stunden und dezimalzahl) "))
pause = float(input("Wie lange Pause(in minuten und dezimalzahl) "))
tagdauer = 0
while tagdauer <= (60*60)*arbeitstag:
    time.sleep(60*arbeiten)
    print("PAUSE!PAUSE!PAUSE!PAUSE!PAUSE!PAUSE!")
    webbrowser.open("https://youtu.be/Jm6huaxUMnI?si=BwHp662tm1nRbdP8")
    solution = random.randint(1,100)
    guess = None
    counter = 0
    print("Käpt'n Hook: Lass uns ein Spiel spielen. Ich denke mir eine Zahl zwischen 1 und 100 und du musst sie erraten!")
    print("Käpt'n Hook: Du hast 6 Versuche. Versuch dein Bestes!")
    while guess != solution:
        guess = int(input("Welche Zahl? "))
        if counter == 6:
            print("Käpt'n Hook: Du hast mehr als 6 Versuche gebraucht. VERLOREN!")
            break
        elif guess > solution:
            counter = counter + 1
            print("Käpt'n Hook: Ha! Das war zu hoch! Das war dein", counter ,"ter Versuch!")
        elif guess < solution:
            counter = counter + 1
            print("Käpt'n Hook: Idiot! Das war zu niedrig! Das war dein", counter ,"ter Versuch!")
        else:
            print("Käpt'n Hook: Du hast es geschafft! Die Zahl war", solution ,"!")
    time.sleep(60*pause)
    print("PAUSE ENDE!PAUSE ENDE!PAUSE ENDE!PAUSE ENDE!PAUSE ENDE!PAUSE ENDE!PAUSE ENDE!PAUSE ENDE!PAUSE ENDE!PAUSE ENDE!PAUSE ENDE!")
    tagdauer = tagdauer + arbeiten + pause

print("Arbeitstag zu Ende :)")