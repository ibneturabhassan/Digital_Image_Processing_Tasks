import cv2
import matplotlib.pyplot as plt
from skimage import morphology

img = cv2.imread('Objects.png', 0)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.show()

ellipseMask = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (76, 76))
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, ellipseMask)
plt.imshow(opening, cmap='gray')
plt.title('Circle')
plt.show()

ellipseMask = morphology.diamond(49)  # Kernel Size is 49*2+1 == (99,99)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, ellipseMask)
plt.imshow(opening, cmap='gray')
plt.title('Diamond')
plt.show()

ellipseMask = cv2.getStructuringElement(cv2.MORPH_RECT, (69, 69))
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, ellipseMask)
plt.imshow(opening, cmap='gray')
plt.title('Rectangle')
plt.show()
