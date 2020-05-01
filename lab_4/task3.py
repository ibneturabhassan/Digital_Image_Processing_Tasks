import cv2
import numpy as np

img = cv2.imread("dark.tif", 0)

rows, cols = img.shape

M = np.float32([[1, 0, 100], [0, 1, 50]])
translation = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow("translation", translation)
cv2.waitKey(0)
cv2.destroyAllWindows()

M = cv2.getRotationMatrix2D((rows / 2, cols / 2), 60, 1)
rotation = cv2.warpAffine(img, M, (cols*2, rows*2))
cv2.imshow("rotation", rotation)
cv2.waitKey(0)
cv2.destroyAllWindows()

M = np.float32([[1, 0, 0], [0.5, 1, 0]])
sheerx = cv2.warpAffine(img, M, (cols*2, rows*2))
cv2.imshow("sheer-X", sheerx)
cv2.waitKey(0)
cv2.destroyAllWindows()

M = np.float32([[1, 0.5, 0], [0, 1, 0]])
sheery = cv2.warpAffine(img, M, (cols*2, rows*2))
cv2.imshow("sheer-Y", sheery)
cv2.waitKey(0)
cv2.destroyAllWindows()