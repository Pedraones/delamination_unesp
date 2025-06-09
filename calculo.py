import image as img

def Fd(diam_drill_mm, diam_delamina_mm):
    Fd = diam_delamina_mm/diam_drill_mm

    print("Fator de delaminação pelos diâmetros: " + str(Fd))
    print("----------------------")

def Fa(diam_drill_mm, diam_delamina_mm):
    pi = 3.141592
    ray_drill = diam_drill_mm/2
    ray_delamina = diam_delamina_mm/2

    delamina_mm2 = delaminacao_area_mm2()

    area_less = pi*float(ray_drill*ray_drill)
    area_bigger = pi*float(ray_delamina*ray_delamina)
    
    area_crown = float(area_bigger - area_less)
    
    Fa = delamina_mm2 / area_crown

    print(f"Fator de delaminação areaDelamina/coroa: {Fa} \n area da delaminação: {delamina_mm2}")
    print("----------------------")

def delaminacao_area_mm2():
    # Conta quantos pixels estão pretos (delaminação)
    num_px_pretos = area_delamina()

    # Conversão de pixels para mm²
    px_por_mm = 238.9869
    area_mm2 = num_px_pretos / (px_por_mm ** 2)

    print(f"Área de delaminação: {area_mm2:.2f} mm²")
    print("----------------------")
    return area_mm2

def area_crown_mm():
    px_por_mm = 238.9869
    qtd_px_crown = img.area_crown_px()
    crown_mm2 = qtd_px_crown / (px_por_mm ** 2)

    return crown_mm2
    
def area_delamina():
    global num_px0
    num_px0 = 0

    img_gray = img.analyzes_px()
    cols = img.img.shape[1]
    lines = img.img.shape[0]

    for y in range(lines):
        for x in range(cols):
            if img_gray[y,x] == 0:
                num_px0 += 1

    return num_px0