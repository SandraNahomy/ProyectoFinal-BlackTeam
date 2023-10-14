from cmu_graphics import*

#FONDO
app.fondo=gradiente('negro','azulMediaNoche',inicio='superior')
Circle(100,70,50,relleno='blanco')  
Circle(100,70,50,relleno='negro',opacidad=30)                                                                                                                                                                                              
               
#CARRETERA
Rect(0,320,400,80,relleno='gris')
Línea(0,360,400,360,relleno='blanco',guion=True)
#EDIFICIO
edificio1 = Group(
        Rect(10,165,20,20, fill = 'azulClaro', borde = 'black'),
        Rect(60,165,20,20, fill = 'azulClaro', borde = 'black'),
        Rect(10,205,20,20, fill = 'azulClaro', borde = 'black'),
        Rect(60,205,20,20, fill = 'azulClaro', borde = 'black'),
        Rect(30,240,30,31))
c=Rect(0,140,100,130, fill = 'azul')
edificio1.centroX=350
edificio1.centroY=255
c.centroY=255
c.centroX=350
c.alFondo()
casa=Group(Rect(113, 180, 80, 100, relleno=gradiente('marrónArenoso', 'mocasín', inicio='superior'),borde='marrónArenoso'),
           Polígono(100, 195, 150,130,206,195,relleno=gradiente('marrónCuero', 'tierra', inicio='superior'),
        borde='marrónCuero'),
        Rect(120, 200, 20, 20, relleno=gradiente('azulCieloProfundo','gainsboro',inicio='derecha-inferior'), borde='mocasín'),
        Rect(165, 200, 20, 20, relleno=gradiente('azulCieloProfundo','gainsboro',inicio='derecha-inferior'), borde='mocasín'),
        Rect(165, 230, 20, 20, relleno=gradiente('azulCieloProfundo','gainsboro',inicio='derecha-inferior'), borde='mocasín'),
        Rect(120, 230, 20, 20, relleno=gradiente('azulCieloProfundo','gainsboro',inicio='derecha-inferior'), borde='mocasín'),
        Rect(143, 250, 20, 30, relleno='marrónCuero', borde='negro'))

casa.centroX=245
casa.centroY=245
casa.visible=False

h=Oval(330,224,17,22,relleno=gradiente('rojo','naranja','amarillo','naranja',inicio='superior-izquierda'))
humo1 = Circulo(320,160,20,relleno=gradiente('gris','grisClaro',inicio='superior'),visible =True,opacidad=30)
humo2 = Circulo(320,120,20,relleno=gradiente('gris','grisClaro',inicio='superior'),visible =True,opacidad=20)
humo3 = Circulo(320,80,20,relleno=gradiente('gris','grisClaro',inicio='superior'),visible =True,opacidad=10)

derrumbe = Poligono(210,270,215,265,225,260,230,255,245,225,275,215,295,190,300,190,310,205,325,210,340,240,360,245,390,270,
    fill = 'marron', borde = 'black', visible = True)

derrumbe.centroX=210
derrumbe.centroY=280

r=Rotulo('AYUDA',200,230,fill='blanco',tamaño=20,rotarÁngulo=-15)
r4=Rotulo('GRACIAS',80,310,fill='blanco',tamaño=25,visible=False)
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
mun3.centroY=340

muñeco4=Grupo(
        Circulo(200,345,10, relleno='blanco',anchuraDeBorde=2),
        Linea(200,350,200,380,relleno='blanco',anchuraDeLínea=2),
        Linea(200,380,190,400,relleno='blanco',anchuraDeLínea=2),
        Linea(200,380,210,400,relleno='blanco',anchuraDeLínea=2),
        Linea(200,360,180,370,relleno='blanco',anchuraDeLínea=2),
        Linea(200,360,220,370,relleno='blanco',anchuraDeLínea=2))
muñeco4.centroX=110
muñeco4.visible=False
muñeco5=Grupo(
        Circulo(200,345,10, relleno='blanco',anchuraDeBorde=2),
        Linea(200,350,200,380,relleno='blanco',anchuraDeLínea=2),
        Linea(200,380,190,400,relleno='blanco',anchuraDeLínea=2),
        Linea(200,380,210,400,relleno='blanco',anchuraDeLínea=2),
        Linea(200,360,180,370,relleno='blanco',anchuraDeLínea=2),
        Linea(200,360,220,370,relleno='blanco',anchuraDeLínea=2))
muñeco5.centroX=85
muñeco5.visible=False
muñeco6=Grupo(
        Circulo(200,345,10, relleno='blanco',anchuraDeBorde=2),
        Linea(200,350,200,380,relleno='blanco',anchuraDeLínea=2),
        Linea(200,380,190,400,relleno='blanco',anchuraDeLínea=2),
        Linea(200,380,210,400,relleno='blanco',anchuraDeLínea=2),
        Linea(200,360,180,370,relleno='blanco',anchuraDeLínea=2),
        Linea(200,360,220,370,relleno='blanco',anchuraDeLínea=2))
muñeco6.centroX=50
muñeco6.visible=False
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
    
    carro1.centroX += 4
    muñeco.centroX += 4
    muñeco2.centroX += 3
    mun3.centroX += 3
    if carro1.centroX > 430:
        muñeco.centroX = -20
        muñeco2.centroX = -30
        muñeco2.alFrente()
        mun3.centroX = -20

    if carro1.centroX > 380:
           muñeco2.centroX=310
           muñeco.centroX=350
           mun3.centroX=370


    if carro1.centroX>=650:
         derrumbe.visible=False
         h.visible=False
         humo1.visible=False
         humo3.visible=False
         humo2.visible=False
         casa.visible=True
         c.relleno='red'
         r.visible=False
         muñeco6.visible=True
         muñeco5.visible=True
         muñeco4.visible=True
         r4.visible=True
         





cmu_graphics.run()


