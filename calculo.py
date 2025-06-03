import image as img

def diameters():
    cols = img.img_res_rgb.shape[0]
    lines = img.img_res_rgb.shape[1]

    diam_drill = int((cols / 180)*84.2)

    diam_delamina = int(lines/1.94)
    diam_drill_mm = diam_drill / 238.9869
    diam_delamina_mm = diam_delamina / 238.9869

    print(diam_drill, diam_delamina_mm)

    return diam_drill_mm, diam_delamina_mm

def Fd(diam_drill_mm, diam_delamina_mm):
    Fd = diam_delamina_mm/diam_drill_mm

    return print("\nFator de delaminação pelos diâmetros: " + str(Fd))

def Fa(diam_drill_mm, diam_delamina_mm):
    pi = 3.141592
    ray_drill = diam_drill_mm/2
    ray_delamina = diam_delamina_mm/2

    delamina_mm2 = delaminacao_area_mm2()

    area_less = pi*float(ray_drill*ray_drill)
    area_bigger = pi*float(ray_delamina*ray_delamina)
    
    area_crown1 = float(area_bigger - area_less)
    
    Fa1 = delamina_mm2 / area_crown1

    return print("Fator de delaminação pelas áreas: " + str(area_crown1) + "\n \n area da delaminição: " + str(delamina_mm2))

def delaminacao_area_mm2():
    # Conta quantos pixels estão pretos (delaminação)
    num_px_pretos = count_preto()

    # Conversão de pixels para mm²
    px_por_mm = 238.9869
    area_mm2 = num_px_pretos / (px_por_mm ** 2)

    print(f"Área de delaminação: {area_mm2:.2f} mm²")
    return area_mm2

def area_crown_mm():
    px_por_mm = 238.9869
    qtd_px_crown = img.area_crown_px()
    crown_mm2 = qtd_px_crown / (px_por_mm ** 2)

    return crown_mm2
    
def count_preto():
    global num_px0
    num_px0 = 0

    img_res_gray = img.analyzes_px()
    cols = img.img_res_gray.shape[1]
    lines = img.img_res_gray.shape[0]

    for y in range(lines):
        for x in range(cols):
            if img_res_gray[y,x] == 0:
                num_px0 += 1

    return num_px0

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
    
    return num_px255

def delamina_for_px(color):
    color = str.lower(color)
    
    if color == "preta" or color == "preto":
        delamina = count_preto() / 238.9869

        return print(str(delamina) + " pixeis de delaminação" )

    elif color == "branca" or color == "branco":
        delamina = count_branco() / 238.9869

        return print(str(delamina) + " milímetros de delaminação" )