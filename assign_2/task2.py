import cv2
import numpy as np

image = cv2.imread('2.png', 0)

kernel = np.ones((6, 6), np.uint8)
ret, thresh = cv2.threshold(image, 60, 255, cv2.THRESH_BINARY)
erosion = cv2.erode(thresh, kernel, iterations=2)
dilation = cv2.dilate(erosion, kernel, iterations=2)

cv2.imshow('Input Image', image)
cv2.imshow('Output Image', dilation)

cv2.waitKey(0)