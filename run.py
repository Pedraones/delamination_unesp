import image as img
import calculo as calc

diam_drill_delamina = list()

#name = input('Digite o nome do arquivo: \n')
name = "fEntrada/d1.bmp"
img.input_img(name)
diametros = calc.diameters()
diam_drill_delamina.append(diametros[0])
diam_drill_delamina.append(diametros[1])
calc.Fd(diam_drill_delamina[0], diam_drill_delamina[1])
calc.Fa(diam_drill_delamina[0], diam_drill_delamina[1])
img.window()