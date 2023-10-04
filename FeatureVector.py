import cv2 as cv
import numpy as np
from scipy import stats
from skimage.feature import greycomatrix, greycoprops
#from skimage.measure import shannon_entropy
from sklearn.metrics.cluster import entropy
#import time

class FeatureVector():
    '''
        This function calculates the color moments like  mean, standard deviation, skewness, kurtosis 
    '''
    def color_moments(self, img, pix_pos, channel, vector):
        temp = list()
        for i in pix_pos:
            temp.append(img[i[0]][i[1]][channel])

        result = stats.describe(temp)
        vector.append(result.mean)
        vector.append(np.sqrt(result.variance))
        vector.append(result.skewness)
        vector.append(result.kurtosis)


    #time start
    #start = time.time()

    #images = ['004_res.png','001_res.png','002_res.png','003_res.png','005_res.png','006_res.png','007_res.png','008_res.png']

    #bgr = cv.imread(images[0])

    def Features(self, bgr):
        '''
            This function will find the 12 color moments and 20 texture moments
        '''
        pixel_present = list()

        count = 0
        size = bgr.shape
        for i in range(size[0]):
            for j in range(size[1]):
                if bgr[i][j][0]>0 or bgr[i][j][1]>0 or bgr[i][j][2]>0:
                        pixel_present.append((i,j))
                        count+=1

        feature_vec = list()

        self.color_moments(bgr, pixel_present, 0, feature_vec)      #blue

        self.color_moments(bgr, pixel_present, 1, feature_vec)      #green

        self.color_moments(bgr, pixel_present, 2, feature_vec)      #red

        #print("color moments", feature_vec)



        #Texture feature

        gray_img = cv.cvtColor(bgr, cv.COLOR_BGR2GRAY)


        mat = greycomatrix(gray_img, distances = [1], angles = [0, np.pi/4, np.pi/2, 3*np.pi/4], levels = 256 )
        #normed = True

        entropy_1 = entropy(mat[:,:,0,0])
        entropy_2 = entropy(mat[:,:,0,1])
        entropy_3 = entropy(mat[:,:,0,2])
        entropy_4 = entropy(mat[:,:,0,3])

        energy = greycoprops(mat, 'energy')
        contrast = greycoprops(mat, 'contrast')
        homogeneity = greycoprops(mat, 'homogeneity')
        correlation = greycoprops(mat, 'correlation')

        #print(energy)
        for i in energy:
            for j in i:
                feature_vec.append(j)
        for i in contrast:
            for j in i:
                feature_vec.append(j)
        for i in homogeneity:
            for j in i:
                feature_vec.append(j)
        for i in correlation:
            for j in i:
                feature_vec.append(j)
        feature_vec.append(entropy_1)
        feature_vec.append(entropy_2)
        feature_vec.append(entropy_3)
        feature_vec.append(entropy_4)

        #name = ['blue_mean','blue_standard deviation', 'blue_skewness', 'blue_kurtosis', 'green_mean', 'green_standard deviation', 'green_skewness', 'green_kurtosis','red_mean', 'red_standard deviation', 'red_skewness', 'red_kurtosis', 'energy_horizontal', 'energy_diagonal_1','energy_vertical','energy_diagonal_2', 'contrast_horizontal', 'contrast_diagonal_1', 'contrast_vertical', 'contrast_diagonal_2', 'homogeneity_horizontal', 'homogeneity_diagonal_1', 'homogeneity_vertical', 'homogeneity_diagonal_2', 'correlation_horizontal', 'correlation_diagonal_1', 'correlation_vertical', 'correlation_diagonal_2', 'entropy_horizontal', 'entropy_diagonal_1', 'entropy_vertical', 'entropy_diagonal_2']

        #print(len(feature_vec))
        #for i in range(32):
        #    print('{} : {}'.format(name[i],feature_vec[i]))
        
        return feature_vec


'''
ob1 = FeatureVector()
#img = cv.imread('001_res.png')
img = cv.imread('thermal_image.jpg')
img = cv.resize(img, (640, 480), interpolation = cv.INTER_LANCZOS4)
res = ob1.Features(img)
#print(ob1.Features(img))
print(res)
print(type(res))
'''
