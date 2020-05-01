import cv2
from PIL import Image
from matplotlib import pyplot as plt

imageName = "dark.tif"
img = Image.open(imageName)
img = img.convert("L")
width, height = img.size

array = []
for x in range(width):
    for y in range(height):
        pixel = img.getpixel((x, y))
        array.append(pixel)


plt.hist(array, 255, facecolor='blue', alpha=0.5)
plt.show()

img = cv2.imread('dark.tif', 0)

# find frequency of pixels in range 0-255
histr = cv2.calcHist([img], [0], None, [256], [0, 256])

# show the plotting graph of an image
plt.plot(histr)
plt.show()