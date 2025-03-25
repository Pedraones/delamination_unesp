import image

cols = image.cols
lines = image.lines

def diameters():
    diam_drill = int((cols / 180)*83.5)

    diam_delamina = int(lines/1.97)

    diam_drill_mm = diam_drill / 238.9869
    diam_delamina_mm = diam_delamina / 238.9869

    return diam_drill_mm, diam_delamina_mm

def delamina(diam_drill_mm, diam_delamina_mm):
    pi = 3.141592
    ray_drill = diam_drill_mm/2
    ray_delamina = diam_delamina_mm/2

    area_less = 2*pi*int(ray_drill*ray_drill)
    area_bigger = 2*pi*int(ray_delamina*ray_delamina)

    Fd = diam_delamina_mm/diam_drill_mm
    Fa = area_bigger/area_less

    return print("Fator de delaminação pelos diâmetros: " + str(Fd) + "\n Fator de delaminação pelas áreas: " + str(Fa))