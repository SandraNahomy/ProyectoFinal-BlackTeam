from cmu_graphics import *
app.fondo ='bisque'
Rect(0,0,400,70,relleno='tierra')
Rect(65,80,270,180, relleno=gradiente('blanco','cian',inicio='superior'), borde='negro')


Linea(200,80,200,260)
Óvalo(10,70,20,50, relleno='tierra')
Óvalo(30,70,20,50, relleno='tierra')
Óvalo(50,70,20,50, relleno='tierra')
Óvalo(70,70,20,50, relleno='tierra')
Óvalo(90,70,20,50, relleno='tierra')
Óvalo(110,70,20,50, relleno='tierra')
Óvalo(130,70,20,50, relleno='tierra')
Óvalo(150,70,20,50, relleno='tierra')
Óvalo(170,70,20,50, relleno='tierra')
Óvalo(190,70,20,50, relleno='tierra')
Óvalo(210,70,20,50, relleno='tierra')
Óvalo(230,70,20,50, relleno='tierra')
Óvalo(250,70,20,50, relleno='tierra')
Óvalo(270,70,20,50, relleno='tierra')
Óvalo(290,70,20,50, relleno='tierra')
Óvalo(310,70,20,50, relleno='tierra')
Óvalo(330,70,20,50, relleno='tierra')
Óvalo(350,70,20,50, relleno='tierra')
Óvalo(370,70,20,50, relleno='tierra')
Óvalo(390,70,20,50, relleno='tierra')
Rect(0,50,60,200, relleno='tierra')
Óvalo(10,250,20,50, relleno='tierra')
Óvalo(30,250,20,50, relleno='tierra')
Óvalo(50,250,20,50, relleno='tierra')
Rect(340,50,60,200, relleno='tierra')
Óvalo(350,250,20,50, relleno='tierra')
Óvalo(370,250,20,50, relleno='tierra')
Óvalo(390,250,20,50, relleno='tierra')
Rect(0,350,400,50, relleno='tierra')

Muñeco=Grupo(
    Circulo(300,220,30, relleno='blanco', anchuraDeBorde=2),
    Linea(300,220,300,320, relleno='blanco', anchuraDeLinea=10),
    Linea(300,320,345,366, relleno='blanco', anchuraDeLinea=10),
    Linea(300,320,255,366, relleno='blanco', anchuraDeLinea=10),
    Linea(300,266,338,293, relleno='blanco', anchuraDeLinea=10),
    Linea(300,266,262,293, relleno='blanco', anchuraDeLinea=10))
    
nube=Grupo(
    Óvalo(300,110,200,110, relleno='blanco'),
    Poligono(332,160,324,198,356,152, relleno='blanco'))
    
    
    
    
Muñeco1=Grupo(
    
    Circulo(300,220,30, relleno='negro', anchuraDeBorde=2),
    Linea(300,220,300,320, relleno='negro', anchuraDeLinea=10),
    Linea(300,320,345,366, relleno='negro', anchuraDeLinea=10),
    Linea(300,320,255,366, relleno='negro', anchuraDeLinea=10),
    Linea(300,266,338,293, relleno='negro', anchuraDeLinea=10),
    Linea(300,266,262,293, relleno='negro', anchuraDeLinea=10))
    
    
    
Muñeco.centroX = 400 - Muñeco.centroX
    

nube1=Grupo(
    Óvalo(300,110,200,110, relleno='blanco'),
    Poligono(332,160,324,198,356,152, relleno='blanco'))
    
nube.centroX = 400 - nube.centroX

Rect(50,70,110,80, relleno='ladrillo')
Rect(55,75,100,70, relleno='blanco')
Linea(105,75,105,145)
Linea(55,85,105,85, guion=True)
Linea(105,85,155,85, guion=True)
Linea(105,95,155,95, guion=True)
Linea(55,95,105,95, guion=True)
Linea(55,105,105,105, guion=True)
Linea(55,105,105,105, guion=True)
Linea(55,115,105,115, guion=True)
Linea(105,115,155,115, guion=True)
Linea(105,105,155,105, guion=True)
Linea(55,125,105,125, guion=True)
Linea(105,125,155,125, guion=True)
Linea(55,135,105,135, guion=True)
Linea(105,135,155,135, guion=True)
Linea(266,110,295,137, relleno='verde')
Linea(295,137,350,77, relleno='verde')

cmu_graphics.run()




