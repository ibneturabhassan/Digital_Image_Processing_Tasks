from PIL import Image
import numpy as np

def downSize(img, factor):
    width, height = img.size
    nwidth = int(width * factor)
    nheight = int(height * factor)
    newImage = Image.new("L", (nwidth, nheight), "red")
    for x in range(0, nwidth):
        for y in range(0, nheight):
            pixel = img.getpixel((int(x / factor), int(y / factor)))
            newImage.putpixel((x, y), pixel)

    return newImage


img = Image.open("cc.png")
img = img.convert("L")
width, height = img.size
width, height = 10, 10
matrix = np.zeros((width, height), dtype=int)
counter = 0
for x in range(0, width):
    for y in range(0, height):
        if img.getpixel((x,y)) == 255:
            matrix[x][y] = img.getpixel((x,y))
matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
          [0, 255, 0, 255, 0, 0, 0, 0, 0, 0, 0, ],
          [0, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, ],
          [0, 255, 0, 255, 0, 0, 0, 0, 0, 0, 0, ],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]
          ]

eq_list =np.zeros(255)
for x in range(0, width):
    for y in range(0, height):
        if matrix[x][y] == 255:
            if (matrix[x][y - 1] == 0 and matrix[x - 1][y] == 0):
                matrix[x][y] = counter
            if(matrix[x][y-1] == 0 and matrix[x-1][y] != 0):
                matrix[x][y] = matrix[x-1][y]
            if (matrix[x][y - 1] != 0 and matrix[x - 1][y] == 0):
                matrix[x][y] = matrix[x][y-1]

            if (matrix[x][y -1] == 0 and matrix[x - 1][y] == 0):
                counter +=1
                eq_list[counter] = counter
                matrix[x][y] = counter
            if (matrix[x][y -1] != 0 and matrix[x - 1][y] != 0):
                lowest = min(matrix[x][y -1], matrix[x-1][y])
                maximum = max(matrix[x][y - 1], matrix[x - 1][y])
                eq_list[maximum] = lowest
                matrix[x][y] = lowest
for x in range(0, width):
    for y in range(0, height):
        matrix[x][y] = eq_list[matrix[x][y]]

print(counter)
print(np.unique(eq_list).size-1)
img.show()