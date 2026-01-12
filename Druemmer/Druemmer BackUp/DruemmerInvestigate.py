import inspect
import os
import random
import DruemmerItemsEquipments

investigated = []

#Druemmer Investigate Function
def investigate(z,x): # z = Investigation Target | x = Currentraum
    #Retrieving Investigation Class and Attributes
    inves = investigation()
    invesmethods = [target for target, method in inspect.getmembers(investigation, predicate=inspect.isfunction)     
        if not target.startswith("_")]
    currentinves = invesmethods[z]
    getattr(inves, currentinves)()
    #Retrieving Equipments
    equip = DruemmerItemsEquipments.equipments()
    equ = DruemmerItemsEquipments.equipments
    equipmethods = [target for target, method in inspect.getmembers(equ, predicate=inspect.isfunction)     
        if not target.startswith("_")]
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(inves.target)
        print(inves.tdescription)
        if inves.tinteractable == True:
            if inves.subtarget1 != None:
                print("--------------")
                print(inves.subtarget1)
                print(inves.subtarget1desc)
            if inves.subtarget2 != None:
                print("--------------")
                print(inves.subtarget2)
                print(inves.subtarget2desc)
            if inves.subtarget3 != None:
                print("--------------")
                print(inves.subtarget3)
                print(inves.subtarget3desc)
            print("--------------")
            ent = input("Wollen sie etwas näher untersuchen oder zurück? ").lower().replace(" ", "")
            if inves.subtarget1 != None:
                if ent == inves.subtarget1.lower().replace(" ",""):
                    invested = str(inves.subtarget1)+str(x)
                    if (invested in investigated) == False:
                        itemfind = random.randint(1,100)
                        print("Test")
                        investigated.append(invested)
                        input()
                    else:
                        print("Das hast du bereits untersucht")
                        input()
            if inves.subtarget2 != None:
                if ent == inves.subtarget2.lower().replace(" ",""):
                    invested = str(inves.subtarget2)+str(x)
                    if (invested in investigated) == False:
                        itemfind = random.randint(1,100)
                        print("Test")
                        investigated.append(invested)
                        input()
                    else:
                        print("Das hast du bereits untersucht")
                        input()
            if inves.subtarget3 != None:
                if ent == inves.subtarget3.lower().replace(" ",""):
                    invested = str(inves.subtarget3)+str(x)
                    if (invested in investigated) == False:
                        itemfind = random.randint(1,100)
                        print("Test")
                        investigated.append(invested)
                        input()
                    else:
                        print("Das hast du bereits untersucht")
                        input()
            if ent == "zurück":
                break



#Druemmer Investigation Objects
class investigation():
    def __init__(self):
        self.target = None
        self.tdescription = None
        self.tinteractable = False
        self.subtarget1 = None
        self.subtarget1desc = None
        self.subtarget2 = None
        self.subtarget2desc = None
        self.subtarget3 = None
        self.subtarget3desc = None

    def akleinerschrank(self):
        self.target = "Kleiner Schrank"
        self.tdescription = "Ein kleiner Schrank!"
        self.tinteractable = True
        self.subtarget1 = "Linke Schublade"
        self.subtarget1desc = "Schublade :)"
        self.st1chance = 25
        self.subtarget2 = "Rechte Schublade"
        self.subtarget2desc = "Eine stark verfallene Schublade."
        self.st2chance = 10
        self.subtarget3 = None
        self.subtarget3desc = None
        self.st3chance = 0

    def bverkümmertesskelett(self):
        self.target = "Verkümmertes Skelett"
        self.tdescription = "Ein verkümmertes Skelett!"
        self.tinteractable = False
        self.subtarget1 = None
        self.subtarget1desc = None
        self.st1chance = 0
        self.subtarget2 = None
        self.subtarget2desc = None
        self.st2chance = 0
        self.subtarget3 = None
        self.subtarget3desc = None
        self.st3chance = 0

    def cbedecktertisch(self):
        self.target = "Bedeckter Tisch"
        self.tdescription = "Ein bedeckter Tisch!"
        self.tinteractable = False
        self.subtarget1 = None
        self.subtarget1desc = None
        self.st1chance = 0
        self.subtarget2 = None
        self.subtarget2desc = None
        self.st2chance = 0
        self.subtarget3 = None
        self.subtarget3desc = None
        self.st3chance = 0
