import cv2
from cv2 import cvtColor, COLOR_RGB2GRAY

img = cv2.imread("delaminacao.png")

cols = img.shape[1]
lines = img.shape[0]
pi = 3.141592

diam_drill = int((cols / 180)*83.5)

diam_delamina = int(lines/1.97)

diam_drill_mm = diam_drill / 238.9869
diam_delamina_mm = diam_delamina / 238.9869

area_less = 2*pi*(diam_drill_mm/2)
area_bigger = 2*pi*(diam_delamina_mm/2)

Fd = diam_delamina_mm/diam_drill_mm
Fa = area_bigger/area_less

print("Fator de delaminação pelos diâmetros: " + str(Fd))
print("Fator de delaminação pelas áreas: " + str(Fa))