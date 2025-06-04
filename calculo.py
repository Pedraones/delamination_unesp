import image as img

def diameters():
    cols = img.img.shape[0]
    lines = img.img.shape[1]

    diam_drill = 6*238.9869
    diam_delamina = 6.5*238.9869
    
    diam_drill_mm = 6
    diam_delamina_mm = 6.5

    #hMaxImg = lines/238.9869
    #diam_drill = int((cols / 180)*84.2)

    #diam_delamina = int(lines/1.94)
    #diam_drill_mm = diam_drill / 238.9869
    #diam_delamina_mm = diam_delamina / 238.9869

    #print(f"Diametro do furo mm: {diam_drill_mm} \n Diametro cobre toda delaminação em mm: {diam_delamina_mm} \n")
    print(f"\n\naltura maxima da imagens {diam_drill}\n\n")

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

    print(f"Raio do furo: {ray_drill} \n Raio do diametro maior: {ray_delamina} \n")
    #return print("Fator de delaminação pelas áreas: " + str(Fa) + "\n \n area da delaminição: " + str(delamina_mm2))

def delaminacao_area_mm2():
    # Conta quantos pixels estão pretos (delaminação)
    num_px_pretos = area_delamina()

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