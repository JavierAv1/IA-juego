import pygame

class enemigo:
    x = 0 #posición incial del enemigo
    y = 0 #posición incial del enemigo
    pos_inicial = 0 #posición incial del enemigo
    velocidad = 0 #velocidad incial del enemigo
    imagenes =[] #imagen de los enemigos
    amplitud = 0 #ancho
    cuadro_actual = 0 
    contador = 0
    muerto = False #muerte del enemigo que inicia como falso
    origy = 0

    def init(self, pantalla, x, y):
        self.muerto = False
        self.cuadro_actual = 0
        self.x = x
        self.pos_inicial = x
        self.velocidad = 3
        self.imagenes.append(pygame.image.load('enemigo1.png').convert_alpha(pantalla))
        self.imagenes.append(pygame.image.load('enemigo2.png').convert_alpha(pantalla))
        self.imagenes.append(pygame.image.load('enemigo3.png').convert_alpha(pantalla))
        for imagen in self.imagenes:
            imagen.set_colorkey((0, 128, 255))
        self.amplitud = self.imagenes[0].get_width()
        self.origy = y
        self.y = self.origy - self.imagenes[0].get_width()
    def actualizar(self, mario, espacio):#Movimiento del enemigo mientras siga vivo
        if not self.muerto:
            self.contador +=1
            if self.contador > 10:
                self.contador = 0
                self.cuadro_actual += 1
                if self.cuadro_actual > 1:
                    self.cuadro_actual = 0
            self.x -= self.velocidad
            if self.x - espacio < self.pos_inicial - espacio - 100 or self.x - espacio > self.pos_inicial - espacio + 100 + self.amplitud:
                self.velocidad = -self.velocidad #delimita el area de movimiento del enemigo, si llega a su punto regresa a posicion inicial
            bloque = self.imagenes[0].get_rect(x=self.x - espacio, y=self.y)
            rect = mario.parado.get_rect(x=mario.x, y=mario.y)
            if bloque.colliderect(rect):# indica si mario aplasta al enemigo y variable muerto cambia a verdadero
                if rect.y + rect.height < bloque.y + 10 and rect.x + rect.width > bloque.x and rect.x < bloque.x + bloque.width:
                    self.muerto = True
                    self.cuadro_actual = 2 #cambia a 2 haciendo referencia a imagen de enemigo aplastado

        self.y = self.origy - self.imagenes[self.cuadro_actual].get_height()

    def dibujar(self, pantalla, espacio):# se dibuja el enemigo en la pantalla
        pantalla.blit(self.imagenes[self.cuadro_actual], (self.x - espacio, self.y))
