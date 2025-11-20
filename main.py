import pygame

pygame.init()

# Configurações da tela
WINDOW_SIZE = (360, 640)                                # Descreve o tamanho da tela
screen = pygame.display.set_mode(WINDOW_SIZE)           # Define o tamanho da tela
pygame.display.set_caption("Flap Bird")

# Configuração do passáro
bird_frames = [                                                                         # Carrega os sprite do pássaro
    pygame.image.load("textures/bird_yellow1.png"),
    pygame.image.load("textures/bird_yellow2.png"),
    pygame.image.load("textures/bird_yellow3.png")
]
bird_index = 0
bird_position = bird_frames[0].get_rect(center=(WINDOW_SIZE[0]//2, WINDOW_SIZE[1]//2))      # Define o posicionamento

# Controle de animação
ANIMATION_SPEED = 200
frame_count = 0

# Font do texto
# font = pygame.font.SysFont("Roboto Slab", 36)
# text = font.render("Hello World", True, (255, 255, 255))
# text_rect = text.get_rect(center=(WINDOW_SIZE[0]//2, WINDOW_SIZE[1]//2))

# Loop do jogo
running = True

while(running):
    for event in pygame.event.get():                    # Verifica os eventos
        if event.type == pygame.QUIT:                   # Se o evento foi "Fechar"
            running = False                             # Sai do loop e fecha o jogo
        
        # Atualiza animação do passáro
        frame_count += 1
        if frame_count >= ANIMATION_SPEED:
            bird_index = (bird_index + 1) % len(bird_frames)
            frame_count = 0

        screen.fill(9090)                                # Se não define uma cor para a tela toda
        # screen.blit(text, text_rect)

        screen.blit(bird_frames[bird_index], bird_position.topleft)

        pygame.display.update()                         # Atualiza a tela

# pygame.QUIT()