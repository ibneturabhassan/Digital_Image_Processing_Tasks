import tkinter
from tkinter import *
import cv2
from matplotlib import pyplot as plt
import numpy as np

def show_values(img):
    height, width = img.shape[:2]

    print(height)
    print(width)
    c = 255 / (np.log(1 + np.max(img)))

    for y in range(width):
        for x in range(height):
            img[x][y] = 1 * pow(img[x][y], w2.get())

    cv2.imshow("After", img)
    cv2.waitKey()
    histr1 = cv2.calcHist([img], [0], None, [256], [0, 256])
    plt.plot(histr1)
    plt.show()

    return 1


master = Tk()
w2 = Scale(master, from_=0, to=7, orient=HORIZONTAL, length=500)
w2.pack()
Button(master, text='Show', command=lambda:show_values(img)).pack()
img = cv2.imread("aerial.tif", 0)
cv2.imshow("Before", img)
cv2.waitKey()
histr = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(histr)
plt.show()

mainloop()