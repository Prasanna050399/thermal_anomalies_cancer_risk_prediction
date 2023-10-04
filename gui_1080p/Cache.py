from datetime import datetime, date

class Cache:
    def __init__(self):
        self.isNew = True
        self.id = None
        self.date = str(date.today())
        self.originalImages = [None, None, None, None, None]
        self.rightMask = None
        self.leftMask = None
        self.roiMasks = [None, None, None, None, None]
        self.normalBodyColor = [None, None, None] #RGB
        self.anomalies = [None, None, None, None, None]
        self.edges = [None, None, None, None, None]
        self.remarks = [None, None, None] #left region, right region, suggestions
        self.fullRemarks = None
        self.diagnosticScore = None
        
    def generatePatientID(self):
        temp = str(datetime.now())
        self.id = ""
        for char in temp:
            if char != " ":
                self.id += char
            else:
                self.id += ","
        isNew = True
        return
    
    def setPatientID(self, id):
        self.id = id
        self.isNew = False
        return
    
    def setVisitDate(self, date):
        self.date = date
        return
    