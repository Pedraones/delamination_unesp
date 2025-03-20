def measures( cols, lines):
    cols = cols
    lines = lines
    return cols, lines

def diameters(self):

    diam_drill = int((self.cols / 180)*83.5)

    diam_delamina = int(self.lines/1.97)

    diam_drill_mm = diam_drill / 238.9869
    diam_delamina_mm = diam_delamina / 238.9869

    return diam_delamina_mm, diam_drill_mm

def delamina(self, pi, diam_drill_mm, diam_delamina_mm):

    pi = 3.141592
    area_less = 2*pi*((diam_drill_mm/2)^2)
    area_bigger = 2*pi*(diam_delamina_mm/2)

    Fd = diam_delamina_mm/diam_drill_mm
    Fa = area_bigger/area_less

    print("Fator de delaminação pelos diâmetros: " + str(Fd))
    print("Fator de delaminação pelas áreas: " + str(Fa))