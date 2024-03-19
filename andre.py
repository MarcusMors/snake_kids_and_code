import pygame
import random
import time

pygame.init()

snake_block = 10
snake_velocidad = 10

pantalla_ancho = 600
pantalla_altura = 600


window = pygame.display.set_mode((pantalla_ancho, pantalla_altura))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

font_style = pygame.font.Font(None, 50)
score_font = pygame.font.Font(None, 35)

def crear_numero_random(rango_inicio, rango_final):
    return crear_numero_random(rango_inicio, rango_final)

def our_snake(snake_block, snake_List):
    for x in snake_List:
        pygame.draw.rect(window, (0, 255, 0), pygame.Rect(x[0], x[1], snake_block, snake_block))

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [pantalla_ancho / 2, pantalla_altura / 2])

def gameLoop():
    game_over = False
    mostrar_menu = False

    #              R G   B
    color_negro = (0, 0, 0)
    color_rojo = (255, 0, 0)
    color_azul = (0,0,255)
    color_cafe = (101,67,33)

    x1 = pantalla_ancho // 2
    y1 = pantalla_altura // 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    ###########################################
    # numeros aleatorios
    ###########################################
    num_rand = crear_numero_random(0, pantalla_ancho - snake_block) / snake_block
    comida_x = round(num_rand) * snake_block

    num_rand = crear_numero_random(0, pantalla_ancho - snake_block) / snake_block
    comida_y = round(num_rand) * snake_block

    contador = 0
    pared = [[2,3],[2,4],[2,5],[2,6],[2,7]]
    pared2 = [[3,6],[4,6],[5,6],[6,6],[7,6]]

    paredes_largas = [pared, pared2]
    for pared in paredes_largas:
        pass
    num_paredes = 15
    paredes = [ ]
    # num_rand = crear_numero_random(0, pantalla_ancho - snake_block) / snake_block

    a = 0
    while a < 15:
        print(a)
        x = crear_numero_random(0,pantalla_altura/10)
        y = crear_numero_random(0, pantalla_ancho/10)
        paredes.append([x,y])
        a += 1

    print(paredes)


    num_rand = crear_numero_random(0, pantalla_ancho - snake_block) / snake_block
    pared_x = round(num_rand) * snake_block

    num_rand = crear_numero_random(0, pantalla_ancho - snake_block) / snake_block
    pared_y = round(num_rand) * snake_block

    # mientras no game_over
    while not game_over:

        print(f"x1: {x1}, y1: {y1}")

        ###########################################
        # DETECTOR DE TECLAS
        ###########################################
        print("aaaaaaaaaaaaaa")
        if contador > 0:
            contador = contador - 1
        print(contador)


        while mostrar_menu == True:
            window.fill((0, 0, 0))
            message("Perdiste!", (255, 255, 255))
            message("Presiona [S]alir or [J]ugar otra vez", (255, 255, 255))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s or event.key == pygame.K_ESCAPE:
                        game_over = True
                        mostrar_menu = False
                    if event.key == pygame.K_j:
                        gameLoop()
                if event.type == pygame.QUIT:
                    game_over = True
                    mostrar_menu = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #tecla esc
                game_over = True
                mostrar_menu = False
            if event.type == pygame.KEYDOWN: # todas las demas teclas
                if event.key == pygame.K_ESCAPE:
                    game_over = True
                    mostrar_menu = False
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_SPACE:
                    contador = 3
                    print("espacio fue presionado")

        ###########################################
        # DETECTOR DE COLISIONES
        ###########################################

        # aca se hace el teletransporte
        if x1 >= pantalla_ancho or x1 < 0 or y1 >= pantalla_altura or y1 < 0:
            print("tocaste el borde")
            mostrar_menu = True

        x1 += x1_change
        y1 += y1_change
        window.fill(color_negro)

        # pygame.draw.rect(window, color_rojo, pygame.Rect(comida_x, comida_y, snake_block, snake_block))
        pygame.draw.rect(window, color_rojo, (comida_x, comida_y, snake_block, snake_block))
        # pygame.draw.rect(pared)

        print
        a = 0
        while a < 15:
            pared_x = paredes[a][0]
            pared_y = paredes[a][1]
            pygame.draw.rect(window, color_cafe, (pared_x*10, pared_y*10, snake_block, snake_block))

            a=a+1

        snake_Head = [x1,y1]
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            # del snake_List[0]
            snake_List.pop(0)

        for x in snake_List[:-1]:
            if x == snake_Head:
                mostrar_menu = True
        print("a")

        for b in pared:
            print(b)
            pygame.draw.rect(window, color_cafe, (b[0]*snake_block, b[1]*snake_block, snake_block, snake_block))

        ###########################################
        # DIBUJADOR
        ###########################################
        # alternative
        # reverse for

        our_snake(snake_block, snake_List)

        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(crear_numero_random(0, pantalla_ancho - snake_block) / snake_block) * snake_block
            comida_y = round(crear_numero_random(0, pantalla_altura - snake_block) / snake_block) * snake_block
            Length_of_snake += 1
        # cosas

        if contador < 1:
            a = 0
            while a < 15:
                if x1 == paredes[a][0]*10 and y1 == paredes[a][1]*10:
                    mostrar_menu = True
                    break
                a =a + 1

            for bloque in pared:
                if x1 == bloque[0]*snake_block and y1 == bloque[1]*snake_block:
                    mostrar_menu = True
                    break


        clock.tick(snake_velocidad)





    pygame.quit()
    quit()

gameLoop()
