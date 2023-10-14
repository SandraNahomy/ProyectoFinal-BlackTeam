from cmu_graphics import*

#FONDO
app.fondo=gradiente('azulCieloClaro','azulClaro',inicio='superior')
Circle(100,70,50,relleno='amarillo')                                                                                                                                                                                              
               
#CARRETERA
Rect(0,320,400,80,relleno='gris')
Línea(0,360,400,360,relleno='blanco',guion=True)
#EDIFICIO
edificio1 = Group(
        Rect(0,140,100,130, fill = 'azul'),
        Rect(10,165,20,20, fill = 'azulClaro', borde = 'black'),
        Rect(60,165,20,20, fill = 'azulClaro', borde = 'black'),
        Rect(10,205,20,20, fill = 'azulClaro', borde = 'black'),
        Rect(60,205,20,20, fill = 'azulClaro', borde = 'black'),
        Rect(30,240,30,31))
edificio1.centroX=350
edificio1.centroY=255

Oval(330,224,17,22,relleno=gradiente('rojo','naranja','amarillo','naranja',inicio='superior-izquierda'))
humo1 = Circulo(300,160,20,relleno=gradiente('gris','grisClaro',inicio='superior'),visible =True,opacidad=30)
humo2 = Circulo(300,120,20,relleno=gradiente('gris','grisClaro',inicio='superior'),opacidad=30 )
humo3 = Circulo(300,80,20,relleno=gradiente('gris','grisClaro',inicio='superior'),opacidad=30 )

#PERSONAJE

muñeco=Grupo(
        Circulo(200,345,10, relleno='blanco',anchuraDeBorde=2),
        Linea(200,350,200,380,relleno='blanco',anchuraDeLínea=2),
        Linea(200,380,190,400,relleno='blanco',anchuraDeLínea=2),
        Linea(200,380,210,400,relleno='blanco',anchuraDeLínea=2),
        Linea(200,360,180,370,relleno='blanco',anchuraDeLínea=2),
        Linea(200,360,220,370,relleno='blanco',anchuraDeLínea=2))

muñeco2=Grupo(
        Circulo(200,345,10, relleno='blanco',anchuraDeBorde=2),
        Linea(200,350,200,380,relleno='blanco',anchuraDeLínea=2),
        Linea(200,380,190,400,relleno='blanco',anchuraDeLínea=2),
        Linea(200,380,210,400,relleno='blanco',anchuraDeLínea=2),
        Linea(200,360,180,370,relleno='blanco',anchuraDeLínea=2),
        Linea(200,360,220,370,relleno='blanco',anchuraDeLínea=2),
        Circle(175,370,10,relleno=None,borde='bronceado',anchuraDeBorde=3),
        Circle(175,370,5,relleno=None,borde='bronceado',anchuraDeBorde=2)
)

muñeco2.centroX=40
muñeco2.centroY=341

mun3=  Grupo(
        Circulo(200,345,10, relleno='blanco',anchuraDeBorde=2),
        Linea(200,350,200,380,relleno='blanco',anchuraDeLínea=2),
        Linea(200,380,190,400,relleno='blanco',anchuraDeLínea=2),
        Linea(200,380,210,400,relleno='blanco',anchuraDeLínea=2),
        Linea(200,360,180,370,relleno='blanco',anchuraDeLínea=2),
        Linea(200,360,220,370,relleno='blanco',anchuraDeLínea=2))

mun3.centroX=185
mun3.centroY=350

carro1=Grupo (Rect(20, 270, 80, 20, relleno='rojo'),
        Rect(55, 255, 35, 15, relleno='rojo'),
        Rect(57,257,33,13),
        Círculo(35, 290, 10),
        Círculo(75, 290, 10),
        Estrella(35,290,10,6, relleno=None, borde='blanco', redondez =10),
        Estrella(75,290,10,6, relleno=None, borde='blanco', redondez =10))


carro1.centroY=338
muñeco.centroY=320
muñeco.centroX=40

app.pasosPorSegundo=20

def enPaso():
    
    carro1.centroX += 5
    muñeco.centroX += 5
    muñeco2.centroX += 3
    mun3.centroX += 4
    if carro1.centroX > 430:
        carro1.centroX= 0
        muñeco.centroX = -20
        muñeco2.centroX = -30
        muñeco2.alFrente()
        mun3.centroX = -20
cmu_graphics.run()

