import image as img
import calculo as calc

diam_drill_delamina = list()

print('\nA delaminação da imagem está em contraste ou destacada ?')
respos = input('Digite S se precisar ou N caso contrário \n')

if respos == "S" or respos == "s":
    name = input('Digite o nome do arquivo: \n')

elif respos == "N" or respos == "n":
    name = input('Digite o nome do arquivo: \n')
    img.input_img(name)
    diam_drill_delamina.append(calc.diameters())
    calc.delamina(diam_drill_delamina[0][0], diam_drill_delamina[0][1])
    img.window()