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
        self.normalBodyColor = [None, None, None] #BGR
        self.anomalies = [None, None, None, None, None]
        self.asymmetryImage = None
        self.edges = [[None,0,255], [None,0,255], [None,0,255], [None,0,255], [None,0,255]]
        self.remarks = [None, None, None] #left region, right region, suggestions
        self.diagnosticScore = None
        self.diagnosticFields = [None, None, None, None, None, None, None, None, None]
        self.nn = [None, None]
        
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

    def print(self):
        print()
        print("isNew:", self.isNew)
        print("id:", self.id)
        print("date:", self.date)
        print("Original images:")
        for image in self.originalImages:
            if image is not None:
                print("\tImage")
            else:
                print("\tNone")
        print("ROI masks:")
        temp1, temp2 = "None", "None"
        if self.rightMask is not None:
            temp1 = "Selected"
        if self.leftMask is not None:
            temp2 = "Selected"
        print("\t", temp1, temp2)
        first = True
        for mask in self.roiMasks:
            if mask is not None:
                if first:
                    print("\tCalculated")
                else:
                    print("\tSelected")
            else:
                print("\tNone")
            first = False
        print("Normal body color:", self.normalBodyColor)
        print("Anomaly images:")
        for anomaly in self.anomalies:
            if anomaly is not None:
                print("\tCalculated")
            else:
                print("\tNone")
        temp = "Calculated"
        if self.asymmetryImage is None:
            temp = "None"
        print("Asymmetry image:", temp)
        print("Edge detected images:")
        for edgeImage in self.edges:
            if edgeImage[0] is not None:
                print("\tCalculated", edgeImage[1], edgeImage[2])
            else:
                print("\tNone", edgeImage[1], edgeImage[2])
        print("Remarks:")
        for remark in self.remarks:
            print("\t'", remark, "'")
        print("Diagnostic score:", self.diagnosticScore)
        print("Diagnostic meter fields:")
        for field in self.diagnosticFields:
            print("\t", field)
        print("NN Prediction:", self.nn)
        print()
