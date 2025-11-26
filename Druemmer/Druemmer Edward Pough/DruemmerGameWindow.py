#Importing Investigate and UseObject

#import DruemmerInvestigate >>>muss ich???<<<

#Druemmer Game Window Class

class window():
    def __init__(self, place, desc, north, east, south, west):
        self.place = place #Name des momentanen Ortes
        self.description = desc #Beschreibung
        self.north = north #Show if way north exist
        self.east = east #Show if way east exist
        self.south = south #Show if way south exist
        self.west = west #Show if way west exist
#        self.investigate = None #Investigation of Target <<<WIP>>>
#        self.useobject = None #Object Usage on Target <<<WIP>>>


    def testraum1(self):
        defi = window.testraum1
        self.place = "Testraum1"
        self.description = """Du befindest dich in Testraum1!
        Du siehst Testobjekt11!
        Ebenfalls siehst Testobjekt12!
        Und auch Testobjekt13!"""
        self.north = None
        self.east = None
        self.south = False
        self.west = False
        raum = window(self.place, self.description, self.north, self.east, self.south, self.west)
        raum.north = self.testraum2()
        raum.east = self.testraum4()
        return raum
        object1 = "tr11_schrank"
        object2 = "tr12_tisch"
        object3 = "tr13_skelett"



    def testraum2(self):
        defi = window.testraum2
        place = "Testraum2"
        description = """Du befindest dich in Testraum2!
        Du siehst Testobjekt21!
        Ebenfalls siehst Testobjekt22!
        Und auch Testobjekt23!"""
        north = False
        east = True and window.testraum3
        south = True and window.testraum1
        west = False
        object1 = "tr21_schrank"
        object2 = "tr22_tisch"
        object3 = "tr23_skelett"

    def testraum3(self):
        defi = window.testraum3
        place = "Testraum3"
        description = """Du befindest dich in Testraum3!
        Du siehst Testobjekt31!
        Ebenfalls siehst Testobjekt32!
        Und auch Testobjekt33!"""
        north = False
        east = False
        south = True and window.testraum4
        west = True and window.testraum2
        object1 = "tr31_schrank"
        object2 = "tr32_tisch"
        object3 = "tr33_skelett"

    def testraum4(self):
        defi = window.testraum4
        place = "Testraum4"
        description = """Du befindest dich in Testraum4!
        Du siehst Testobjekt41!
        Ebenfalls siehst Testobjekt42!
        Und auch Testobjekt43!"""
        north = True and window.testraum3
        east = False
        south = False
        west = True and window.testraum1
        object1 = "tr41_schrank"
        object2 = "tr42_tisch"
        object3 = "tr43_skelett"
