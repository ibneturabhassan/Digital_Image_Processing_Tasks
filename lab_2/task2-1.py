from PIL import Image


def upSize(img, factor):
    width, height = img.size
    nwidth = int(width * factor)
    nheight = int(height * factor)
    newImage = Image.new("L", (nwidth, nheight), "red")
    for x in range(0, nwidth):
        for y in range(0, nheight):
            pixel = img.getpixel((int(x / factor), int(y / factor)))
            newImage.putpixel((x, y), pixel)

    return newImage


img = Image.open("lena.tiff")
img = img.convert("L")
Imgf2 = upSize(img, 2)
Imgf4 = upSize(img, 4)


img.show()
Imgf2.show()
Imgf4.show()
