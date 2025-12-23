import inspect


#Druemmer Investigate Function
def investigate(x):
    invesmethods = [target for target, method in inspect.getmembers(investigation, predicate=inspect.isfunction)     
        if not target.startswith("_")]
    print(invesmethods)
    currentinves = invesmethods[x]
    getattr(investigation(), currentinves)()
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
        self.subtarget3desc = None

    def kleinerschrank(self):
        self.target = "Kleiner Schrank"
        self.tdescription = "Ein kleiner Schrank!"
        self.tinteractable = False
        self.subtarget1 = None
        self.subtarget1desc = None
        self.subtarget2 = None
        self.subtarget2desc = None
        self.subtarget3 = None
        self.subtarget3desc = None

    def verkümmertesskelett(self):
        self.target = "Verkümmertes Skelett"
        self.tdescription = "Ein verkümmertes Skelett!"
        self.tinteractable = False
        self.subtarget1 = None
        self.subtarget1desc = None
        self.subtarget2 = None
        self.subtarget2desc = None
        self.subtarget3 = None
        self.subtarget3desc = None