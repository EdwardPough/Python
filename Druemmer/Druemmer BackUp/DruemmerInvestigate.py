#Druemmer Investigate Function
def investigate():
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
        