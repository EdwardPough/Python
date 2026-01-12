#Importing Investigate and UseObject



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
        self.description = f"""Du befindest dich in Testraum1!
        Du siehst einen kleinen Schrank!
        Ebenfalls siehst du ein verkümmertes Skelett!"""
        self.north = "testraum2"
        self.east = "testraum4"
        self.south = False
        self.west = False
        self.combat = False
        self.interactable = True
        self.object1 = "Kleiner Schrank" #Nummer 0
        self.object1nr = 0
        self.object2 = "Verkümmertes Skelett" #Nummer 1
        self.object2nr = 1
        self.object3 = False
        self.object3nr = False



    def testraum2(self):                #Interactable
        self.place = "Testraum2"
        self.description = """Du befindest dich in Testraum2!
        Du siehst einen bedeckten Tisch!"""
        self.north = False
        self.east = "testraum3"
        self.south = "testraum1"
        self.west = False
        self.combat = False
        self.interactable = True
        self.object1 = "Bedeckter Tisch" #Nummer 2
        self.object1nr = 2
        self.object2 = None
        self.object2nr = False
        self.object3 = None
        self.object3nr = False

    def testraum3(self):                #Combat
        self.place = "Testraum3"
        self.description = """Du befindest dich in Testraum3!
        Du siehst Spinnenweben, die den leeren Raum verzieren!
        Aus den Schatten bewegt sich eine Silhouette auf dich hinzu..."""
        self.north = False
        self.east = False
        self.south = "testraum4"
        self.west = "testraum2"
        self.combat = True
        self.enemyrange_a = 0
        self.enemyrange_z = 0
        self.interactable = False
        self.object1 = None
        self.object1nr = False
        self.object2 = None
        self.object2nr = False
        self.object3 = None
        self.object3nr = False

    def testraum4(self):                   #Combat and Interactable
        self.place = "Testraum4"
        self.description = """Du befindest dich in Testraum4!
        Du siehst einen kleinen Schrank!
        Ebenfalls siehst du ein verkümmertes Skelett!
        Und auch einen bedeckten Tisch!
        Aus den Schatten bewegt sich eine Silhouette
        auf dich hinzu..."""
        self.north = "testraum3"
        self.east = False
        self.south = False
        self.west = "testraum1"
        self.combat = True
        self.enemyrange_a = 1
        self.enemyrange_z = 2
        self.interactable = True
        self.object1 = "Kleiner Schrank" #Nummer 0
        self.object1nr = 0
        self.object2 = "Verkümmertes Skelett" #Nummer 1
        self.object2nr = 1
        self.object1 = "Bedeckter Tisch" #Nummer 2
        self.object1nr = 2
