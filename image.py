import cv2
from cv2 import COLOR_RGB2GRAY, cvtColor
import numpy as np

# Variáveis globais para armazenar dados da imagem e medidas
img = None
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
    global img
    if name:
        try:
            img = cv2.imread('images/' + name)
            if img is None:
                print(f"Aviso: Não foi possível encontrar 'images/{name}'. Tentando carregar '{name}' do diretório atual.")
                img = cv2.imread(name)
                if img is None:
                    print(f"Erro: Não foi possível carregar a imagem '{name}'. Verifique o nome e o caminho do arquivo.")
                    return False
            
            return True
        
        except Exception as e:
            print(f"Erro ao carregar a imagem: {e}")
            return False
    else:
        print("Erro: Nenhum nome de arquivo fornecido para input_img.")
        return False

def measures():
    global wResi, hResi, center_x, center_y, cols, lines, diam_drill, diam_delamina, ray_drill, ray_delamina

    if img is None:
        print("Erro: Imagem não carregada antes de chamar measures().")
        return False

    cols, lines = img.shape[:2]

    wResi = int(lines / 3)
    hResi = int(cols / 3)

    center_x = int(lines / 2)
    center_y = int(cols / 2)

    diam_drill = 6*239
    diam_delamina = int(6.6*239)
    
    ray_delamina = diam_delamina/2
    ray_drill = diam_drill/2

    print(f"Dimensões: {cols}x{lines}")
    
    return True

def analyzes_px():
    measures()        
    global img
    isolate()
    
    img = cvtColor(img, COLOR_RGB2GRAY)

    for x in range(img.shape[0]):  # linhas
        for y in range(img.shape[1]):  # colunas
            
            if img[x,y] <= 130:
                img[x,y] = 0

    return img

def apply_color_inside_small_circle():
    global img
    measures()

    mask = np.zeros(img.shape[:2], dtype=np.uint8)
    
    cv2.circle(mask, (center_x, center_y), int(ray_drill), 255, -1)
    
    fill_color = (255, 255, 255)
    
    color_img = np.full_like(img, fill_color)
    img = cv2.bitwise_and(img, img, mask=cv2.bitwise_not(mask)) + \
              cv2.bitwise_and(color_img, color_img, mask=mask)
    
    print(f"{ray_delamina}, {ray_drill}")

def apply_color_outside_large_circle():
    global img
    measures()

    mask = np.zeros(img.shape[:2], dtype=np.uint8)
    
    cv2.circle(mask, (center_x, center_y), int(ray_delamina), 255, -1)
    
    mask_inv = cv2.bitwise_not(mask)
    
    fill_color = (255, 255, 255) # BGR
    color_img = np.full_like(img, fill_color)
    
    img = cv2.bitwise_and(img, img, mask=mask) + \
              cv2.bitwise_and(color_img, color_img, mask=mask_inv)

def isolate():
    apply_color_outside_large_circle()
    apply_color_inside_small_circle()

def window():

    print(img[1,1])
    cv2.namedWindow('img_process', cv2.WINDOW_NORMAL)
    cv2.imshow('img_process', img) 
    cv2.resizeWindow('img_process', wResi,hResi)

    cv2.waitKey()