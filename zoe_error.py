import sys

import pygame

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la pantalla
ancho, altura = 800, 600
screen = pygame.display.set_mode((ancho, altura))
pygame.display.set_caption("Juego con Pygame")

# Cargar la imagen y_tanque ajustar su tamaño
image_tanque = pygame.image.load("tanque.png")


contador = 0
d = 1
alien_image = pygame.image.load("aliens2.png")

tanque_ancho, tanque_alto = image_tanque.get_size()
new_size = (int(tanque_ancho / 2), int(tanque_alto / 2))  # Reducción a la mitad

alien_ancho, alien_alto = alien_image.get_size()
new_size_alien = (int(alien_ancho / 5), int(alien_alto / 5))  # Reducción a la mitad

a = [9, 200]
b = [17, 200]
c = [60, 200]
balas = [a, b, c]


alien_image = pygame.transform.scale(alien_image, new_size_alien)

tanque = pygame.transform.scale(image_tanque, new_size)

tanque_rect = tanque.get_rect()


k = []
i = 0
while i < 15:
    k.append(alien_image.get_rect())
    i = i + 1


# Establecer la posición inicial
x_alien, y_alien = ancho / 2, 15

x_tanque, y_tanque = ancho / 2, altura - tanque_alto // 2

tanque_rect.topleft = (x_tanque, y_tanque)

# Configurar el reloj para controlar la velocidad de actualización
clock = pygame.time.Clock()


alien_separation = 90
i = 0

# print(k)
while i < 15:
    # print("i:", i)
    k[i].topleft = (x_alien + alien_separation * i, y_alien)
    i = i + 1


# Configurar variables de disparo
bullet_speed = 8
generar_bala = False
#      R  G  B
rojo = (255, 0, 0)

milisegundos = 75
ybala = -100000000000000000
xbala = 100000000000000000000
# Bucle principal del juego

deplazamiento = 50

game_over = False
while not game_over:
    # Limpiar la pantalla
    screen.fill((255, 255, 255))

    # print(f"x_tanque: {x_tanque}, y_tanque: {y_tanque}")
    #######################################
    # DETECTOR DE TECLAS
    #######################################

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Iniciar el disparo cuando se presiona la tecla de espacio
                generar_bala = True
                balas.append([x_tanque, y_tanque])
            if event.key == pygame.K_ESCAPE:
                game_over = True

    # Verificar si se presiona la tecla de flecha izquierda
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x_tanque += 5
    if keys[pygame.K_LEFT]:
        x_tanque -= 5

    tanque_rect.topleft = (x_tanque, y_tanque)

    #######################################
    # DIBUJAR BALAS
    #######################################
    if len(balas) != 0:
        i = 0
        while i < len(balas):
            balas[i][1] = balas[i][1] - 5
            ybala = balas[i][1]
            xbala = balas[i][0]
            pygame.draw.rect(screen, rojo, (xbala, ybala, 10, 12))
            i = i + 1

    if milisegundos < 75:
        milisegundos = milisegundos + 1
    else:
        milisegundos = 0
        print(
            """
---------------



paso



-----------------
"""
        )

        x_alien = x_alien + deplazamiento
        for alien_rectangulo in k:
            alien_rectangulo.topleft = (alien_rectangulo.x + deplazamiento, y_alien)

        if x_alien > ancho or x_alien < 0:
            y_alien += abs(deplazamiento)
            deplazamiento *= -1

    # Dibujar la imagen en la pantalla

    screen.blit(tanque, tanque_rect)
    for alien_rectangulo in k:
        screen.blit(alien_image, alien_rectangulo)
    # print(k)
    # Actualipzar la pantalla
    pygame.display.flip()

    # Establecer la velocidad de actualización
    clock.tick(60)  # 60 fotogramas por segundo, ajusta según sea necesario
