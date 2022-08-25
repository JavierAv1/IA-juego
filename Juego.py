import pygame
from Mapa import Mapa
from Jugador import jugador


negro=(0,0,0)
blanco=(255,255,255)
pantalla_tamaño=(1300,700)#Dimensiones de la pantalla de juego
pantalla=pygame.display.set_mode(pantalla_tamaño)#Iniciar
reloj=pygame.time.Clock()
Termino=False
#Inciar/ Pantalla de inicio, dimensiones

mapa= Mapa()
mario =jugador()
mario.init(pantalla)

mapa.init(pantalla=pantalla)
while not Termino:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Termino= True
            #Eventos
        mario.eventos(event, pantalla)
    
    #Actualizar
    mario.actualizar()
    mapa.Actializar(mario)
    pantalla.fill(negro)
    
    #Dibujar
    mapa.dibujar(pantalla, mario)
    mario.dibujar(pantalla)
    pygame.display.flip()
    reloj.tick(60)