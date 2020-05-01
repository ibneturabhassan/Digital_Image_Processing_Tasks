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

equ = cv2.equalizeHist(img)

cv2.imshow("After", equ)
cv2.waitKey()
histr2 = cv2.calcHist([equ], [0], None, [256], [0, 256])
plt.plot(histr2)
plt.show()
