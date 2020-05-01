import cv2
from matplotlib import pyplot as plt

img = cv2.imread('coins.jpg', 1)

# plot histogram of the given image
histr = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(histr)
plt.show()

# apply threshold on the given image... sets foreground to 0
ret, thresh = cv2.threshold(img, 130, 240, cv2.THRESH_BINARY)
cv2.imshow("image", thresh)
cv2.waitKey(0)

# displays histogram of the mask
histr = cv2.calcHist([thresh], [0], None, [256], [0, 256])
plt.plot(histr)
plt.show()

# applying bitwise or
final_img = cv2.bitwise_or(img, thresh)
cv2.imshow("image", final_img)
cv2.waitKey(0)
