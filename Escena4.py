from cmu_graphics import*

#FONDO
app.fondo=gradiente('azulCieloClaro','azulClaro',inicio='superior')
Circle(300,70,50,relleno='amarillo')                                                                                                                                                                                              
               
#CARRETERA
Rect(0,320,400,80,relleno='gris')
Línea(0,360,400,360,relleno='blanco',guion=True)
#PERSONAJE
muñeco=Grupo(
        Circulo(200,345,10, relleno='blanco',anchuraDeBorde=2),
        Linea(200,350,200,380,relleno='blanco',anchuraDeLínea=2),
        Linea(200,380,190,400,relleno='blanco',anchuraDeLínea=2),
        Linea(200,380,210,400,relleno='blanco',anchuraDeLínea=2),
        Linea(200,360,180,370,relleno='blanco',anchuraDeLínea=2),
        Linea(200,360,220,370,relleno='blanco',anchuraDeLínea=2))
muñeco.centroY=290

muñeco2=Grupo(
        Circulo(200,345,10, relleno='blanco',anchuraDeBorde=2),
        Linea(200,350,200,380,relleno='blanco',anchuraDeLínea=2),
        Linea(200,380,190,400,relleno='blanco',anchuraDeLínea=2),
        Linea(200,380,210,400,relleno='blanco',anchuraDeLínea=2),
        Linea(200,360,180,370,relleno='blanco',anchuraDeLínea=2),
        Linea(200,360,220,370,relleno='blanco',anchuraDeLínea=2))

muñeco2.centroX=100
muñeco2.centroY=290

mun3=  Grupo(
        Circulo(200,345,10, relleno='blanco',anchuraDeBorde=2),
        Linea(200,350,200,380,relleno='blanco',anchuraDeLínea=2),
        Linea(200,380,190,400,relleno='blanco',anchuraDeLínea=2),
        Linea(200,380,210,400,relleno='blanco',anchuraDeLínea=2),
        Linea(200,360,180,370,relleno='blanco',anchuraDeLínea=2),
        Linea(200,360,220,370,relleno='blanco',anchuraDeLínea=2))

mun3.centroX=250
mun3.centroY=290

carro1=Grupo (Rect(20, 270, 80, 20, relleno='rojo'),
        Rect(55, 255, 35, 15, relleno='rojo'),
        Rect(57,257,33,13),
        Círculo(35, 290, 10),
        Círculo(75, 290, 10),
        Estrella(35,290,10,6, relleno=None, borde='blanco', redondez =10),
        Estrella(75,290,10,6, relleno=None, borde='blanco', redondez =10))

Circle(125,295,10,relleno=None,borde='bronceado',anchuraDeBorde=3)
Circle(125,295,5,relleno=None,borde='bronceado',anchuraDeBorde=2)

carro1.centroY=338

app.pasosPorSegundo=20

def enPaso():
    
    carro1.centroX += 4

    if carro1.centroX > 430:
        carro1.centroX=-30
cmu_graphics.run()

