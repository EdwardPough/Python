import time
import webbrowser
arbeitstag = float(input("Wie lange ist Ihr Arbeitstag(in stunden und dezimalzahl) "))
arbeiten = float(input("Wie lange Arbeiten(in stunden und dezimalzahl) "))
pause = float(input("Wie lange Pause(in minuten und dezimalzahl) "))
tagdauer = 0
while tagdauer <= (60*60)*arbeitstag:
    time.sleep(60*arbeiten)
    print("PAUSE!PAUSE!PAUSE!PAUSE!PAUSE!PAUSE!")
    webbrowser.open("https://youtu.be/Jm6huaxUMnI?si=BwHp662tm1nRbdP8")
    time.sleep(60*pause)
    print("PAUSE ENDE!PAUSE ENDE!PAUSE ENDE!PAUSE ENDE!PAUSE ENDE!PAUSE ENDE!PAUSE ENDE!PAUSE ENDE!PAUSE ENDE!PAUSE ENDE!PAUSE ENDE!")
    tagdauer = tagdauer + arbeiten + pause

print("Arbeitstag zu Ende :)")