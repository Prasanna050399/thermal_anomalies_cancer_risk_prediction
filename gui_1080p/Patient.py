from datetime import datetime, date
from dateutil.relativedelta import relativedelta
import cv2 as cv
import numpy as np
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import gridfs

class Patient:
    def __init__(self):
        self.id = ""
        self.isNew = True
        self.name = ""
        self.mobile = ""
        self.date = str(date.today())
        self.dateOfBirth = ""   
        self.referredBy = ""
        self.maritalStatus = 0
        self.breastFeed = 0
        self.ageAtFirstPregnancy = 0
        self.bcFamilyHistory = 0
        self.bcSelfHistory = 0
        self.breastProfile = 0
        self.radiationHistory = 0
        self.medConsumptionHistory = 0
        self.remarks = ""
        self.scans = [None, None, None, None, None, None]
        self.rois = [None, None, None, None, None, None]
        self.anomalies = [None, None, None, None, None, None]
        self.edges = [None, None, None, None, None, None]
        
    
    
    def newPatient(self):
        self.id = str(datetime.now())
        temp = ""
        for char in self.id:
            if char != " ":
                temp += char
            else:
                temp += ","
        self.id = temp
        self.isNew = True
        self.name = ""
        self.mobile = ""
        self.date = str(date.today())
        self.dateOfBirth = ""
        self.referredBy = ""
        self.maritalStatus = 0
        self.breastFeed = 0
        self.ageAtFirstPregnancy = 0
        self.bcFamilyHistory = 0
        self.bcSelfHistory = 0
        self.breastProfile = 0
        self.radiationHistory = 0
        self.medConsumptionHistory = 0
        self.remarks = ""
        self.scans.clear()
        del self.scans
        self.scans = [None, None, None, None, None, None]
        self.rois.clear()
        del self.rois
        self.rois = [None, None, None, None, None, None]
        self.anomalies.clear()
        del self.anomalies
        self.anomalies = [None, None, None, None, None, None]
        self.edges.clear()
        del self.edges
        self.edges = [None, None, None, None, None, None]
    
    
    
    def clearPatient(self):
        self.id = ""
        self.isNew = False
        self.name = ""
        self.mobile = ""
        self.date = str(date.today())
        self.dateOfBirth = ""
        self.referredBy = ""
        self.maritalStatus = 0
        self.breastFeed = 0
        self.ageAtFirstPregnancy = 0
        self.bcFamilyHistory = 0
        self.bcSelfHistory = 0
        self.breastProfile = 0
        self.radiationHistory = 0
        self.medConsumptionHistory = 0
        self.remarks = ""
        self.scans.clear()
        del self.scans
        self.scans = [None, None, None, None, None, None]
        self.rois.clear()
        del self.rois
        self.rois = [None, None, None, None, None, None]
        self.anomalies.clear()
        del self.anomalies
        self.anomalies = [None, None, None, None, None, None]
        self.edges.clear()
        del self.edges
        self.edges = [None, None, None, None, None, None]
        
    
    
    def getPatientId(self):
        return self.id
        
    def setPatientId(self, entry):
        self.id = entry
        
    def getPatientName(self):
        return self.name
        
    def setPatientName(self, entry):
        self.name = entry
        
    def getPatientMobileNumber(self):
        return self.mobile
    
    def setPatientMobileNumber(self, entry):
        self.mobile = entry
    
    def getDate(self):
        return self.date
    
    def setDate(self, entry):
        self.date = entry
        
    def getDateOfBirth(self):
        if self.dateOfBirth == "":
            return date.today()
        return datetime.strptime(self.dateOfBirth, "%Y-%m-%d").date()
        
    def setDateOfBirth(self, entry):
        self.dateOfBirth = entry.strftime("%Y-%m-%d")
    
    def getDateOfBirthForDatabase(self):
        if self.dateOfBirth == "":
            return str(date.today())
        return self.dateOfBirth
        
    def setDateOfBirthForDatabase(self, entry):
        self.dateOfBirth = entry
        
    def getAge(self):
        return str(relativedelta(date.today(), datetime.strptime(dateOfBirth)).years)
    
    #def setAge(self, arg):
    #    self.age = arg
    
    def getReferredBy(self):
        return self.referredBy
        
    def setReferredBy(self, entry):
        self.referredBy = entry
        
    def getMaritalStatus(self):
        return self.maritalStatus
        
    def setMaritalStatus(self, entry):
        self.maritalStatus = entry
        
    def getBreastFeedingHistory(self):
        return self.breastFeed
        
    def setBreastFeedingHistory(self, entry):
        self.breastFeed = entry
        
    def getAgeDuringFirstPregnancy(self):
        return self.ageAtFirstPregnancy
        
    def setAgeDuringFirstPregnancy(self, entry):
        self.ageAtFirstPregnancy = entry
        
    def getBCFamilyHistory(self):
        return self.bcFamilyHistory
        
    def setBCFamilyHistory(self, entry):
        self.bcFamilyHistory = entry
        
    def getSelfHistoryOfBC(self):
        return self.bcSelfHistory
        
    def setSelfHistoryOfBC(self, entry):
        self.bcSelfHistory = entry
        
    def getBreastProfile(self):
        return self.breastProfile
        
    def setBreastProfile(self, entry):
        self.breastProfile = entry
        
    def getRadiationHistory(self):
        return self.radiationHistory
        
    def setRadiationHistory(self, entry):
        self.radiationHistory = entry
        
    def getMedicineConsumptionHistory(self):
        return self.medConsumptionHistory
        
    def setMedicineConsumptionHistory(self, entry):
        self.medConsumptionHistory = entry
        
    def getSpecialRemarks(self):
        return self.remarks
        
    def setSpecialRemarks(self, entry):
        self.remarks = entry
        
    def getScanImage(self, idx):
        return self.scans[idx]
    
    def setScanImage(self, image, idx):
        self.scans[idx] = image
    
    def getRoiImage(self, idx):
        return self.rois[idx]
    
    def setRoiImage(self, image, idx):
        self.rois[idx] = image
    
    def clearROIs(self):
        self.rois.clear()
    
    def getImageArray(self):
        return self.scans
    
    def getAnomalyImage(self, idx):
        return self.anomalies[idx]
    
    def setAnomalyImage(self, image, idx):
        self.anomalies[idx] = image
    
    def getAnomalyArray(self):
        return self.anomalies
    
    def getEdgesImage(self, idx):
        return self.edges[idx]
    
    def setEdgesImage(self, image, idx):
        self.edges[idx] = image
    
    def getEdgesArray(self):
        return self.edges
    
    
    
    def connectToMongoDB(self):
        self.client = MongoClient()
        try:
            self.client.admin.command("ismaster")
            self.db =self.client.Patient
            self.patientInformation = self.db.Information
            self.imageStore = self.db.Images
            self.fs = gridfs.GridFS(self.db)
        except ConnectionFailure:
            return False
        return True
    
    
    
    def checkDatabaseConnection(self):
        try:
            self.client.admin.command("ismaster")
        except ConnectionFailure:
            return False
    
    
    
    def getPatientInformationFromDB(self):
        ret = self.patientInformation.find_one({"_id":self.id})
        if ret is not None:
            self.isNew = False
            self.name = ret["Name"]
            self.dateOfBirth = ret["DOB"]
            self.referredBy = ret["ReferedBy"]
            self.mobile = ret["MobileNo"]
            self.maritalStatus = ret["MaritalStatus"]
            self.breastFeed = ret["BreastFeed"]
            self.ageAtFirstPregnancy = ret["AgeAtFirstPregnancy"]
            self.bcFamilyHistory = ret["BCFamilyHistory"]
            self.bcSelfHistory = ret["BCSelfHistory"]
            self.breastProfile = ret["BreastProfile"]
            self.radiationHistory = ret["RadiationHistory"]
            self.medConsumptionHistory = ret["MedConsumptionHistory"]
            self.remarks = ret["SpecialRemarks"]
        return True
    
    
    
    def savePatientInformationInDB(self):
        Information = {
            "_id" : self.id,
            "Name": self.name,
            "DOB": self.dateOfBirth,
            "ReferedBy": self.referredBy,
            "MobileNo" : self.mobile,
            "MaritalStatus" : self.maritalStatus,
            "BreastFeed": self.breastFeed,
            "AgeAtFirstPregnancy":self.ageAtFirstPregnancy,
            "BCFamilyHistory": self.bcFamilyHistory,
            "BCSelfHistory": self.bcSelfHistory,
            "BreastProfile":self.breastProfile,
            "RadiationHistory": self.radiationHistory,
            "MedConsumptionHistory":self.medConsumptionHistory,
            "SpecialRemarks" : self.remarks
        }
        
        # saving new patient data
        if(self.isNew == True):
            self.id =  self.patientInformation.insert_one(Information).inserted_id
            patientImageCollection = {
                "_id" : self.id
                "visits" : []
            }
            self.imageStore.insert_one(patientImageCollection)
            self.isNew = False
        # saving existing patient data
        else:
            self.patientInformation.update_one({'_id':self.id}, {"$set": Information})
        return True
    
    
    
    def getPatientScanImagesFromDB(self):
        patientVisitCursor = self.imageStore.find_one( { "_id" : self.id } )["visits"]
        
        for visit in patientVisitCursor:
            if visit["VisitDate"] == self.date:
                for i in range(6):
                    readimg1 = self.fs.get( visit["OriginalImages"][i]["ImageID"] )
                    readimg1 = np.frombuffer( readimg1.read(), dtype=np.uint8 )
                    readimg1 = np.reshape( readimg1, visit["OriginalImages"][i]["ImageShape"] )
                    self.scans[i] = readimg1
                    
                    readimg2 = self.fs.get( visit["AnomalyImages"][i]["ImageID"] )
                    readimg2 = np.frombuffer( readimg2.read(), dtype=np.uint8 )
                    readimg2 = np.reshape( readimg2, visit["AnomalyImages"][i]["ImageShape"] )
                    self.anomalies[i] = readimg2
                    
                    readimg3 = self.fs.get( visit["EdgeImages"][i]["ImageID"] )
                    readimg3 = np.frombuffer( readimg3.read(), dtype=np.uint8 )
                    readimg3 = np.reshape( readimg3, visit["EdgeImages"][i]["ImageShape"] )
                    self.edges[i] = readimg3
        
        return True
    
    
    
    def savePatientScanImagesInDB(self):
        original = [None, None, None, None, None, None]
        anomalies = [None, None, None, None, None, None]
        edges = [None, None, None, None, None, None]
        
        for i in range(6):
            original[i] = self.scans[i].copy()
            anomalies[i] = self.anomalies[i].copy()
            edges[i] = self.edges[i].copy()
        
        originalId = []
        anomaliesId= []
        edgesId = []
        
        for i in range(6):
            originalId.append( self.fs.put( original[i].tobytes(), encoding="utf-8" ) )
            anomaliesId.append( self.fs.put( anomalies[i].tobytes(), encoding="utf-8" ) )
            edgesId.append( self.fs.put( edges[i].tobytes(), encoding="utf-8" ) )
        
        visit = {
            "VisitDate" : self.date,
            
            "OriginalImages" : [
                {
                    "ImageID" : originalId[0],
                    "ImageShape" : original[0].shape,
                    "ImageDateType" : str(original[0].dtype)
                },
                {
                    "ImageID" : originalId[1],
                    "ImageShape" : original[1].shape,
                    "ImageDateType" : str(original[1].dtype)
                },
                {
                    "ImageID" : originalId[2],
                    "ImageShape" : original[2].shape,
                    "ImageDateType" : str(original[2].dtype)
                },
                {
                    "ImageID" : originalId[3],
                    "ImageShape" : original[3].shape,
                    "ImageDateType" : str(original[3].dtype)
                },
                {
                    "ImageID" : originalId[4],
                    "ImageShape" : original[4].shape,
                    "ImageDateType" : str(original[4].dtype)
                },
                {
                    "ImageID" : originalId[5],
                    "ImageShape" : original[5].shape,
                    "ImageDateType" : str(original[5].dtype)
                }
            ],
            
            "AnomalyImages" : [
                {
                    "ImageID" : anomaliesId[0],
                    "ImageShape" : anomalies[0].shape,
                    "ImageDateType" : str(anomalies[0].dtype)
                },
                {
                    "ImageID" : anomaliesId[1],
                    "ImageShape" : anomalies[1].shape,
                    "ImageDateType" : str(anomalies[1].dtype)
                },
                {
                    "ImageID" : anomaliesId[2],
                    "ImageShape" : anomalies[2].shape,
                    "ImageDateType" : str(anomalies[2].dtype)
                },
                {
                    "ImageID" : anomaliesId[3],
                    "ImageShape" : anomalies[3].shape,
                    "ImageDateType" : str(anomalies[3].dtype)
                },
                {
                    "ImageID" : anomaliesId[4],
                    "ImageShape" : anomalies[4].shape,
                    "ImageDateType" : str(anomalies[4].dtype)
                },
                {
                    "ImageID" : anomaliesId[5],
                    "ImageShape" : anomalies[5].shape,
                    "ImageDateType" : str(anomalies[5].dtype)
                }
            ],
            
            "EdgeImages" : [
                {
                    "ImageID" : edgesId[0],
                    "ImageShape" : edges[0].shape,
                    "ImageDateType" : str(edges[0].dtype)
                },
                {
                    "ImageID" : edgesId[1],
                    "ImageShape" : edges[1].shape,
                    "ImageDateType" : str(edges[1].dtype)
                },
                {
                    "ImageID" : edgesId[2],
                    "ImageShape" : edges[2].shape,
                    "ImageDateType" : str(edges[2].dtype)
                },
                {
                    "ImageID" : edgesId[3],
                    "ImageShape" : edges[3].shape,
                    "ImageDateType" : str(edges[3].dtype)
                },
                {
                    "ImageID" : edgesId[4],
                    "ImageShape" : edges[4].shape,
                    "ImageDateType" : str(edges[4].dtype)
                },
                {
                    "ImageID" : edgesId[5],
                    "ImageShape" : edges[5].shape,
                    "ImageDateType" : str(edges[5].dtype)
                }
            ]
        }
        
        self.imageStore.update_one( { "_id" : self.id } , { "$push" : { "visits" : visit } } )
        
        return True
    
    
    
    def searchInDB(self, searchMethod, query):
        ret = self.patientInformation.find({ searchMethod : { "$regex" : "^"+query } })
        result = []
        for entry in ret:
            patientId = entry["_id"]
            patientName = entry["Name"]
            patientMobile = entry["MobileNo"]
            temp = patientId + " " + patientName + " " + patientMobile
            result.append(temp)
        return result
    
    
    
    def findPatientVisitDates(self):
        patientVisitCursor = self.imageStore.find_one( { "_id" : self.id } )["visits"]
        visitDates = []
        for visit in patientVisitCursor:
            visitDates.append(visit["VisitDate"])
        return visitDates
    
    
    
    def saveInformationConfirmationCheck(self):
        for attribute, value in vars(self).items():
            if attribute == "id":
                continue
            elif attribute == "remarks":
                continue
            elif value == "":
                return False
        return True
    
    
    
    def generateReportConfirmationCheck(self):
        for image in self.scans:
            if image is None:
                return False
        return True
    
    
    
    #for testing purposes only
    def printPatientClassContents(self):
        # for attribute, value in var.__dict__.iteritems():
        # for attribute, value in vars(self).items():
        # members = [attr for attr in dir(example) if not callable(getattr(example, attr)) and not attr.startswith("__")]
        # for attribute in dir(an_object):
        for attribute, value in vars(self).items():
            print(attribute, " ", value)
    #
    
    
    def __del__(self):
        del self.id
        del self.name
        #del self.mobile
        del self.dateOfBirth
        del self.referredBy
        del self.maritalStatus
        del self.breastFeed
        del self.ageAtFirstPregnancy
        del self.bcFamilyHistory
        del self.bcSelfHistory
        del self.breastProfile
        del self.radiationHistory
        del self.medConsumptionHistory
        del self.remarks
        self.scans.clear()
        del self.scans

'''
anomalies = []
getAge()
setAge()
getDate()
getImageArray()
getAnomalyArray()
setAnomalyImage(img, idx)
'''