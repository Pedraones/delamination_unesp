import image as img

def Fd(diam_drill_mm, diam_delamina_mm):
    Fd = diam_delamina_mm/diam_drill_mm

    print("Fator de delaminação pelos diâmetros: " + str(Fd))
    print("----------------------")

def Fa(diam_drill_mm):
    pi = 3.141592
    ray_drill = diam_drill_mm/2

    delamina_mm2 = delaminacao_area_mm2()

    area_less = pi*float(ray_drill*ray_drill)
    
    Fa = delamina_mm2 / area_less

    print(f"Fator de delaminação areaDelamina/coroa: {Fa} \n area da delaminação: {delamina_mm2}")
    print("----------------------")

def delaminacao_area_mm2():
    num_px_pretos = area_delamina()

    px_por_mm = 238.9869
    area_mm2 = num_px_pretos / (px_por_mm ** 2)
    
    return area_mm2
    
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