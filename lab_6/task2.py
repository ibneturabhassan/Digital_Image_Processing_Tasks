import cv2
import numpy as np
from matplotlib import pyplot as pyp

img = cv2.imread('lowcon.tif',0)
height, width = img.shape[:2]
Rmax=np.amax(img)
Rmin=np.amin(img)
Smax=255
Smin=0
ratio = (Smax-Smin)/(Rmax-Rmin)
table = np.zeros(256, dtype=int)

hist = cv2.calcHist([img],[0],None,[256],[0,255])
pyp.plot(hist)
pyp.xlim([0,256])
pyp.show()

for R in range(Rmin,Rmax+1):
  S=ratio*(R-Rmin)+Smin
  table[R] = S

for row in range(height):
  for col in range(width):
    img[row][col]=table[img[row][col]]

hist = cv2.calcHist([img],[0],None,[256],[0,255])
pyp.plot(hist)
pyp.xlim([0,256])
pyp.show()

print(Rmin)
print(Rmax)
cv2.imshow("image", img)
cv2.waitKey()
