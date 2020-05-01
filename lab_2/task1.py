from PIL import Image



def downSize(img, factor):
    width, height = img.size
    nwidth = int(width / factor)
    nheight = int(height / factor)
    newImage = Image.new("L", (nwidth, nheight), "red")
    for x in range(0, width, factor):
        for y in range(0, height, factor):
            pixel = img.getpixel((x, y))
            newImage.putpixel((int(x / factor), int(y / factor)), pixel)

    return newImage


img = Image.open("lena.tiff")
img = img.convert("L")
Imgf2 = downSize(img, 2)
Imgf4 = downSize(img, 4)


img.show()
Imgf2.show()
Imgf4.show()
