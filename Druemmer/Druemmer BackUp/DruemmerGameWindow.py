#Importing Investigate and UseObject
#import DruemmerInvestigate >>>muss ich???

#Druemmer Game Window Class


class window():
    def __init__(self):
        self.place = None #Name des momentanen Ortes
        self.description = None #Beschreibung
        self.north = None #Show if way north exist
        self.east = None #Show if way east exist
        self.south = None #Show if way south exist
        self.west = None #Show if way west exist
        self.investigate = None #Investigation of Target
        self.useobject = None #Object Usage on Target

    def testraum1(self, object1 ,object2, object3):
        self.place = "Testraum1"
        self.description = """Du befindest dich in Testraum1!
        Du siehst Testobjekt11!
        Ebenfalls siehst Testobjekt12!
        Und auch Testobjekt13!"""
        self.north = True
        self.east = True
        self.south = False
        self.west = False
        object1 = "tr11_schrank"
        object2 = "tr12_tisch"
        object3 = "tr13_skelett"



    def testraum2(self):
        pass

    def testraum3(self):
        pass