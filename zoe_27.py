puntaje=0
mensaje = "The Game End!"
#             Red Green Blue
text_color = (0,0,0)
import time
import sys
import pygame

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la pantalla
ancho, altura = 800, 600
screen = pygame.display.set_mode((ancho, altura))
pygame.display.set_caption("Juego con Pygame")

font = pygame.font.Font(None, 36)  # Puedes cambiar el valor de 36 según tus preferencias

bg = pygame.image.load("bg.jpg")
# Cargar la imagen ffffffffffff9y_tanque ajustar su tamaño
image_tanque = pygame.image.load("tanque.png").convert_alpha()
tanque_ancho, tanque_alto = image_tanque.get_size()
new_size = (int(tanque_ancho / 2), int(tanque_alto / 2))  # Reducción a la mitad
tanque = pygame.transform.scale(image_tanque, new_size).convert_alpha()
tanque_rect = tanque.get_rect()


k = []
new_size = 0
numero_de_aliens=10

x_alien, y_alien = ancho / 2, 10

alien_image = pygame.image.load("aliens2.png").convert_alpha()

def rectangulos_de_aliens(alien_image):
    alien_ancho, alien_alto = alien_image.get_size()
    new_size_alien = (int(alien_ancho / 5), int(alien_alto / 5))  # Reducción a la mitad
    alien_image = pygame.transform.scale(alien_image, new_size_alien).convert_alpha()
    k = []
    i = 0
    while i < 10:
        k.append(alien_image.get_rect())
        i = i + 1

    dist = 90
    i = 0
    x_alien = 25

    while i < 10:
        print("i:", i)
        k[i].topleft = (x_alien + dist * i, y_alien)
        i = i + 1
    return k, alien_image


balas = []

k , alien_image = rectangulos_de_aliens(alien_image)
# k = rectangulos_de_aliens()




# Establecer la posición inicial

x_tanque, y_tanque = ancho / 2, altura - tanque_alto // 2

tanque_rect.topleft = (x_tanque, y_tanque)

# Configurar el reloj para controlar la velocidad de actualización
clock = pygame.time.Clock()


# Configurar variables de disparo
bullet_speed = 8
generar_bala = False
#      R  G  B
rojo = (255, 0, 0)

milisegundos = 0
ybala = -100000000000000000
xbala = 100000000000000000000
# Bucle principal del juego

deplazamiento = 50

p = [10, 10]


while True:
    # Limpiar la pantalla
    # screen.fill((255, 255, 255))
    screen.blit(bg, (0, 0))

    # print(f"x_tanque: {x_tanque}, y_tanque: {y_tanque}")
    #######################################
    # DETECTOR DE TECLAS
    #######################################
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Iniciar el disparo cuando se presiona la tecla de espacio
                generar_bala = True
                balas.append([x_tanque + int(tanque_ancho / 4), y_tanque])

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
    if len(balas) > 0:
        i = 0
        while i < len(balas):
            print(f"i:{i}")
            balas[i][1] = balas[i][1] - 5
            ybala = balas[i][1]
            xbala = balas[i][0]
            pygame.draw.rect(screen, rojo, (xbala, ybala, 10, 12))

            if balas[i][1] < 0:
                del balas[i]
                i = i - 1

            i = i + 1

    # detectarcolicion
    i = 0
    g = 0
    while i < len(balas):
        while g < len(k):
            ybala = balas[i][1]
            xbala = balas[i][0]
            rect_bala = pygame.Rect(xbala, ybala, 10, 12)
            if rect_bala.colliderect(k[g]):
                print("colicion")
                del k[g]
                puntaje=puntaje+1
                g = g - 1

            g = g + 1

        i = i + 1
    text_surface = font.render(f"puntaje : {puntaje}", True, text_color)
    screen.blit(text_surface, (10, 10))  # Puedes ajustar las coordenadas según tus necesidades
    if milisegundos < 75:
        milisegundos = milisegundos + 1
    else:
        milisegundos = 0
        print("holaaaaaaaaaaaaaaaaaaaaaaa")
        x_alien = x_alien + deplazamiento
        for alien_rectangulo in k:
            alien_rectangulo.topleft = (alien_rectangulo.x + deplazamiento, y_alien)

        if x_alien > ancho - 400 or x_alien < 0:
            y_alien += abs(deplazamiento)
            deplazamiento *= -1

    # Dibujar la imagen en la pantalla

    screen.blit(tanque, tanque_rect)
    for alien_rectanguloooooo in k:
        screen.blit(alien_image, alien_rectanguloooooo)
    # input

    # Actualizar la pantalla
    pygame.display.flip()

    # Establecer la velocidad de actualización
    clock.tick(70)  # 60 fotogramas por segundo, ajusta según sea necesario
    white = (255, 255, 255)
    black=(0,0,0)
    # if puntaje >= numero_de_aliens :
    if puntaje >= 1 :
        break
screen.fill(white)
text_surface = font.render(mensaje, True, text_color)
screen.blit(text_surface, (ancho/2, altura/2))  # Puedes ajustar las coordenadas según tus necesidade
pygame.display.flip()
time.sleep(10)

