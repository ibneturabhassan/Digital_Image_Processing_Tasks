import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("kidney.tif", 0)
height, width = img.shape[:2]
mask = np.zeros(img.shape)

cv2.imshow("Before", img)
cv2.waitKey()
histr = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(histr)
plt.show()

for x in range(height):
    for y in range(width):
        if img[x, y] >= 135 and img[x][y] <= 255:
            mask[x, y] = 255
        else:
            mask[x, y] = 0

cv2.imshow("Mask", mask)
cv2.waitKey()


cv2.imwrite('mask.png', mask)

img1 = cv2.imread('kidney.tif', 0)
img2 = cv2.imread('mask.png', 0)
cv2.imshow("final image", img1 | img2)
cv2.waitKey()
