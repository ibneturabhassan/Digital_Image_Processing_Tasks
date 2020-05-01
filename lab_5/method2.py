import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("img1.jpg", 0)

cv2.imshow("Before", img)
cv2.waitKey()
histr = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(histr)
plt.show()
height, width = img.shape[:2]

print(height)
print(width)
c = 255/(np.log(1 + np.max(img)))
maximum = np.max(img)
minimum = np.min(img)

for x in range(height):
    for y in range(width):
        img[x][y] = ((img[x][y] -minimum) / (maximum - minimum))*255.



cv2.imshow("After", img)
cv2.waitKey()
histr2 = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(histr2)
plt.show()