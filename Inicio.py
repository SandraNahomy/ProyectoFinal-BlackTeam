from cmu_graphics import *

# Rect(0,0,400,400)
botones = Grupo(Rect(0,0,400,400),
    Polígono(160,160,167,151,289,151,289,172,285,177,285,215,290,225,290,235,160,235,relleno='azulOscuro',borde=rgb(0, 255, 255)),
    Poligono(120,181,110,189,110,235,120,235,relleno='azulMediaNoche',borde=rgb(0, 255, 255)),
    Rect(120,160,160,80,relleno='azulOscuro',borde='agua',anchuraDeBorde=4),
    Rotulo('START',200,200,tamaño=35,relleno='blanco',fuente='orbitron',negrito=True),
    Línea(150,181,139,214,relleno='azulOscuro',anchuraDeLinea=1),
    Línea(164,210,175,193,relleno='azulOscuro',anchuraDeLinea=1),
    Línea(182,213,210,185,relleno='azulOscuro',anchuraDeLinea=1),
    Línea(216,205,234,185,relleno='azulOscuro',anchuraDeLinea=1),
    Línea(259,193,250,205,relleno='azulOscuro',anchuraDeLinea=1)
    )


cmu_graphics.run()



