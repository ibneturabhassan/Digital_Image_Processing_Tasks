import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("bright.tif", 0)
height, width = img.shape[:2]

cv2.imshow("Before", img)
cv2.waitKey()
histr = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(histr)
plt.show()


h = [0.0]*256
for x in range(height):
    for y in range(width):
        h[img[x, y]] +=1
h = np.array(h)/(width*height)
cdf = np.cumsum(h)
sk = np.uint8(255*cdf)
newImg = np.zeros_like(img)
for x in range(height):
    for y in range(width):
        newImg[x, y] = sk[img[x, y]]


cv2.imshow("After", newImg)
cv2.waitKey()
histr = cv2.calcHist([newImg], [0], None, [256], [0, 256])
plt.plot(histr)
plt.show()

histr2 = cv2.calcHist([newImg], [0], None, [256], [0, 256])
plt.plot(histr2)
plt.show()