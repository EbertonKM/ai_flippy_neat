import pygame
import os
import config

from GameObjects.Background import Background
from GameObjects.Floor import Floor
from GameObjects.Bird import Bird

# Inicializar o Pygame 
pygame.init()

# Configurações da tela
screen = pygame.display.set_mode(config.WINDOW_SIZE)           # Define o tamanho da tela
pygame.display.set_caption("Pássaro Batedor de Asas")

# Carrega o background
background = Background()
background.load_sprite()
floor = Floor(y=400)
floor.load_sprite()

# Carrega o passáro
bird = Bird(name="José", color=3, x=config.WINDOW_SIZE[0]/3, y=config.WINDOW_SIZE[1]/2)

# Controle de animação
ANIMATION_SPEED = 580
frame_count = 0

# Font do texto
# font = pygame.font.SysFont("Roboto Slab", 36)
# text = font.render("Hello World", True, (255, 255, 255))
# text_rect = text.get_rect(center=(config.WINDOW_SIZE[0]//2, config.WINDOW_SIZE[1]//2))

# Loop do jogo
running = True

while(running):
    for event in pygame.event.get():                    # Verifica os eventos
        if event.type == pygame.QUIT:                   # Se o evento foi "Fechar"
            running = False                             # Sai do loop e fecha o jogo
    
    # Atualiza o fundo e o piso
    background.move()
    floor.move()

    # Renderiza o fundo e o piso
    background.draw(screen)
    floor.draw(screen)

    # Atualiza o passário
    bird.move()

    # screen.blit(text, text_rect)
    screen.blit(bird.load_frame(), (bird.x, bird.y))

    pygame.display.update()                             # Atualiza a tela

pygame.quit()