import inspect


#Druemmer Investigate Function
def investigate(z):
    inves = investigation()
    invesmethods = [target for target, method in inspect.getmembers(investigation, predicate=inspect.isfunction)     
        if not target.startswith("_")]
    currentinves = invesmethods[z]
    getattr(inves, currentinves)()
    print(inves.target)
    print(inves.tdescription)
    if inves.tinteractable == True:
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

    def akleinerschrank(self):
        self.target = "Kleiner Schrank"
        self.tdescription = "Ein kleiner Schrank!"
        self.tinteractable = False
        self.subtarget1 = None
        self.subtarget1desc = None
        self.subtarget2 = None
        self.subtarget2desc = None
        self.subtarget3 = None
        self.subtarget3desc = None

    def bverkümmertesskelett(self):
        self.target = "Verkümmertes Skelett"
        self.tdescription = "Ein verkümmertes Skelett!"
        self.tinteractable = False
        self.subtarget1 = None
        self.subtarget1desc = None
        self.subtarget2 = None
        self.subtarget2desc = None
        self.subtarget3 = None
        self.subtarget3desc = None

    def cbedecktertisch(self):
        self.target = "Bedeckter Tisch"
        self.tdescription = "Ein bedeckter Tisch!"
        self.tinteractable = False
        self.subtarget1 = None
        self.subtarget1desc = None
        self.subtarget2 = None
        self.subtarget2desc = None
        self.subtarget3 = None
        self.subtarget3desc = None
