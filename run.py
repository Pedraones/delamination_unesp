import image as img
import calculo as calc

diam_drill_delamina = list()

name = 'diamantada/fSaida/d21.bmp'
img.input_img(name)
diametros = img.measures()

diam_drill_delamina.append(diametros[0])
diam_drill_delamina.append(diametros[1])

calc.Fd(diam_drill_delamina[0], diam_drill_delamina[1])
calc.Fa(diam_drill_delamina[0])

img.window() 