from cmu_graphics import *

app.fondo=gradiente('azulCieloProfundo','azulClaro',inicio='superior')

Rect(0,300,400,150,relleno='verde')

Línea(200,0,200,400,anchuraDeLínea=3)


#EdificioMalo

Polígono(0,300,5,270,30,245,60,250,80,225,115,250,105,225,160,245,155,270,180,300,relleno='marrónCuero')

#EdificioBueno

Rect(210,190,180,110,relleno='marrón')

Rect(240,230,120,70)

Rect(370,150,14,40,relleno='gris',borde='negro',anchuraDeBorde=1.5)



Ovalo(95,70,160,110,relleno='blanco')

Línea(70,45,125,95,relleno='rojo',anchuraDeLínea=3)

Línea(125,45,75,95,relleno='rojo',anchuraDeLínea=3)


Ovalo(300,70,160,110,relleno='blanco')

Línea(275,80,300,105,relleno='verdeAmarillo',anchuraDeLínea=3)

Línea(300,105,345,45,relleno='verdeAmarillo',anchuraDeLínea=3)

cmu_graphics.run()












