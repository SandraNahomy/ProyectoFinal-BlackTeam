# Escena 1:
import time

app.fondo = gradient('azulCieloProfundo','azulClaro', inicio = 'superior')

cielo = Group(
    Estrella(80,60,45,8, fill =gradient('amarillo','amarillo','naranja'), redondez = 75),
    Circulo(80,60,25, relleno = 'amarillo')
    )
nube1 = Group(
    Circulo(250,40,25, fill = 'white', borde = 'gainsboro'),
    Circulo(210,40,25, fill = 'white', borde = 'gainsboro'),
    Circulo(230,40,25, fill = 'white', borde = 'gainsboro'),
    Rect(195,23,70,35, fill = 'white'))
nube1.dx = 1
nube1.alFondo()
nube2 = Group(
    Circulo(350,70,25, fill = 'white', borde = 'gainsboro'),
    Circulo(310,70,25, fill = 'white', borde = 'gainsboro'),
    Circulo(330,70,25, fill = 'white', borde = 'gainsboro'),
    Rect(295,53,70,35, fill = 'white'))
nube2.dx = 1

humo1 = Circulo(300,160,20, visible = False)
humo2 = Circulo(300,120,20, visible = False)
humo3 = Circulo(300,80,20, visible = False)

def terremoto(edificio1,edificio2,empresa,letrero,derrumbe):
    
    time.sleep(0.5)
    mode_pelicula = Group(Rect(0,0,400,50),
        Rect(0,350,400,50))
    time.sleep(1)
    edificio1.centroX += 10
    edificio2.centroX += 10
    empresa.centroX += 10
    time.sleep(0.1)
    edificio1.centroX -= 10
    edificio2.centroX -= 10
    empresa.centroX -= 10
    time.sleep(0.1)
    edificio1.centroX += 10
    edificio2.centroX += 10
    empresa.centroX += 10
    time.sleep(0.1)
    edificio1.centroX -= 10
    edificio2.centroX -= 10
    empresa.centroX -= 10
    time.sleep(0.1)
    edificio1.centroX += 10
    edificio2.centroX += 10
    empresa.centroX += 10
    time.sleep(0.1)
    edificio1.centroX -= 10
    edificio2.centroX -= 10
    empresa.centroX -= 10
    time.sleep(0.1)
    edificio1.centroX += 10
    edificio2.centroX += 10
    empresa.centroX += 10
    time.sleep(0.1)
    edificio1.centroX -= 10
    edificio2.centroX -= 10
    empresa.centroX -= 10
    time.sleep(0.1)
    suspenso = Rect(0,0,400,400)
    time.sleep(2)
    suspenso.visible, mode_pelicula.visible = False, False
    
    if mode_pelicula.visible == False:
        empresa.visible = False
        derrumbe.visible = True
        humo1.visible = True
        humo2.visible = True
        humo3.visible = True
        letrero.centroY = 230
        letrero.rotarAngulo = -25
def inicio():
    
    suelo = Group(
        Rect(0,360,400,40, fill = 'verde'),
        Rect(-2,270,404,22, fill = 'grisOscuro', borde = 'black', anchuraDeBorde = 1),
        Rect(-2,290,404,70, fill = 'gris', borde = 'black', anchuraDeBorde = 1),
        Linea(0,320,400,320, fill = 'white', guion = (12,14)),
        Linea(30,289,30,272, fill = 'gris'),
        Linea(150,289,150,272, fill = 'gris'))
        
    edificio1 = Group(
        Rect(0,140,100,130, fill = 'azul'),
        Rect(10,165,20,20, fill = 'azulClaro', borde = 'black'),
        Rect(60,165,20,20, fill = 'azulClaro', borde = 'black'),
        Rect(10,205,20,20, fill = 'azulClaro', borde = 'black'),
        Rect(60,205,20,20, fill = 'azulClaro', borde = 'black'),
        Rect(30,240,30,31))
        
    edificio2 = Group(
        Rect(100,130,100,140, fill = 'red'),
        Rect(120,155,20,25, fill = 'azulClaro', borde = 'black'),
        Rect(160,155,20,25, fill = 'azulClaro', borde = 'black'),
        Rect(120,195,20,25, fill = 'azulClaro', borde = 'black'),
        Rect(160,195,20,25, fill = 'azulClaro', borde = 'black'),
        Rect(130,240,40,31, fill = 'marronCuero', borde = 'black', anchuraDeBorde = 1),
        Rect(115,110,70,20, fill = 'white'),
        Rotulo('hotel',150,120, fuente = 'cinzel', negrito = True))
    edificio2.izquierda = edificio1.derecha
    empresa = Group(
        Rect(210,160,180,110, fill = 'marron'),
        Rect(240,200,120,70),
        Poligono(220,289,240,270,360,270,380,289, fill = 'gris'),
        Rect(360,120,15,40, fill = 'gris', borde = 'black', anchuraDeBorde = 1.5))
    
    derrumbe = Poligono(210,270,215,265,225,260,230,255,245,225,275,215,295,190,300,190,310,205,325,210,340,240,360,245,390,270,
    fill = 'marron', borde = 'black', visible = False)
    
    letrero= Group(Rect(240,165,120,30, fill = 'naranja', borde = 'white'),
        Rotulo('EMPRESA',300,180, fill = 'nieve', negrito = True, tamaño = 20))
        
    terremoto(edificio1,edificio2,empresa,letrero,derrumbe)


inicio()   


def enPaso():
    
    nube1.centroX += nube1.dx
    nube2.centroX += nube2.dx
    cielo.rotarAngulo += 1
    humo1.centroY -= 1
    humo1.opacidad -= 0.5
    humo2.centroY -= 1
    humo2.opacidad -= 0.5
    humo3.centroY -= 1
    humo3.opacidad -= 0.5
    if nube2.centroX > 400 or nube1.centroX < 0:
        nube1.dx = -nube1.dx
        nube2.dx = -nube2.dx
    if humo1.centroY < 40:
        humo1.centroY = 160
        humo1.opacidad = 100
        
    if humo2.centroY < 40:
        humo2.centroY = 160
        humo2.opacidad = 100
        
    if humo3.centroY < 40:
        humo3.centroY = 160
        humo3.opacidad = 100
    


cmu_graphics.run()
