import pygame
import config

from GameObjects.Background import Background
from GameObjects.Floor import Floor
from GameObjects.Bird import Bird

# Inicializar o Pygame 
pygame.init()

# Instancia clock
clock = pygame.time.Clock()

# Configurações da tela
screen = pygame.display.set_mode(config.WINDOW_SIZE)           # Define o tamanho da tela
pygame.display.set_caption("Flappy")

# Carrega o background
background = Background(sprite_name="background-day.png", speed=config.BACKGROUND_SPEED, chunk_count=3)
background.load_sprite()
floor = Floor(sprite_name="base.png", speed=config.BACKGROUND_SPEED*3, chunk_count=3, y=400)
floor.load_sprite()

# Carrega o passáro
bird = Bird(name="José", color="yellow", x=config.WINDOW_SIZE[0]/3, y=config.WINDOW_SIZE[1]/2)

# Controle de animação
ANIMATION_SPEED = 580
frame_count = 0

# Font do texto
font = pygame.font.Font(None, 36)

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
    screen.blit(bird.load_frame(), (bird.x, bird.y))

    # Começa a gambiarra para mostrar FPS
    fps = clock.get_fps()
    fps_text = font.render(f"FPS: {int(fps)}", True, (255, 255, 255))
    screen.blit(fps_text, (10, 10))
    # Finaliza a gambiarra para mostrar FPS

    pygame.display.update()                             # Atualiza a tela
    clock.tick(config.FPS)                              # Controla os frames por segundo

pygame.quit()