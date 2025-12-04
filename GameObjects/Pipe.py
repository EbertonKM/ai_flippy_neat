import os
import pygame
import random
import config

class Pipe():
    def __init__(self, x):
        self.x = x
        self.height = 0
        self.top = 0
        self.bottom = 0
        self.UPPER_PIPE = None
        self.LOWER_PIPE = None
        self.passed = False

        self.load_pipe_sprites()

    # Carrega as imagens dos campos
    def load_pipe_sprites(self):
        pipe_sprite_path = os.path.join(config.TEXTURES_DIR, 'pipe-green.png')
        self.pipe_sprite = pygame.image.load(pipe_sprite_path).convert_alpha()
        self.UPPER_PIPE = pygame.transform.flip(self.pipe_sprite, False, True)
        self.LOWER_PIPE = self.pipe_sprite

    def set_pipe_height(self):
        # Define alturas aleatórias para os canos
        max_pipe_height = config.WINDOW_SIZE[1] - config.GAP_SIZE - 100  # Evita sobreposição
        self.height = random.randint(50, max_pipe_height)
        self.top = self.height - self.UPPER_PIPE.get_height()
        self.bottom = self.height + config.GAP_SIZE

    def move(self):
        # Move os canos para a esquerda
        self.x -= config.FLOOR_PIPE_SPEED
    
    def collide(self, bird, screen=None):
        bird_center = bird.x + bird.cframe.get_width() // 2, bird.y + bird.cframe.get_height() // 2

        # Verifica colisão com o cano superior
        if self.x < bird_center[0] < self.x + self.UPPER_PIPE.get_width() and bird_center[1] < self.top + self.UPPER_PIPE.get_height():
            return True

        # Verifica colisão com o cano inferior
        if self.x < bird_center[0] < self.x + self.LOWER_PIPE.get_width() and bird_center[1] > self.bottom:
            return True

        return False

    def draw(self, screen):
        # Renderiza os canos na tela
        screen.blit(self.UPPER_PIPE, (self.x, self.top))
        screen.blit(self.LOWER_PIPE, (self.x, self.bottom))