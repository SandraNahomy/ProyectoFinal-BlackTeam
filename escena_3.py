from cmu_graphics import *
app.url= 'https://media.diariopopular.com.ar/p/a75396215fbdf6607fe15352912495e7/adjuntos/143/imagenes/008/065/0008065513/1140x0/smart/sin-titulo-3png.png'

Rect(0,0,400,300,relleno='bisque')
Rect(0,300,400,200,relleno='naranjaMarrón')

Línea(44,85,355,85,anchuraDeLínea=3)
Línea(45,85,45,278,anchuraDeLínea=3)
Línea(45,278,355,278,anchuraDeLínea=3)
Línea(355,278,355,85,anchuraDeLínea=3)


Rect(50,90,300,180,relleno='blanco')



imagen=Image(app.url,50,90)
imagen.ancho /= 3.8
imagen.altura /= 3.9

#Personaje1
Circulo(70,290,30)
Línea(70,290,70,400,anchuraDeLínea=5)
Línea(70,350,20,330,anchuraDeLínea=5)
Línea(20,330,40,300,anchuraDeLínea=5)
Línea(70,350,110,330,anchuraDeLínea=5)
Línea(110,330,100,305,anchuraDeLínea=5)

#Personaje2
Circulo(320,290,30)
Línea(320,290,320,400,anchuraDeLínea=5)
Línea(320,350,270,330,anchuraDeLínea=5)
Línea(270,330,285,300,anchuraDeLínea=5)

Línea(320,350,370,350,anchuraDeLínea=5)
Línea(370,350,320,380,anchuraDeLínea=5)

cmu_graphics.run()