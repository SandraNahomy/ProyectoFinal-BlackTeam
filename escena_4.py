from cmu_graphics import *

app.fondo = gradiente('azulCieloClaro','azulClaro', inicio = 'superior')

Rect(0,240,400,160, fill = 'verdeOscuro')

fundacion = Group(
    Rect(60,120,240,120, fill = 'nieve', borde = 'black'),
    Rect(100,160,160,80),
    Poligono(60,120,140,80,380,80,380,240,300,240,300,120, fill = 'white', borde = 'negro'),
    Linea(300,120,380,80),
    Rotulo('FUNDACION',160,140, tamaño = 20),
    Circulo(240,140,10, fill = 'red'))

cmu_graphics.run()