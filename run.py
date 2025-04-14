import image as img
import calculo as calc

diam_drill_delamina = list()

print('\nA delaminação da imagem está em contraste ou destacada ?')
respos = str.lower(input('Digite S se estiver ou N caso contrário \n'))

if respos == "s":
    name = input('Digite o nome do arquivo: \n')
    img.input_img(name)
    global color
    color = str.lower(input('\nOs sinais de delaminação está com a cor preta ou branca ? \n'))

    if color == "preta" or color == "preto":
        calc.count_preto()
        calc.delamina_for_px(color)

    elif color == "branca" or color == "branco":
        calc.count_branco()
        calc.delamina_for_px(color)

elif respos == "n":
    name = input('Digite o nome do arquivo: \n')
    img.input_img(name)
    diam_drill_delamina.append(calc.diameters())
    calc.Fd(diam_drill_delamina[0][0], diam_drill_delamina[0][1])
    calc.Fa(diam_drill_delamina[0][0], diam_drill_delamina[0][1])
    img.window()