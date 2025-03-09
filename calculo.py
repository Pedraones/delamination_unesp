import cv2
from cv2 import cvtColor, COLOR_RGB2GRAY

img = cv2.imread("delaminacao.png")

cols = img.shape[1]
lines = img.shape[0]

img_gray = cvtColor(img, COLOR_RGB2GRAY)

count_bits = 0

for x in range(lines):
    for y in range(cols):
        if img_gray[x, y] == 0:
            count_bits += 1

print("Bits pretos: " + str(count_bits))