from PIL import Image
import numpy as npy

def upSize(img, factor):
    width, height = img.size
    nwidth = int(width*factor)
    nheight = int(height*factor)
    imgO = npy.zeros([width, height], dtype=int)
    Imgarr = npy.zeros([nwidth, nheight], dtype=int)
    counter = 0
    imgO = npy.array(img)


    for x in range(0, width, 2):

        for y in range(0, height, 2):
            blue = imgO[x][y]
            green = imgO[x+1][y]
            red = imgO[x][y+1]
            purple = imgO[x+1][y+1]

            if ((x + counter >= nwidth) or (y + counter>= nheight)):
                break
            Imgarr[x + counter][y + counter] = blue
            Imgarr[x + counter+2][y + counter] = green
            Imgarr[x + counter][y + counter+2] = red
            Imgarr[x + counter+2][y + counter+2] = purple

            Imgarr[x + counter][y + counter+1] = int((int(blue)+int(green))/2)
            Imgarr[x + counter+1][y + counter] = int((int(blue)+int(red))/2)
            Imgarr[x + counter + 2][y + counter + 1] = int((int(purple)+int(red))/2)
            Imgarr[x + counter + 1][y + counter + 2] = int((int(purple)+int(green))/2)
            Imgarr[x + counter + 1][y + counter + 1] = int((int(purple) + int(green) + int(red) + int(blue))/4)
            if ((x == 2) and (y == 2)):
                print(Imgarr[x + counter+1][y + counter+1])
                print(Imgarr[x + counter+1][y + counter])
                print(Imgarr[x + counter+2][y + counter+1])
                print(Imgarr[x + counter+1][y + counter+2])
                print(Imgarr[x + counter+1][y + counter+1])


        counter += 1

    print(imgO[2:4, :])
    print(Imgarr[3:6, :])
    return Imgarr


img = Image.open("lena.tiff")
img = img.convert("L")
Imgf2 = upSize(img, 2)

img.show()

Image.fromarray(Imgf2, mode='L').show()