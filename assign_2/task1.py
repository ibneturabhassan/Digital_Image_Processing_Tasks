import cv2
import numpy as np

image = cv2.imread('1.png', 0)

kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(image, kernel, iterations=1)
dilation = cv2.dilate(erosion, kernel, iterations=1)

cv2.imshow('Input Image', image)
cv2.imshow('After Erosion', erosion)
cv2.imshow('After Dilation', dilation)

cv2.waitKey(0)