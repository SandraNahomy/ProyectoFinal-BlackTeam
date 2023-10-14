from cmu_graphics import *

app.fondo=gradiente('azulCieloProfundo','azulClaro',inicio='superior')

#Bunker
Rect(0,120,400,400,relleno='verdeBosque')
Rect(10,128,380,265,borde='negro',anchuraDeBorde=4,relleno=gradiente('gris','grisOscuro','grisOscuro','gris',inicio='superior'))

#Escalera
Línea(180,130,180,390)
Línea(210,130,210,390)
Línea(195,130,195,390,anchuraDeLínea=28,guión=(4,9),relleno='nieve')

#Persona en la escalera
Circulo(195,180,6.5)
Linea(195,180,195,210)
Linea(195,195,185,185)
Linea(195,195,205,185)
Linea(195,210,190,220)
Linea(195,210,200,220)

#Personas en el bunker
Circulo(50,340,7)
Línea(50,340,50,370)
Línea(50,355,40,370)
Línea(50,355,62,370)
Línea(50,370,40,385)
Línea(50,370,60,385)

#Cajón
Rect(320,350,65,38,relleno='marrónCuero')
Rect(324,354,59,33,relleno='granate',borde='negro')
cmu_graphics.run() 