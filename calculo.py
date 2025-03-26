import image as img


def diameters():
    cols = img.img_res.shape[1]
    lines = img.img_res.shape[0]
    diam_drill = int((cols / 180)*83.5)

    diam_delamina = int(lines/1.97)

    diam_drill_mm = diam_drill / 238.9869
    diam_delamina_mm = diam_delamina / 238.9869

    return diam_drill_mm, diam_delamina_mm

def delamina(diam_drill_mm, diam_delamina_mm):
    pi = 3.141592
    ray_drill = diam_drill_mm/2
    ray_delamina = diam_delamina_mm/2

    area_less = 2*pi*int(ray_drill**2)
    area_bigger = 2*pi*int(ray_delamina**2)

    Fd = diam_delamina_mm/diam_drill_mm
    Fa = area_bigger/area_less

    return print("\nFator de delaminação pelos diâmetros: " + str(Fd) + "\nFator de delaminação pelas áreas: " + str(Fa))