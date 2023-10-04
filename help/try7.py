import cv2 as cv
import numpy as np

image = cv.imread("mask1.jpg")
image = cv.resize(image, (640, 480), interpolation = cv.INTER_LANCZOS4)
image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
contours, hierarchy = cv.findContours(image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
hull = []
for i in range(len(contours)):
    print(contours[i])
    print()
    print()
    print()
    # creating convex hull object for each contour
    hull.append(cv.convexHull(contours[i], False))
# create an empty black image
drawing = np.zeros((image.shape[0], image.shape[1], 3), np.uint8)
# draw contours and hull points
for i in range(len(contours)):
    color_contours = (0, 255, 0) # green - color for contours
    color = (255, 255, 255) # blue - color for convex hull
    # draw ith contour
    cv.drawContours(drawing, contours, i, color_contours, 1, 8, hierarchy)
    # draw ith convex hull object
    cv.drawContours(drawing, hull, i, color, 1, 8)
cv.imshow("hull", drawing)
cv.waitKey()
