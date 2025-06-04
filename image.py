import cv2
from cv2 import COLOR_RGB2GRAY, cvtColor
import numpy as np

# Variáveis globais para armazenar dados da imagem e medidas
img = None
img_rgb = None
img_gray = None
center_x = 0
center_y = 0
lines = 0
cols = 0
diam_drill = 0
diam_delamina = 0
ray_drill = diam_drill/2
ray_delamina = diam_delamina/2
wResi = 0
hResi = 0


def input_img(name):
    global img, img_rgb, img_gray
    if name:
        try:
            img = cv2.imread('images/' + name)
            if img is None:
                print(f"Aviso: Não foi possível encontrar 'images/{name}'. Tentando carregar '{name}' do diretório atual.")
                img = cv2.imread(name)
                if img is None:
                    print(f"Erro: Não foi possível carregar a imagem '{name}'. Verifique o nome e o caminho do arquivo.")
                    return False
            
            img_rgb = img.copy()
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
            
            return True
        
        except Exception as e:
            print(f"Erro ao carregar a imagem: {e}")
            return False
    else:
        print("Erro: Nenhum nome de arquivo fornecido para input_img.")
        return False

def measures():
    global wResi, hResi, center_x, center_y, cols, lines, diam_drill, diam_delamina, ray_drill, ray_delamina

    if img_gray is None:
        print("Erro: Imagem não carregada antes de chamar measures().")
        return False

    cols, lines = img_gray.shape[:2]

    wResi = int(lines / 3)
    hResi = int(cols / 3)

    center_x = int(lines / 2)
    center_y = int(cols / 2)

    diam_drill = 6*239
    diam_delamina = int(6.4*239)
    
    ray_delamina = diam_delamina/2
    ray_drill = diam_drill/2

    print(f"Dimensões: {cols}x{lines}")
    
    return True

def analyzes_px():
    measures()        
    global img_gray
    global img_res_gray
    
    img_gray=cvtColor(img, COLOR_RGB2GRAY)

    for x in range(img_gray.shape[0]):  # linhas
        for y in range(img_gray.shape[1]):  # colunas
            pixel_value = img_gray[x, y]
            
            """if pixel_value <= 180:
                analyzed_img[x, y] = 0"""
    
    return img_gray

def apply_color_inside_small_circle():
    global img_rgb
    if img_rgb is None or diam_drill == 0:
        print("\n Erro: Imagem ou diâmetro do furo não inicializados para apply_color_inside_small_circle().")
        return

    mask = np.zeros(img_rgb.shape[:2], dtype=np.uint8)
    
    cv2.circle(mask, (center_x, center_y), int(ray_drill), 255, -1)
    
    fill_color = (255, 255, 255)
    
    color_img = np.full_like(img_rgb, fill_color)
    img_rgb = cv2.bitwise_and(img_rgb, img_rgb, mask=cv2.bitwise_not(mask)) + \
              cv2.bitwise_and(color_img, color_img, mask=mask)
    
    print(f"{ray_delamina}, {ray_drill}")

def apply_color_outside_large_circle():
    global img_rgb
    if img_rgb is None or diam_delamina == 0:
        print("Erro: Imagem ou diâmetro de delaminação não inicializados para apply_color_outside_large_circle().")
        return

    mask = np.zeros(img_rgb.shape[:2], dtype=np.uint8)
    
    cv2.circle(mask, (center_x, center_y), int(ray_delamina), 255, -1)
    
    mask_inv = cv2.bitwise_not(mask)
    
    fill_color = (255, 255, 255) # BGR
    color_img = np.full_like(img_rgb, fill_color)
    
    img_rgb = cv2.bitwise_and(img_rgb, img_rgb, mask=mask) + \
              cv2.bitwise_and(color_img, color_img, mask=mask_inv)

def window():
    apply_color_outside_large_circle()

    apply_color_inside_small_circle()

    analyzes_px()
    cv2.namedWindow('img_process', cv2.WINDOW_NORMAL)
    cv2.imshow('img_process', img_rgb) 

    cv2.resizeWindow('img_process', wResi,hResi)

    cv2.waitKey()