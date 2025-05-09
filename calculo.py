import image as img

def diameters():
    cols = img.img_res_rgb.shape[1]
    lines = img.img_res_rgb.shape[0]
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

def count_preto():
    global num_px0
    num_px0  = 0

    img_res_gray = img.analyzes_px()
    cols = img.img_res_gray.shape[1]
    lines = img.img_res_gray.shape[0]

    for y in range(lines):
        for x in range(cols):
            if img_res_gray[y,x] == 0:
                num_px0 += 1

def count_branco():
    global num_px255
    num_px255 = 0

    img_res_gray = img.analyzes_px()
    cols = img.img_res_rgb.shape[1]
    lines = img.img_res_rgb.shape[0]

    for y in range(lines):
        for x in range(cols):
            if img_res_gray[y,x] > 0:
                num_px255 += 1

def delamina_for_px(color):
    color = str.lower(color)
    
    if color == "preta" or color == "preto":
        count_preto()

        return print(str(num_px0) + " pixeis de delaminação" )

    elif color == "branca" or color == "branco":
        count_branco()

        return print(str(num_px255) + " pixeis de delaminação" )