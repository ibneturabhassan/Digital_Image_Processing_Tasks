import numpy as np
import cv2
import matplotlib.pyplot as plt


def TwoPassAlgo(input_img):
    # first pass
    count = 0;
    invcount = 0;
    table = np.zeros(500, np.uint32)
    rows, columns = input_img.shape
    for i in range(rows):
        for j in range(columns):
            if (input_img[i, j] == 0):
                continue;
            else:
                if (i == 0 and j == 0):
                    count += 1;
                    input_img[0, 0] = count;
                    table[count] = count;
                elif (i == 0 and j != 0):
                    if (input_img[0, j - 1] != 0):
                        input_img[0, j] = input_img[0, j - 1];
                    else:
                        count += 1;
                        input_img[0, j] = count;
                        table[count] = count;
                elif (i != 0 and j == 0):
                    if (input_img[i - 1, 0] != 0):
                        input_img[i, 0] = input_img[i - 1, 0]
                    else:
                        count += 1;
                        input_img[i, 0] = count;
                        table[count] = count;
                else:
                    top = input_img[i - 1, j];
                    left = input_img[i, j - 1];
                    if (top == 0 and left == 0):
                        count += 1
                        input_img[i, j] = count;
                        table[count] = count;
                    elif (top == 0 and left != 0):
                        input_img[i, j] = left;
                    elif (left == 0 and top != 0):
                        input_img[i, j] = top;
                    elif (top != 0 and left != 0):
                        if (left == top):
                            input_img[i, j] = left;
                        elif (top < left):
                            input_img[i, j] = top;
                            # table[table[left]]=top;
                            label = left
                            while (table[label] != label):
                                prev = label
                                label = table[label]
                                table[prev] = top
                            if (table[label] > top):
                                table[label] = top;
                            else:
                                table[top] = label;
                            invcount += 1;
                        elif (left < top):
                            input_img[i, j] = left;
                            # table[table[top]]=left;
                            label = top
                            while (table[label] != label):
                                prev = label
                                label = table[label]
                                table[prev] = left
                            if (table[label] > left):
                                table[label] = left;
                            else:
                                table[left] = label;
                            invcount += 1;
    # end first pass

    # second pass
    for i in range(rows):
        for j in range(columns):
            if (input_img[i, j] != 0):
                label = int(table[int(input_img[i, j])]);
                while (label != table[label]):
                    label = table[label]
                table[int(input_img[i, j])] = label;
                input_img[i, j] = table[label];

    # getting number of segments
    segments = count;
    for i in range(count + 1):
        if (table[i] != i):
            segments -= 1;

    return [input_img, table, segments]


img_array = cv2.imread('cc.png', cv2.IMREAD_GRAYSCALE)
img_array.shape
cv2.imshow("img", img_array)
ret, binary_img = cv2.threshold(img_array, 100, 255, cv2.THRESH_BINARY)

plt.imshow(binary_img)
cv2.waitKey(0)
img_mask, img_table, img_segments = TwoPassAlgo(binary_img)

img_mask, img_table, img_segments

plt.imshow(img_mask)
cv2.waitKey(0)

print(img_segments-1)
