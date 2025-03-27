import image as img

def diameters():
    cols = img.img_res.shape[1]
    lines = img.img_res.shape[0]
    diam_drill = int((cols / 180)*83.5)

    diam_delamina = int(lines/1.97)

    diam_drill_mm = diam_drill / 238.9869
    diam_delamina_mm = diam_delamina / 238.9869

    return diam_drill_mm, diam_delamina_mm

def Fd(diam_drill_mm, diam_delamina_mm):
    Fd = diam_delamina_mm/diam_drill_mm

    return print("\nFator de delaminação pelos diâmetros: " + str(Fd))

def Fa(diam_drill_mm, diam_delamina_mm):
    pi = 3.141592
    ray_drill = diam_drill_mm/2
    ray_delamina = diam_delamina_mm/2

    area_less = 2*pi*int(ray_drill**2)
    area_bigger = 2*pi*int(ray_delamina**2)
    
    Fa = area_bigger/area_less

    return print("Fator de delaminação pelas áreas: " + str(Fa))

def count_white():
    global num_px0
    num_px0  = 0

    img_res_gray = img.img_res_gray
    cols = img.img_res_gray.shape[1]
    lines = img.img_res_gray.shape[0]

    for x in range(cols):
        for y in range(lines):
            if img_res_gray[x, y] == 0:
                num_px0 += 1

    return num_px0

def count_preto():
    global num_px0
    num_px0  = 0

    img_res_gray = img.img_res_gray
    cols = img.img_res_gray.shape[1]
    lines = img.img_res_gray.shape[0]

    for x in range(cols):
        for y in range(lines):
            if img_res_gray[x, y] == 0:
                num_px0 += 1

    return num_px0