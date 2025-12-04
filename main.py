import pygame
import config

from GameObjects.Background import Background
from GameObjects.Floor import Floor
from GameObjects.Bird import Bird
from GameObjects.Pipe import Pipe
from UserInterface.InterfaceManager import InterfaceManager

# Inicializar o Pygame 
pygame.init()

# Instancia clock
clock = pygame.time.Clock()

# Configurações da tela
screen = pygame.display.set_mode(config.WINDOW_SIZE)           # Define o tamanho da tela
pygame.display.set_caption("Flappy")

user_interface = InterfaceManager(screen, clock)

# Carrega o background
background = Background(sprite_name="background-day.png", speed=config.BACKGROUND_SPEED, chunk_count=3)
background.load_sprite()
floor = Floor(sprite_name="base.png", speed=config.BACKGROUND_SPEED*3, chunk_count=3, y=config.FLOOR_HEIGHT)
floor.load_sprite()

# Carrega o passáro
bird = Bird(name="José", color="yellow", x=config.WINDOW_SIZE[0]//3, y=config.WINDOW_SIZE[1]//2)
bird.load_frames()

# Carrega os cano (lá ele)
pipes = [Pipe(300)]

# Loop do jogo
running = True

while(running):
    for event in pygame.event.get():                    # Verifica os eventos
        if event.type == pygame.QUIT:                   # Se o evento foi "Fechar"
            running = False                             # Sai do loop e fecha o jogo
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird.jump()
    
    # Atualiza a posição fundo e o piso
    background.move()
    floor.move()
    # Renderiza o fundo e o piso
    background.draw(screen)
    floor.draw(screen)

    # Atualiza o passário
    bird.move()
    bird.draw(screen)
    bird.show_name(screen)

    # Atualiza os canos
    for pipe in pipes:
        pipe.move()
        pipe.draw(screen)

    if len(pipes) == 0 or pipes[-1].x < config.WINDOW_SIZE[0] - 200:
        pipes.append(Pipe(config.WINDOW_SIZE[0]))

    if pipes and pipes[0].x < -pipes[0].UPPER_PIPE.get_width():
        pipes.pop(0)

    user_interface.update()
    pygame.display.update()                             # Atualiza a tela
    clock.tick(config.FPS)                              # Controla os frames por segundo

pygame.quit()