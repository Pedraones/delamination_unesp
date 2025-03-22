import cv2

#armazena a imagem que será utilizada para o "processamento"
img = cv2.imread('images/d10.bmp')

#redimensiona o tamanho da imagem para a exibição
img_res = img[00:1530, 250:1800]

#Armazenamento da quantidade de colunas e linhas da imagem
cols = img_res.shape[1]
lines = img_res.shape[0]

#Identificação do centro (aproximado) da imagem
center_x = int(cols / 2)
center_y = int((lines / 2))

#diametro do furo presente
diam_drill = int((cols / 180)*83.5)

#Diametro entre o alcance mais distante da delaminação (manchas mais escuras que estão próximas do furo) 
diam_delamina = int(lines/1.97)

#Espessura da linha da circunferência que será desenhada
thickness = 2

#Circunferência que contorna o "parede interna" do furo, baseada no diametro do furo
drill_circle = cv2.circle(img_res, (center_x, center_y), diam_drill, (200,200,25), thickness=thickness)

#Circunferência que contorna o toda a marca de delaminação em volta do furo, baseada no diâmetro da delaminação (diam_delamina)
delamina_circle = cv2.circle(img_res, (center_x, center_y), diam_delamina, (200,200,25), thickness=thickness)

#Tamanho da janela que exibirá o resultado da imagem
wResi = int(cols / 3)
hResi = int(lines / 3)

#Exibição da imagem em uma janela
def window():
    cv2.namedWindow('img_process', cv2.WINDOW_NORMAL)
    cv2.imshow('img_process', img_res)
    cv2.resizeWindow('img_process', wResi,hResi)

    print('Colunas: ' + str(cols) + ' Linhas: ' + str(lines))

    #cv2.imwrite('saida.png', img_resize) #salva a imagem q esta dentro da variavel IMG

    #Fecha a janela ao clicar em qualquer tecla
    cv2.waitKey()