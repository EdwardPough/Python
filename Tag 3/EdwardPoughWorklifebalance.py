import time
import webbrowser

tagdauer = 0
while tagdauer <= (60*60)*8:
    time.sleep(60*90)
    print("PAUSE!PAUSE!PAUSE!PAUSE!PAUSE!PAUSE!")
    webbrowser.open("https://youtu.be/Jm6huaxUMnI?si=BwHp662tm1nRbdP8")
    time.sleep(60*7.5)
    print("PAUSE ENDE!PAUSE ENDE!PAUSE ENDE!PAUSE ENDE!PAUSE ENDE!PAUSE ENDE!PAUSE ENDE!PAUSE ENDE!PAUSE ENDE!PAUSE ENDE!PAUSE ENDE!")
    tagdauer = tagdauer + 5850

print("Arbeitstag zu Ende :)")