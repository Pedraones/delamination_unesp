import cv2
from cv2 import COLOR_RGB2GRAY, cvtColor

img = cv2.imread('d10.bmp')
  
img_recort = img[00:1500, 280:1750]

img_gray = cvtColor(img_recort, COLOR_RGB2GRAY)

cols = img_gray.shape[1]
lines = (img_gray.shape[0])

wResi = int(cols / 3)
hResi = int(lines / 3)

#for esta alterando a cor dos pixels dentro do range d ambos os for para preto(0)

for x in range(lines):
    for y in range(cols):
        if img_gray[x, y] < 210:
            img_gray[x, y] = 255
        
        else:
            img_gray[x,y] = 0

#os cv2's abaixo exibem a imagem em uma janela

cv2.namedWindow('img_process', cv2.WINDOW_NORMAL)
cv2.imshow('img_process', img_gray)

cv2.resizeWindow('img_process', wResi,hResi)

print('Colunas: ' + str(cols) + ' Linhas: ' + str(lines))
#cv2.imwrite('saida.png', img) salva a imagem q esta dentro da variavel IMG

cv2.waitKey()