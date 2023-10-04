#BGR
import cv2
import matplotlib.pyplot as plt
import numpy as np
from timeit import default_timer as timer

class AnomalyDetection():

    def __init__(self, original, image, grayLevel):
        self.orig = original.copy()
        self.roi = image.copy()
        self.grayLevel = grayLevel

    
    def detect(self):
        '''
            This function first applies details enhancment function to
            the roi image which is followed by k means clustering. After
            that we are converting the image into gray scale to apply
            threshold value. The value used is 15%. This is used to find
            the anomaly within the image. Once the anomaly is found then
            we are just highlighting the pixel for cold and hot anomaly i.e red and blue.
        '''
        #image = cv2.resize(self.roi, (640, 480), interpolation = cv2.INTER_LANCZOS4)
        #self.orig = cv2.resize(self.orig, (640, 480), interpolation = cv2.INTER_LANCZOS4)
        image = self.roi
        img_enhanced = cv2.detailEnhance(image, sigma_s=10, sigma_r=0.15)
        
        # convert to RGB
        img = cv2.cvtColor(img_enhanced, cv2.COLOR_BGR2RGB)
        
        Z = img.reshape((-1,3))

        # convert to np.float32
        Z = np.float32(Z)

        # define criteria, number of clusters(K) and apply kmeans()
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        K = 8
        ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

        # Now convert back into uint8, and make original image
        center = np.uint8(center)
        res = center[label.flatten()]
        res2 = res.reshape((img.shape))

        coefficients = [0.1,0.6,0.1]
        # Gives blue channel all the weight
        # for standard gray conversion, coefficients = [0.114, 0.587, 0.299]
        m = np.array(coefficients).reshape((1,3))
        gray = cv2.transform(res2, m)
        avg = self.grayLevel

        #finding the anomaly pixels 
        position = list()
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                if gray[i][j] > 0 :
                    temp = avg - gray[i][j]
                    if temp > avg*15/100:
                        position.append((i,j))

        #highligting the pixels
        for x,y in position:
            if self.orig[x][y][0] < self.orig[x][y][2]:
                #red
                self.orig[x][y] = [100,100,200]
            elif self.orig[x][y][0] > self.orig[x][y][2]:
                #blue
                self.orig[x][y] = [200,100,100]
##            else:
##                # yellow
##                self.orig[x][y] = [100,100,200]
        
        return self.orig

'''
coordinates = list()
def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 3, (255, 255, 255), 2)
        coordinates.append((y,x))
        print(x, y, img[y][x])
        cv2.imshow('image',img)
        cv2.waitKey()

def getGrayLevel(image, x, y):
    temp = image.copy()
    coefficients = [0.1,0.6,0.1]
    m = np.array(coefficients).reshape((1,3))
    gray = cv2.transform(temp, m)
    avg = 0
    count = 0
    for i in range(x-1,x+2):
        if i >= 480 or i < 0:
            continue
        for j in range(y-1,y+2):
            if j >= 640 or j < 0:
                continue
            else:
                avg += gray[i][j]
                count += 1
    avg /= count
    return round(avg)
'''

'''
#roi_images = ['i1.jpg','i2.jpg','i3.jpg','i4.jpg','i5.jpg']
#images = ["007.jpg", "014.jpg", "031.png", "012.jpg", "013.jpg" ]
images = ["thermal_image.jpg"]
roi_images = ["roi.jpg"]
#7,14,031,12,13
for i in range(len(images)):
    img = cv2.imread(images[i])
    img = cv2.resize(img, (640, 480), interpolation = cv2.INTER_LANCZOS4)
    image = cv2.imread(images[i])
    image = cv2.resize(image, (640, 480), interpolation = cv2.INTER_LANCZOS4)
    roi = cv2.imread(roi_images[i])
    roi = cv2.resize(roi, (640, 480), interpolation = cv2.INTER_LANCZOS4)
    
    cv2.imshow('image',img)
    cv2.setMouseCallback('image',click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    coor = coordinates.pop()
    x, y = coor
    grayLevel = getGrayLevel(image, x, y)
    
    t1 = timer()
    ob1 = AnomalyDetection(image, roi, grayLevel)
    img = ob1.detect()
    t2 = timer()
    
    print(t2-t1)
    cv2.imshow('img',img)
    cv2.waitKey()
'''
