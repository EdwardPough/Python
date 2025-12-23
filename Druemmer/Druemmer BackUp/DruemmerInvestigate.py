import inspect


#Druemmer Investigate Function
def investigate(x):
    invesmethods = [place for place, method in inspect.getmembers(investigation, predicate=inspect.isfunction)     
        if not place.startswith("_")]
    print(invesmethods)
    currentinves = invesmethods[x]
    #investigation.currentinves()
    print(investigation.target)
    print(investigation.tdescription)
    if investigation.tinteractable == True:
        pass

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
        self.subtarget3.desc = None

    def kleinerschrank(self):
        self.target = "Kleiner Schrank"
        self.tdescription = "Ein kleiner Schrank!"
        self.tinteractable = False
        self.subtarget1 = None
        self.subtarget1desc = None
        self.subtarget2 = None
        self.subtarget2desc = None
        self.subtarget3 = None
        self.subtarget3.desc = None

    def verkümmertesskelett(self):
        self.target = "Verkümmertes Skelett"
        self.tdescription = "Ein verkümmertes Skelett!"
        self.tinteractable = False
        self.subtarget1 = None
        self.subtarget1desc = None
        self.subtarget2 = None
        self.subtarget2desc = None
        self.subtarget3 = None
        self.subtarget3.desc = None