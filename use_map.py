import pygame
import random
import time

pygame.init()

snake_block = 10
# snake_block = 20
# snake_block = 30
# snake_block = 40
snake_velocidad = 10

# MAPA_0 = [
#     "              ",
#     "  ##          ",
#     "  ##          ",
#     "              ",
#     "          ### ",
#     "  ####    #   ",
#     "          #   ",
#     "              ",
# ]

# MAPA = MAPA_0

pantalla_ancho = 300
# pantalla_ancho = len(MAPA[0]) * snake_block
pantalla_altura = 300
# pantalla_altura = len(MAPA) * snake_block


window = pygame.display.set_mode((pantalla_ancho, pantalla_altura))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()





font_style = pygame.font.Font(None, 50)
score_font = pygame.font.Font(None, 35)

def our_snake(snake_block, snake_List):
    for x in snake_List:
        pygame.draw.rect(window, (0, 255, 0), pygame.Rect(x[0], x[1], snake_block, snake_block))

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [pantalla_ancho / 2, pantalla_altura / 2])

def gameLoop():
    game_over = False
    mostrar_menu = False

    color_negro = (0, 0, 0)
    color_rojo = (255, 0, 0)

    x1 = pantalla_ancho // 2
    y1 = pantalla_altura // 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    num_rand = random.randrange(0, pantalla_ancho - snake_block) / snake_block
    foodx = round(num_rand) * snake_block

    num_rand = random.randrange(0, pantalla_ancho - snake_block) / snake_block
    foody = round(num_rand) * snake_block

    # mientras no game_over
    while not game_over:

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
            if event.type == pygame.QUIT:
                game_over = True
                mostrar_menu = False
            if event.type == pygame.KEYDOWN:
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

        # aca se hace el teletransporte
        if x1 >= pantalla_ancho or x1 < 0 or y1 >= pantalla_altura or y1 < 0:
            mostrar_menu = True

        x1 += x1_change
        y1 += y1_change
        window.fill(color_negro)

        # pygame.draw.rect(window, color_rojo, pygame.Rect(foodx, foody, snake_block, snake_block))
        pygame.draw.rect(window, color_rojo, (foodx, foody, snake_block, snake_block))

        snake_Head = [x1,y1]
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            # del snake_List[0]
            snake_List.pop(0)

        for x in snake_List[:-1]:
            if x == snake_Head:
                mostrar_menu = True

        # alternative
        # reverse for

        our_snake(snake_block, snake_List)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, pantalla_ancho - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, pantalla_altura - snake_block) / snake_block) * snake_block
            Length_of_snake += 1

        clock.tick(snake_velocidad)

    pygame.quit()
    quit()

gameLoop()

