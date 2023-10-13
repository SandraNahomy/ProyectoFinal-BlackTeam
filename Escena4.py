from cmu_graphics import*

#FONDO
app.fondo=gradiente('negro','azulMedianoche',inicio='superior')

#CARRETERA
Rect(0,320,400,80,relleno='gris')
Linea(0,360,400,360,relleno='blanco',guion=True)

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

carro1.centroY=338

carro2= Grupo(Rect(300, 330, 70, 20, relleno='azulCieloClaro'),
Rect(315, 315, 25, 15, relleno='azulCieloClaro'),
Rect(315,318,23,13),
Círculo(315, 350, 10),
Círculo(355, 350, 10),
Estrella(315,350,10,6, relleno=None, borde='blanco', redondez =10),
Estrella(355,350,10,6, relleno=None, borde='blanco', redondez =10))
#VEHICULOS
app.pasosPorSegundo=1

def enPasos():

 carro1.centroX+=10
 carro2.centroX+=10

cmu_graphics.run()

