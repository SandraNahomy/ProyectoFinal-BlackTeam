from cmu_graphics import *

Rect(20, 270, 70, 20, relleno='rojo')
Rect(55, 255, 25, 15, relleno='rojo')
Rect(57,257,23,13)
Círculo(35, 290, 10)
Círculo(75, 290, 10)
Estrella(35,290,10,6, relleno=None, borde='blanco', redondez =10)
Estrella(75,290,10,6, relleno=None, borde='blanco', redondez =10)

Rect(300, 330, 70, 20, relleno='azulCieloClaro')
Rect(315, 315, 25, 15, relleno='azulCieloClaro')
Rect(315,318,23,13)
Círculo(315, 350, 10)
Círculo(355, 350, 10)
Estrella(315,350,10,6, relleno=None, borde='blanco', redondez =10)
Estrella(355,350,10,6, relleno=None, borde='blanco', redondez =10)

cmu_graphics.run()