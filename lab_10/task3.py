import cv2
import matplotlib.pyplot as plt
from scipy import ndimage

img = cv2.imread('Fig01.tif')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.show()

img2 = ndimage.grey_dilation(img, size=(2, 2))
plt.imshow(img2, cmap='gray')
plt.title('2x2 Dilation')
plt.show()

img2 = ndimage.grey_dilation(img, size=(3, 3))
plt.imshow(img2, cmap='gray')
plt.title('3x3 Dilation')
plt.show()

img2 = ndimage.grey_dilation(img, size=(5, 5))
plt.imshow(img2, cmap='gray')
plt.title('5x5 Dilation')
plt.show()

img2 = ndimage.grey_erosion(img, size=(2, 2))
plt.imshow(img2, cmap='gray')
plt.title('2x2 Erosion')
plt.show()

img2 = ndimage.grey_erosion(img, size=(3, 3))
plt.imshow(img2, cmap='gray')
plt.title('3x3 Erosion')
plt.show()

img2 = ndimage.grey_erosion(img, size=(5, 5))
plt.imshow(img2, cmap='gray')
plt.title('5x5 Erosion')
plt.show()
