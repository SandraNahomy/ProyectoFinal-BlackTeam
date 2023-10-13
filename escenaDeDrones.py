from cmu_graphics import *

Rect(0,0,400,400,relleno=gradiente('azulCielo','rosadoClaro',inicio='superior'))


humo = Grupo(
    Óvalo(377,167,40,20,relleno='gris'),
    Óvalo(390,177,40,20,relleno='gris'),
    Óvalo(340,160,40,20,relleno='gris'),
    Óvalo(379,137,40,20,relleno='gris'),
    Óvalo(333,130,40,20,relleno='gris'),
    Óvalo(294,141,40,20,relleno='gris'),
    Óvalo(309,154,40,20,relleno='gris'),
    Óvalo(333,142,40,20,relleno='gris'),
    Óvalo(359,150,40,20,relleno='gris'),
    Óvalo(355,134,40,20,relleno='gris'),
    Óvalo(383,150,40,20,relleno='gris'),
    Óvalo(304,129,40,20,relleno='gris')
    )   

dron = Grupo(
    Circulo(160,120,20),
    Linea(120,120,160,120,anchuraDeLinea=5),
    Linea(200,120,160,120,anchuraDeLinea=5),
    Linea(200,100,200,120,anchuraDeLinea=5),
    Linea(120,100,120,120,anchuraDeLinea=5),
    Óvalo(120,99,30,10),
    Óvalo(200,99,30,10),
    Circulo(160,120,5,relleno='white')
    )
    
dron1=Grupo(
    Circulo(160,120,10  ),
    Linea(140,120,160,120,anchuraDeLinea=5),
    Linea(180,120,160,120,anchuraDeLinea=5),
    Linea(180,100,180,120,anchuraDeLinea=5),
    Linea(140,100,140,120,anchuraDeLinea=5),
    Óvalo(140,99,30,10),
    Óvalo(180,99,30,10),
    Circulo(160,120,3,relleno='white')
    ) 
    
dron2=Grupo(
    Circulo(160,120,15),
    Linea(120,120,160,120,anchuraDeLinea=5),
    Linea(200,120,160,120,anchuraDeLinea=5),
    Linea(200,100,200,120,anchuraDeLinea=5),
    Linea(120,100,120,120,anchuraDeLinea=5),
    Óvalo(120,99,30,10),
    Óvalo(200,99,30,10),
    Circulo(160,120,5,relleno='white')
    ) 

dron1.centroX = 240
dron1.centroY =60
dron2.centroX = 80
dron2.centroY =180

ciudad = Grupo(
    Rect(0,320,400,320,relleno=gradiente('cespedVerde','grisOscuro',inicio='izquierda')),
    Poligono(320,320,320,219,340,240,360,220,370,240,400,200,400,320,relleno='salmon'),
    Rect(338,261,30,30,relleno='azulCieloClaro'),
    
    )  
    
 
    
    
app.pasoPorSegundo = 1

def enPaso():
    humo.centroX -= 3
    dron.centroX += 2
    dron1.centroX += 2
    dron2.centroX += 2
    if humo.centroX < 0:
        humo.centroX = 400
        
    elif dron.centroX > 400:
        dron.centroX = 50
        dron1.centroX = 120
        dron2.centroX = 0
cmu_graphics.run() 