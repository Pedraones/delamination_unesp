import cv2
from cv2 import COLOR_RGB2GRAY, cvtColor

img = cv2.imread('images/d10.bmp')

img_res = img[00:1530, 250:1800]

cols = img_res.shape[1]
lines = img_res.shape[0]
  
center_x = int(cols / 2)
center_y = int((lines / 2))

diam_drill = int((cols / 180)*83.5)

diam_delamina = int(lines/1.97)
thickness = 2

drill_circle = cv2.circle(img_res, (center_x, center_y), diam_drill, (200,200,25), thickness=thickness)

delamina_circle = cv2.circle(img_res, (center_x, center_y), diam_delamina, (200,200,25), thickness=thickness)

img_gray = cvtColor(img_res, COLOR_RGB2GRAY)

wResi = int(cols / 3)
hResi = int(lines / 3)

#os cv2's abaixo exibem a imagem em uma janela

cv2.namedWindow('img_process', cv2.WINDOW_NORMAL)
cv2.imshow('img_process', img_res)
cv2.resizeWindow('img_process', wResi,hResi)

print('Colunas: ' + str(cols) + ' Linhas: ' + str(lines))

#cv2.imwrite('saida.png', img_resize) #salva a imagem q esta dentro da variavel IMG

cv2.waitKey()