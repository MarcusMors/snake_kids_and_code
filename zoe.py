import sys

import pygame

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la pantalla
ancho, altura = 800, 600
screen = pygame.display.set_mode((ancho, altura))

# Cargar la imagen y ajustar su tamaño
tanque = pygame.image.load("tanque.png")
tanque_ancho, tanque_alto = tanque.get_size()
new_size = (int(tanque_ancho / 2), int(tanque_alto / 2))  # Reducción a la mitad
image = pygame.transform.scale(tanque, new_size)
image_rect = image.get_rect()

# Establecer la posición inicial
x, y = ancho / 2, altura - tanque_alto / 2

image_rect.topleft = (x, y)

# Configurar el reloj para controlar la velocidad de actualización
clock = pygame.time.Clock()

# Configurar variables de disparo
bullet_speed = 8
generar_bala = False

#          R  G  B
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (10, 60, 225)
blanco = (255, 255, 255)
negro = (0, 0, 0)

# Bucle principal del juego

y_bala = y
correr_juego = True
while correr_juego:
    # Limpiar la pantalla
    screen.fill((255, 255, 255))

    print(f"x_tanque: {x}, y_tanque: {y}")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            correr_juego = False
            print("break game")
            break

        # pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                correr_juego = False
                print("break game")
                break
            if event.key == pygame.K_SPACE:
                # Iniciar el disparo cuando se presiona la tecla de espacio
                print("generar bala!")
                generar_bala = True
                y_bala = y

    # Verificar si se presiona la tecla de flecha izquierda
    # Disparar cuando se está disparando
    if generar_bala:
        y_bala -= 5
        print(f"x:{x},y_bala{y_bala}")
        pygame.draw.rect(screen, rojo, (x, y_bala, 40, 40))
    if y_bala < 0:
        generar_bala = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x += 5
    if keys[pygame.K_LEFT]:
        x -= 5
    image_rect.topleft = (x, y)


    # Dibujar la imagen en la pantalla
    screen.blit(image, image_rect)
    # Actualizar la pantalla
    pygame.display.flip()

    # Establecer la velocidad de actualización
    clock.tick(60)  # 60 fotogramas por segundo, ajusta según sea necesario

pygame.quit()
quit()
