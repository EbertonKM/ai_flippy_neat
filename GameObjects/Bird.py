import os
import pygame
import config
import random

class Bird:
    def __init__(self, name, color, x, y):
        self.name = name
        self.color = color
        self.x = x
        self.y = y
        self.angle = 0
        self.velocity = 0
        self.height = self.y
        self.frames = None
        self.cframes = None
        self.collider_radius = 15

        # Garante que a cor seja válida
        if self.color not in config.AVALIABLE_COLORS:
            self.color = config.AVALIABLE_COLORS[random.choice(range(len(config.AVALIABLE_COLORS)))]
            print(f"[WARNING] Cor inválida para o pássaro {self.name}. Definindo cor aleatória: {self.color}")

    def load_frames(self):
        try:
            self.frames = [
                pygame.image.load(os.path.join(config.TEXTURES_DIR, f"bird_{self.color}{i}.png")).convert_alpha()
                for i in range(1, 4)
            ]
            self.cframe = self.frames[0] # Define o frame do índice 0 como o primeiro
            print(f"[DEBUG] Frames carregados para {self.name}: {self.frames}")
        except FileNotFoundError as e:
            print(f"[ERRO] Não foi possível carregar os frames para {self.name}: e")
            raise
    
    def move(self):
        if self.velocity < config.MAX_FALLING_SPEED:
            self.velocity += config.GRAVITY
        self.y += self.velocity

        if self.y > 530:
            self.y = -30

        if self.velocity < 0 or self.y < self.height + 50:
            if self.angle < config.ROTATION_MAX_ANGLE:
                self.angle = config.ROTATION_MAX_ANGLE
        else:
            if self.angle > -90:
                self.angle -= config.ROTATION_SPEED

    def jump(self):
        self.velocity = config.FLAP_POWER
        self.height = self.y

    def collided_with_floor(self):
        if self.y + self.cframe.get_height() >= config.FLOOR_HEIGHT:
            return True
        return False
    
    def draw(self, screen):
        self.cframe = self.frames[(pygame.time.get_ticks() // 200) % len(self.frames)]
        rotated_sprite = pygame.transform.rotate(self.cframe, self.angle)
        rect = rotated_sprite.get_rect(center=(self.x, self.y))
        screen.blit(rotated_sprite, rect)

        if config.DEBUG:
            pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.collider_radius, 1)


    # Exibe o nome do passáro acima dele
    def show_name(self, screen):
        font = pygame.font.Font(None, 20)
        name_text = font.render(self.name, True, (255, 255, 255))
        screen.blit(name_text, (self.x - 15, self.y - 25))