import time
import webbrowser

print('tippen sie "suche" um den webbrowser zu öffnen')
x = input("was? ")
if x == "suche":
    webbrowser.open("https://www.google.com/")
    #open googel
    print("googel öpen")
else:
    time.sleep(10000)
    print("hat nicht geklappt... programm schliesst sich")