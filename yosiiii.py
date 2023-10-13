from cmu_graphics import *
Rect(20, 270, 70, 20, relleno=gradiente('carmesí', 'rojoOscuro', inicio='superior'))
Rect(55, 255, 25, 15, relleno=gradiente('rojo', 'carmesí', inicio='superior'))
Rect(57,257,23,13)
Círculo(35, 290, 10)
Círculo(75, 290, 10)

Rect(300, 330, 70, 30, relleno=gradiente('naranjaOscuro', 'rojoNaranja', inicio='superior'))
Rect(310, 310, 50, 20, relleno=gradiente('naranja', 'naranjaOscuro', inicio='superior'))
Círculo(315, 360, 10)
Círculo(355, 360, 10)

cmu_graphics.run()