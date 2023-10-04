import cv2 as cv
import numpy as np

def KMeansBackgroundElimination(img):
    k = 2
    image = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    
    # converting RGB image matrix into array of float values for opencv kmeans procedure
    pixel_vals = image.reshape((-1,3))
    pixel_vals = np.float32(pixel_vals)
    
    # kmeans setup and execution
    # setting iterations to 100 and accuracy to 85%
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.85)
    # calling kmeans function of opencv
    retval, labels, centers = cv.kmeans(pixel_vals, k, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)
    
    # converting segmentation result from float array to RGB matrix
    centers = np.uint8(centers)
    segmented_data = centers[labels.flatten()]
    segmented_image = segmented_data.reshape((image.shape))
    
    # converting result into Binary format (0(Black), 255(White))
    segmented_image = cv.cvtColor(segmented_image, cv.COLOR_RGB2BGR)
    segmented_gray_image = cv.cvtColor(segmented_image, cv.COLOR_BGR2GRAY)
    bwThresh, segmented_bw_image = cv.threshold(segmented_gray_image, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    return segmented_bw_image

image = cv.imread("thermal_image.jpg")
result = KMeansBackgroundElimination(image)
edges = cv.Canny(result, 0, 255)
cv.imshow("input", image)
cv.imshow("result", result)
cv.imshow("edges", edges)
cv.waitKey()
