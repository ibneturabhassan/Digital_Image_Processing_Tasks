from datetime import datetime
from tkinter import *
import cv2

import numpy as np

def show_values():
    img = cv2.imread("aerial.tif", 0)
    height, width = img.shape[:2]

    print("Number of pixels: "+str(height*width))

    t1 = datetime.now()
    mapper = np.zeros((8, 256))
    for x in range(7):
        for y in range(255):
            mapper[x][y] = y^x

    c = 255 / (np.log(1 + np.max(img)))
    for y in range(width):
        for x in range(height):
            img[x][y] = mapper[w2.get()][img[x][y]]

    t2 = datetime.now()
    print("Time difference using mapping")
    print(t2-t1)

    t1 = datetime.now()
    c = 255 / (np.log(1 + np.max(img)))
    for y in range(width):
        for x in range(height):
            img[x][y] = 1 * pow(img[x][y], w2.get())

    t2 = datetime.now()
    print("Time difference using nested loops")
    print(t2 - t1)

    return 1


master = Tk()
w2 = Scale(master, from_=0, to=7, orient=HORIZONTAL, length=500)
w2.pack()
Button(master, text='Show', command=show_values).pack()



mainloop()