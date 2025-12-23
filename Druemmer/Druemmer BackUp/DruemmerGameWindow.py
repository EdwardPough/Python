#Importing Investigate and UseObject

#import DruemmerInvestigate >>>muss ich???<<<

#Druemmer Game Window Class

class window():
    def __init__(self):
        self.place = "None" #Name des momentanen Ortes
        self.description = "None" #Beschreibung
        self.north = "None" #Show if way north exist
        self.east = "None" #Show if way east exist
        self.south = "None" #Show if way south exist
        self.west = "None" #Show if way west exist
        self.combat = False
        self.interactable = False
#        self.investigate = None #Investigation of Target <<<WIP>>>
#        self.useobject = None #Object Usage on Target <<<WIP>>>


    def testraum1(self):            #Interactable
        self.place = "Testraum1"
        self.description = """Du befindest dich in Testraum1!
        Du siehst Testobjekt11!
        Ebenfalls siehst Testobjekt12!
        Und auch Testobjekt13!"""
        self.north = "testraum2"
        self.east = "testraum4"
        self.south = False
        self.west = False
        self.combat = False
        self.interactable = True
        self.object1 = "kleiner schrank"
        self.object1nr = 0
        self.object2 = "verkümmertes skelett"
        self.object2nr = 1
        self.object3 = False
        self.object3nr = False



    def testraum2(self):                #Interactable
        self.place = "Testraum2"
        self.description = """Du befindest dich in Testraum2!
        Du siehst Testobjekt21!
        Ebenfalls siehst Testobjekt22!
        Und auch Testobjekt23!"""
        self.north = False
        self.east = "testraum3"
        self.south = "testraum1"
        self.west = False
        self.combat = False
        self.interactable = True
        self.object1 = "tr21_schrank"
        self.object2 = "tr22_tisch"
        self.object3 = "tr23_skelett"

    def testraum3(self):                #Combat
        self.place = "Testraum3"
        self.description = """Du befindest dich in Testraum3!
        Du siehst Testobjekt31!
        Ebenfalls siehst Testobjekt32!
        Und auch Testobjekt33!"""
        self.north = False
        self.east = False
        self.south = "testraum4"
        self.west = "testraum2"
        self.combat = True
        self.interactable = False
        self.object1 = "tr31_schrank"
        self.object2 = "tr32_tisch"
        self.object3 = "tr33_skelett"

    def testraum4(self):                   #Combat and Interactable
        self.place = "Testraum4"
        self.description = """Du befindest dich in Testraum4!
        Du siehst Testobjekt41!
        Ebenfalls siehst Testobjekt42!
        Und auch Testobjekt43!"""
        self.north = "testraum3"
        self.east = False
        self.south = False
        self.combat = True
        self.interactable = True
        self.west = "testraum1"
        self.object1 = "tr41_schrank"
        self.object2 = "tr42_tisch"
        self.object3 = "tr43_skelett"
