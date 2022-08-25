import pygame
from enemigos import enemigo

tamano = 100
azul=(152, 217, 234)
verde=(0, 170, 0)

class Mapa:
    piso=pygame.image.load("piso.png")#manda a llamar imagen del piso
    espacio = 0
    enemigos = []#lista de enemigos
    def init(self, pantalla):#inicializar a los enemigos
        f = open("mapa.txt", "r")
        for (idx, fila) in enumerate(f):
            for (idx2, col) in enumerate(fila):
                posx = idx2 * tamano - self.espacio
                posy = idx * tamano
                if col == "3":#indica que por cada numero 3 en mapa.txt aparecera un enemigo
                    nuevo_enemigo = enemigo()
                    nuevo_enemigo.init(pantalla, posx, posy)
                    self.enemigos.append(nuevo_enemigo)
        f.close()


    def Actializar(self, mario):
        for enem in self.enemigos:#por cada enemigo en lista de enemigos se va a actualizar
            enem.actualizar(mario, self.espacio)
    
    def dibujar(self, pantalla, mario):#se mandara a la pantalla
        #If con el cual se podra recorrer/mover el mapa a la izq o der
        if mario.x > 1000:
            mario.x = 1000
            self.espacio += mario.velocidad
        if mario.x < 300  and self.espacio > 0:
            mario.x = 300
            self.espacio -= mario.velocidad
        if self.espacio < 0:
            self.espacio = 0

            
        f = open("mapa.txt", "r")#se manda a llamar archivo del mapa, "r"=reading, este leera el archivo
        for (idx, fila) in enumerate(f): # idx=indice, por cada fila en("in") nuestro archivo
            for(idx2, col) in enumerate(fila):#y por cada columna en una fila
                posx=idx2 * 100 - self.espacio#posicion "x" sera igual a indice2 tendra un cuadro de 100px 
                posy=idx * 100
                if col=="1":#dibujar cielo representado en  mapa.txt con "1" 
                    pygame.draw.rect(pantalla, azul, (posx, posy, tamano * 2, tamano))
                if col=="2" or col=="3":#dibujar cielo representado en  mapa.txt con "2"
                    rect = mario.parado.get_rect(x=mario.x, y=mario.y)#Dibujara un rectangulo con el cual podra ocupar de plataforma
                    bloque = pygame.draw.rect(pantalla, verde, (posx, posy, tamano *2, tamano))
                    pantalla.blit(pygame.transform.scale(self.piso, (tamano * 2,tamano)),(posx, posy))
                    if bloque.colliderect(rect):#Este if sera si el jugador choca con el bloque se podra subir
                        if rect.y + rect.height < posy + 10 and rect.x + rect.width > posx and rect.x < posx + (tamano * 2):
                            mario.tierra = True
                        #Aquí se declara para cuando se choque debajo de las plataformas y no se pase a traves de ellos  
                        elif rect.y > posy + tamano -20 and rect.x + rect.width > posx and rect.x < posx + (tamano * 2):
                            mario.velocidady = mario.gravedad
                        #Aquí se declara para cuando se choque a los lados de las plataformas y no se pase a traves de ellos    
                        elif rect.x + rect.width > posx and rect.x < posx + tamano * 2:
                            if mario.direccion_actual == 1:
                                mario.x =posx - rect.width
                            else:
                                mario.x = posx + tamano * 2

        for enem in self.enemigos:# se dibujan enemigos en el mapa
            enem.dibujar(pantalla, self.espacio)
        f.close()
