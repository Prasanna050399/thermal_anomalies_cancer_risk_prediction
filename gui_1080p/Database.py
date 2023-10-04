from datetime import datetime, date
import cv2 as cv
import numpy as np
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import gridfs

class Database:
    def __init__(self):
        self.client = None
        
    def openConnection(self):
        self.client = MongoClient()
        try:
            self.client.admin.command("ismaster")
            self.db =self.client.Patient
            self.patientInformation = self.db.Information
            self.imageStore = self.db.Images
            self.fs = gridfs.GridFS(self.db)
        except ConnectionFailure:
            self.client.close()
            self.client = None
            return False
        return True
    
    def closeConnection(self):
        if self.client is not None:
            self.client.close()
            self.client = None
        
    def getPatientInformationFromDB(self, patientId):
        ret = self.patientInformation.find_one( {"_id" : patientId} )
        result = {}
        if ret is not None:
            result["PatientId"] = ret["_id"]
            result["ReferedBy"] = ret["ReferedBy"]
            result["Name"] = ret["Name"]
            result["DOB"] = ret["DOB"]
            result["MobileNo"] = ret["MobileNo"]
            result["MaritalStatus"] = ret["MaritalStatus"]
            result["BreastFeed"] = ret["BreastFeed"]
            result["AgeAtFirstPregnancy"] = ret["AgeAtFirstPregnancy"]
            result["BCFamilyHistory"] = ret["BCFamilyHistory"]
            result["BCSelfHistory"] = ret["BCSelfHistory"]
            result["BreastProfile"] = ret["BreastProfile"]
            result["RadiationHistory"] = ret["RadiationHistory"]
            result["MedConsumptionHistory"] = ret["MedConsumptionHistory"]
            result["SpecialRemarks"] = ret["SpecialRemarks"]
            return result
        return None
    
    def savePatientInformationInDB(self, arr, isNew):
        Information = {
            "_id" : arr["PatientId"],
            "ReferedBy": arr["ReferedBy"],
            "Name": arr["Name"],
            "DOB": arr["DOB"],
            "MobileNo" : arr["MobileNo"],
            "MaritalStatus" : arr["MaritalStatus"],
            "BreastFeed": arr["BreastFeed"],
            "AgeAtFirstPregnancy":arr["AgeAtFirstPregnancy"],
            "BCFamilyHistory": arr["BCFamilyHistory"],
            "BCSelfHistory": arr["BCSelfHistory"],
            "BreastProfile": arr["BreastProfile"],
            "RadiationHistory": arr["RadiationHistory"],
            "MedConsumptionHistory": arr["MedConsumptionHistory"],
            "SpecialRemarks" : arr["SpecialRemarks"]
        }
        
        # saving new patient data
        if(isNew == True):
            self.patientInformation.insert_one(Information)
            patientImageCollection = {
                "_id" : arr["PatientId"],
                "visits" : []
            }
            self.imageStore.insert_one(patientImageCollection)
        
        # saving existing patient data
        else:
            self.patientInformation.update_one( {'_id' : arr["PatientId"]}, {"$set" : Information} )
        
    def getPatientVisitDataFromDB(self, patientId, visitDate):
        patientVisitCursor = self.imageStore.find_one( { "_id" : patientId } )["visits"]
        
        scans = [None, None, None, None, None]
        anomalies = [None, None, None, None, None]
        edges = [None, None, None, None, None]
        diagnosticScore = None
        remarks = None
        
        for visit in patientVisitCursor:
            if visit["VisitDate"] == visitDate:
                diagnosticScore = visit["DiagnosticScore"]
                remarks = visit["Remarks"]
                for i in range(5):
                    readimg1 = self.fs.get( visit["OriginalImages"][i]["ImageID"] )
                    readimg1 = np.frombuffer( readimg1.read(), dtype=np.uint8 )
                    readimg1 = np.reshape( readimg1, visit["OriginalImages"][i]["ImageShape"] )
                    scans[i] = readimg1
                    
                    readimg2 = self.fs.get( visit["AnomalyImages"][i]["ImageID"] )
                    readimg2 = np.frombuffer( readimg2.read(), dtype=np.uint8 )
                    readimg2 = np.reshape( readimg2, visit["AnomalyImages"][i]["ImageShape"] )
                    anomalies[i] = readimg2
                    
                    readimg3 = self.fs.get( visit["EdgeImages"][i]["ImageID"] )
                    readimg3 = np.frombuffer( readimg3.read(), dtype=np.uint8 )
                    readimg3 = np.reshape( readimg3, visit["EdgeImages"][i]["ImageShape"] )
                    edges[i] = readimg3
        
        return { "PatientID" : patientId, "VisitDate" : visitDate, "OriginalImages" : scans, "AnomalyImages" : anomalies, "EdgeImages" : edges, "DiagnosticScore" : diagnosticScore, "Remarks" : remarks }
    
    def savePatientVisitDataInDB(self, arr):
        patientId = arr["PatientID"]
        visitDate = arr["VisitDate"]
        original = [None, None, None, None, None]
        anomalies = [None, None, None, None, None]
        edges = [None, None, None, None, None]
        diagnosticScore = arr["DiagnosticScore"]
        remarks = arr["Remarks"]
        
        for i in range(5):
            original[i] = arr["OriginalImages"][i].copy()
            anomalies[i] = arr["AnomalyImages"][i].copy()
            edges[i] = arr["EdgeImages"][i].copy()
        
        originalId = []
        anomaliesId= []
        edgesId = []
        
        for i in range(6):
            originalId.append( self.fs.put( original[i].tobytes(), encoding="utf-8" ) )
            anomaliesId.append( self.fs.put( anomalies[i].tobytes(), encoding="utf-8" ) )
            edgesId.append( self.fs.put( edges[i].tobytes(), encoding="utf-8" ) )
        
        visit = {
            "VisitDate" : visitDate,
            
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
            ],
            
            "DiagnosticScore" : diagnosticScore,
            
            "Remarks" : remarks
        }
        
        self.imageStore.update_one( { "_id" : patientId } , { "$push" : { "visits" : visit } } )
        
    def searchInDB(self, searchMethod, query):
        ret = self.patientInformation.find({ searchMethod : { "$regex" : "^"+query } })
        result = []
        for entry in ret:
            patientId = entry["_id"]
            patientName = entry["Name"]
            patientMobile = entry["MobileNo"]
            #temp = patientId + " " + patientName + " " + patientMobile
            temp = [patientId, patientName, patientMobile]
            result.append(temp)
        return result
    
    def findPatientVisitDates(self, patientId):
        patientVisitCursor = self.imageStore.find_one( { "_id" : patientId } )["visits"]
        visitDates = []
        for visit in patientVisitCursor:
            visitDates.append(visit["VisitDate"])
        return visitDates
    