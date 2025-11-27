import os
import pygame
import config
import random

class Bird:
    ROTATION_MAX_ANGLE = 25
    ROTATION_SPEED = 20
    GRAVITY = 0.0002
    FLAP_POWER = -2
    AVALIABLE_COLORS = ("blue", "red", "yellow", "black")

    def __init__(self, name, color, x, y):
        self.name = name
        self.color = self.AVALIABLE_COLORS[color]
        self.x = x
        self.y = y
        self.angle = 0
        self.velocity = 0
        self.height = self.y
        self.frames = None
        self.cframes = None

    def load_frame(self): # Completamente errado
        for i in (1, 3):
            self.frames = pygame.image.load(os.path.join(config.TEXTURES_DIR, f"bird_{self.color}{i}.png")).convert_alpha()
        self.cframes = self.frames
        return self.cframes
    
    def move(self):
        if self.velocity < config.MAX_FALLING_SPEED:
            self.velocity += self.GRAVITY
        self.y += self.velocity

        if self.y > 530:
            self.y = -30

        # Falta aplicar isso de fato ao sprite
        if self.velocity < 0 or self.y < self.height + 50:
            if self.angle < self.ROTATION_MAX_ANGLE:
                self.angle = self.ROTATION_MAX_ANGLE
        else:
            if self.angle > -90:
                self.angle -= self.ROTATION_SPEED