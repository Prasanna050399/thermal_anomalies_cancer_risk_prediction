from datetime import datetime, date

import cv2 as cv


class Cache:
    def __init__(self):
        self.isNew = True
        self.id = None
        self.name = ""
        self.ref = ""
        self.age = ""
        self.specialRemarks = ""
        self.historyMeterScore = None
        self.date = str(date.today())
        self.time = datetime.now().strftime("%H:%M:%S")
        self.originalImages = [None, None, None, None, None]
        self.rightMask = None
        self.leftMask = None
        self.roiMasks = [None, None, None, None, None]
        self.normalBodyColorPos = [None, None]
        self.normalBodyColor = [None, None, None] #BGR
        self.normalBodyColorGray = None
        self.anomalies = [None, None, None, None, None]
        #self.asymmetryImage = None ##
        self.edges = [[None,0,255], [None,0,255], [None,0,255], [None,0,255], [None,0,255]]
        self.remarks = ["", "", ""] #left region, right region, suggestions
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
        print("Name:", self.name)
        print("Referred By:", self.ref)
        print("Age:", self.age)
        print("Special Remarks:", self.specialRemarks)
        print("History Meter Score:", self.historyMeterScore)
        print("date:", self.date)
        print("time:", self.time)
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
        print("Normal body color co-ordinates:", self.normalBodyColorPos)
        print("Normal body color:", self.normalBodyColor)
        print("Normal body color gray level:", self.normalBodyColorGray)
        print("Anomaly images:")
        for anomaly in self.anomalies:
            if anomaly is not None:
                print("\tCalculated")
            else:
                print("\tNone")
##        temp = "Calculated"
##        if self.asymmetryImage is None:
##            temp = "None"
##        print("Asymmetry image:", temp)
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

    def visualize(self):
        originalnames = ["Front view image", "Right Lateral view image", "Left Lateral view image", "Right Oblique view image", "Left Oblique view image"]
        roinames = ["Front view ROI", "Right Lateral view ROI", "Left Lateral view ROI", "Right Oblique view ROI", "Left Oblique view ROI"]
        anomalynames = ["Front view anomaly", "Right Lateral view anomaly", "Left Lateral view anomaly", "Right Oblique view anomaly", "Left Oblique view anomaly"]
        edgenames = ["Front view edges", "Right Lateral view edges", "Left Lateral view edges", "Right Oblique view edges", "Left Oblique view edges"]

        present = False
        for i in range(len(self.originalImages)):
            if self.originalImages[i] is not None:
                cv.imshow(originalnames[i], self.originalImages[i])
                present = True
        if present is True:
            cv.waitKey()

        present = False
        for i in range(len(self.roiMasks)):
            if self.roiMasks[i] is not None:
                cv.imshow(roinames[i], self.roiMasks[i])
                present = True
        if present is True:
            cv.waitKey()

        present = False
        for i in range(len(self.anomalies)):
            if self.anomalies[i] is not None:
                cv.imshow(anomalynames[i], self.anomalies[i])
                present = True
        if present is True:
            cv.waitKey()

        present = False
        for i in range(len(self.edges)):
            if self.edges[i][0] is not None:
                cv.imshow(edgenames[i], self.edges[i][0])
                present = True
        if present is True:
            cv.waitKey()

    def saveCacheToFileSystem(self):
        originalNames = ["001_o.jpg", "002_o.jpg", "003_o.jpg", "004_o.jpg", "005_o.jpg"]
        anomalyNames = ["001_a.jpg", "002_a.jpg", "003_a.jpg", "004_a.jpg", "005_a.jpg"]
        edgeNames = ["001_e.jpg", "002_e.jpg", "003_e.jpg", "004_e.jpg", "005_e.jpg"]

        for i in range(len(self.originalImages)):
            cv.imwrite(originalNames[i], self.originalImages[i])

        for i in range(len(self.anomalies)):
            cv.imwrite(anomalyNames[i], self.anomalies[i])

        for i in range(len(self.edges)):
            cv.imwrite(edgeNames[i], self.edges[i][0])
        
