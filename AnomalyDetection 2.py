import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

#images = ["001.png", "002.png", "003.png", "004.jpg", "005.jpg", "006.jpg", "007.jpg", "008.jpg", "009.jpg", "010.jpg", "011.jpg", "012.jpg", "013.jpg", "014.jpg", "015.jpg", "016.jpg", "017.jpg", "018.jpg", "019.jpg", "020.jpg", "021.jpg", "022.jpg", "023.jpg", "024.jpg", "025.jpg", "026.jpg", "027.png", "028.png", "029.png", "030.png", "031.png"]
#images = ["001.png", "002.png", "003.png", "004.jpg", "005.jpg", "006.jpg", "007.jpg", "008.jpg", "009.jpg", "010.jpg", "011.jpg", "012.jpg", "013.jpg", "014.jpg", "015.jpg"]

images = ["001_res.png", "002_res.png", "003_res.png", "004_res.png", "005_res.png", "006_res.png", "007_res.png", "008_res.png", "009_res.png", "010_res.png", "011_res.png", "012_res.png", "013_res.png", "014_res.png", "015_res.png"]

class AnomalyDetection:
    def __init__(self, image, roi):
        self.REDRLIMIT = 200 # 234 200
        self.REDGLIMIT = 180 # 190 180
        self.REDBLIMIT = 120 # 120
        self.BLUERLIMIT = 20 # 25 20
        self.BLUEGLIMIT = 225 # 245 225
        self.BLUEBLIMIT = 120 # 80 120
        self.roi = roi.copy()
        self.result = image.copy()
        #self.roi = cv.resize(self.roi, (640, 480), interpolation = cv.INTER_LANCZOS4)
        #self.result = cv.resize(self.result, (640, 480), interpolation = cv.INTER_LANCZOS4)
    def find_anomaly(self):
        rows, columns, _ = self.roi.shape
        for i in range(rows):
            for j in range(columns):
                b = self.roi[i][j][0]
                g = self.roi[i][j][1]
                r = self.roi[i][j][2]
                if r==0 and g==0 and b==0:
                    continue
                # red region anomaly detection
                if r >= self.REDRLIMIT and g <= self.REDGLIMIT and b <= self.REDBLIMIT:
                    self.result[i][j][0] = 32
                    self.result[i][j][1] = 67
                    self.result[i][j][2] = 125
                # blue region anomaly detection
                if r <= self.BLUERLIMIT and g <= self.BLUEGLIMIT and b >= self.BLUEBLIMIT:
                    self.result[i][j][0] = 147
                    self.result[i][j][1] = 47
                    self.result[i][j][2] = 106
        return
    def get_anomaly(self):
        return self.result

'''
if __name__ == "__main__":
    idx = 0
    for idx in range(idx, len(images)):
        print(images[idx])
        img = cv.imread(images[idx])
        img = cv.resize(img, (640, 480), interpolation = cv.INTER_LANCZOS4)
        #img = cv.edgePreservingFilter(img, flags=1, sigma_s=60, sigma_r=0.4)
        imgEnhance = cv.detailEnhance(img, sigma_s=10, sigma_r=0.15)
        #img = imgEnhance
        #imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        
        obj = AnomalyDetection(img, img)
        obj.find_anomaly()
        result = obj.get_anomaly()
        #img = cv.edgePreservingFilter(img, flags=1, sigma_s=60, sigma_r=0.4)
        #img = cv.detailEnhance(img, sigma_s=10, sigma_r=0.15)
        imgGray = cv.cvtColor(imgEnhance, cv.COLOR_BGR2GRAY)
        #highThresh = str(input("Threshold: "))
        highThresh, _ = cv.threshold(imgGray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
        lowThresh = 0.5 * highThresh
        print("Threshold:", lowThresh, "-", highThresh)
        temp = ""
        while True:
            #print("inside while loop")
            #highThresh, _ = cv.threshold(imgGray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
            edges = cv.Canny(imgGray, lowThresh, highThresh)
            kernel = np.ones((5,5), np.uint8)
            #edges = cv.dilate(edges, kernel, iterations=1)
            #edges = cv.morphologyEx(edges, cv.MORPH_OPEN, kernel)
            #edges = cv.morphologyEx(edges, cv.MORPH_CLOSE, kernel)
            
            cv.imshow(images[idx], result)
            #cv.imshow("rgb", img)
            cv.imshow("edges", edges)
            #cv.imshow("gray", imgGray)
            
            #plt.imshow(imgRGB)
            #plt.show()
            
            cv.waitKey()
            #break
            #print("done")
            temp = str(input("\nEnter Threshold: "))
            if temp == "next":
                break
            temp = temp.strip()
            temp = temp.split()
            if len(temp) is 1:
                highThresh = int(temp[0])
                lowThresh = int(0.5 * highThresh)
            elif len(temp) is 2:
                lowThresh = int(temp[0])
                highThresh = int(temp[1])
            print("Threshold: ", lowThresh, "-", highThresh)
'''
