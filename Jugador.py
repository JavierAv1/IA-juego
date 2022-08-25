import pygame
from enum import IntEnum

class direccion(IntEnum): #representa en que dirección va el jugador 
    Izq = 0
    der = 1

class condicion(IntEnum): #representa si el jugador esta parado, esta caminando o bien esta saltando(en el aire) 
    parado = 0 #representa estar parado
    caminando = 1 #representa estar caminando
    aire = 2 #representa estar brincando

class jugador: #clase que controla el movimiento del juego
    direccion_actual=direccion["der"] #dirección inicial que va a la derecha
    x = 0 #direccion inicial derecha x 0 y
    y = 0
    velocidadx = 0 #velocidad inicial
    velocidady = 0 #velocidad inicial
    caminando = [] #lista de imágenes que se llama caminando
    estado = 1 #el estado que va ser la que va a representar si el jugador está parado o caminando
    cuadro_actual = 0 #cuadro actual en el que esta parado
    contador = 0 #animación del contador
    parado = None 
    aire = None
    gravedad = 0 #va a hacer que el jugador caiga 
    tierra = False #booleano que representa si el jugador esta en el piso o no
    invertir = False #booleano que representa si el jugador va a la izquierda y la imagen se invierta
    def init(self, pantalla):
        self.invertir = False
        self.gravedad = 7 ##################################
        self.x = 0
        self.y = 0
        self.estado = condicion.aire
        self.velocidad = 5 #velocidad del jugador
        # Se mandaran a llamar imagenes las cuales representaran los diferentes estados del muñequito
        self.parado = pygame.image.load('parado.png').convert_alpha(pantalla)
        self.aire = pygame.image.load('aire.png').convert_alpha(pantalla)
        self.caminando.append(pygame.image.load('parado.png').convert_alpha(pantalla))
        self.caminando.append(pygame.image.load('caminando.png').convert_alpha(pantalla))
        self.parado.set_colorkey((255,255,255))
        self.parado= self.parado.convert()
        self.aire.set_colorkey((255,255,255))
        self.aire= self.aire.convert()

        for(idx, i) in enumerate(self.caminando):
            i.set_colorkey((255,255,255))
            self.caminando[idx] = self.caminando[idx].convert()

        self.cuadro_actual = 0 #Indica en el recuadro actual en el que se esta posicionado 
    #Aquí se definiran los controles/comandos para manejar al personaje 
    def eventos(self, event, pantalla):
        if event.type == pygame.KEYDOWN:#Agacharse
            if event.key ==pygame.K_UP and self.estado != condicion.aire:#brincar
                self.velocidady = -20
                self.estado = condicion.aire
                self.tierra = False #personaje no esta pisando la plataforma
            if event.key == pygame.K_q:
                self.y = 0
            if event.key == pygame.K_LEFT:# ir a la izquierda
                self.direccion_actual = direccion.Izq
                self.velocidadx = -self.velocidad
            if event.key == pygame.K_RIGHT:#ir a la derecha
                self.direccion_actual = direccion.der
                self.velocidadx = self.velocidad
            if event.key == pygame.K_SPACE and self.estado == 0:
                pass
        #Cuando se suelten las teclas este vuelva a su estado 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.velocidadx = 0
            if event.key == pygame.K_RIGHT:
                self.velocidady= 0
        #Aquí se iran actuañizando los valores con forme se vaya moviendo el presonaje
            
    def actualizar(self):# Se ira actualizando los estados cambiar a caminar o bien parar, brincar o cgacharse
        if self.tierra:
            self.velocidady = 0
            if self.velocidadx != 0:
                self.estado = condicion.caminando
            if self.velocidadx == 0:
                    self.estado = condicion.parado
        self.x += self.velocidadx
        if self.tierra == False:
            self.estado = condicion.aire
        if self.estado == condicion.aire:
            self.velocidady += 1
            if self.velocidady > self.gravedad:# si esta en el aire no podra brincar otra vez
                self.velocidady = self.gravedad
            self.y += self.velocidady
        if self.direccion_actual == direccion.Izq:# representa cuando el personaje avanza a la izquierda
            self.invertir = True
        else:
            self.invertir = False
        self.tierra = False

    def dibujar(self, pantalla):#aqui se mandan a llamar las acciones que se declararon anteriormente 
        if self.estado == condicion.parado:#Se dibuja a mario parado
            pantalla.blit(pygame.transform.flip(self.parado, self.invertir, False), (self.x, self.y))
        if self.estado == condicion.aire:#se dibuja mario brincando
            pantalla.blit(pygame.transform.flip(self.aire, self.invertir, False), (self.x, self.y))
        if self.estado == condicion.caminando: #se dibuja accion de caminar
            self.contador += 1
            if self.contador > 5:
                self.cuadro_actual += 1
                self.contador = 0
                if self.cuadro_actual > 1:
                    self.cuadro_actual = 0
            pantalla.blit(pygame.transform.flip(self.caminando[self.cuadro_actual], self.invertir, False), (self.x, self.y))#Dibuja  mario caminando
               