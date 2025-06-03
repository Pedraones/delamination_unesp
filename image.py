import cv2
import numpy as np
from cv2 import COLOR_RGB2GRAY, cvtColor    
from PIL import Image

def recolor():
    global img_res_rgb
    global img_res_gray
    global img_gray

    img_gray = cvtColor(img_array, COLOR_RGB2GRAY)

    img_res_gray = img_gray[00:1530, 350:1800]

    print('quantidade de pixels de uma imagem: '+str(img_array.size))
    print('quantidade de pixels de coluna: '+str(float(img_array[1].size)))
    print('quantidade de pixels de linha: '+str(float(img_array[0].size )))

    print('\n\nquantidade de pixels de uma imagem: '+str(img_gray.size))
    print('quantidade de pixels de coluna: '+str(float(img_gray[1].size)))
    print('quantidade de pixels de linha: '+str(float(img_gray[0].size)))

def input_img(name):
    #armazena a imagem que será utilizada para o "processamento"
    if name:
        global img_array 
        img = Image.open('images/' + name)
        img_array = np.array(img)

        recolor()
    else:
        name = input('Insira o nome do arquivo: \n')

def measures():
    global wResi
    global hResi
    global center_x
    global center_y
    global cols
    global lines

    cols = img_res_rgb.shape[1]
    lines = img_res_rgb.shape[0]

    #Armazenamento da quantidade de colunas e linhas da imagem  
    wResi = int(cols / 3)
    hResi = int(lines / 3)

    #Identificação do centro (aproximado) da imagem
    center_x = int(cols / 2)
    center_y = int((lines / 2))

    return cols, lines


def draw_circle():
    #diametro do furo presente
    global diam_drill
    global diam_delamina

    diam_drill = int((lines / 180)*84.2)
    diam_delamina = int(lines/1.98)

    #Diametro entre o alcance mais distante da delaminação (manchas mais escuras que estão próximas do furo) 

    #Espessura da linha da circunferência que será desenhada
    thickness = 2

    #Circunferência que contorna o "parede interna" do furo, baseada no diametro do furo
    #cv2.circle(img_res_rgb, (center_x, center_y), diam_drill, (255,255,255), thickness=thickness)

    #Circunferência que contorna o toda a marca de delaminação em volta do furo, baseada no diâmetro da delaminação (diam_delamina)
    #cv2.circle(img_res_rgb, (center_x, center_y), diam_delamina, (255,255,255), thickness=thickness)

    return diam_delamina, diam_drill

def analyzes_px():
    measures()        
    global img_res_rgb
    global img_res_gray
    global analyzed_img

    modified_gray = cv2.cvtColor(img_res_rgb, cv2.COLOR_BGR2GRAY)
    analyzed_img = modified_gray.copy()

    for x in range(modified_gray.shape[0]):  # linhas
        for y in range(modified_gray.shape[1]):  # colunas
            pixel_value = modified_gray[x, y]
            
            if pixel_value <= 180:
                analyzed_img[x, y] = 0
    img_res_gray = analyzed_img.copy()
    
    return img_res_gray
def apply_color_inside_small_circle():
    global img_res_rgb
    measures()
    
    mask = np.zeros(img_res_rgb.shape[:2], dtype=np.uint8)
    
    diam_drill = int((lines / 180) * 84)
    cv2.circle(mask, (center_x, center_y), diam_drill, 255, -1)
    
    color_inside = (255, 255, 255)  # BGR
    color_img = np.full_like(img_res_rgb, color_inside)
    
    img_res_rgb = cv2.bitwise_and(img_res_rgb, img_res_rgb, mask=cv2.bitwise_not(mask)) + \
                  cv2.bitwise_and(color_img, color_img, mask=mask)

    
def apply_color_outside_circle():
    global img_res_rgb
    measures()
    diam_delamina = int(lines/2)
    
    mask = np.zeros(img_res_rgb.shape[:2], dtype=np.uint8)
    
    cv2.circle(mask, (center_x, center_y), diam_delamina, 255, -1)
    
    mask_inv = cv2.bitwise_not(mask)
    
    color_outside = (255, 255, 255)  # BGR
    color_img = np.full_like(img_res_rgb, color_outside)
    
    img_res_rgb = cv2.bitwise_and(img_res_rgb, img_res_rgb, mask=mask) + \
                  cv2.bitwise_and(color_img, color_img, mask=mask_inv)
    
def area_crown_px():
    measures()        
    global img_res_rgb
    global img_res_gray
    global analyzed_img
    qtd_px_crown = 0

    for x in range(img_res_rgb.shape[0]):  # linhas
        for y in range(img_res_rgb.shape[1]):  # colunas
            qtd_px_crown += 1
            
    return qtd_px_crown

#Exibição da imagem em uma janela
def window():
    measures()
    draw_circle()
    apply_color_outside_circle()
    apply_color_inside_small_circle()
    analyzes_px()
    cv2.namedWindow('img_process', cv2.WINDOW_NORMAL)
    cv2.imshow('img_process', img_res_gray)
    cv2.resizeWindow('img_process', wResi,hResi)

    cv2.waitKey()