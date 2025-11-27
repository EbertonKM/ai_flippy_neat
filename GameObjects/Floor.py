import os
import pygame
import config

class Floor:
    SPEED = config.BACKGROUND_SPEED*3
    CHUNKS = 3

    def __init__(self, y):
        self.floor_sprite = None
        self.chunk_width = 0
        self.y = y
        self._chunks = []

    def load_sprite(self):
        self.floor_sprite = pygame.transform.scale2x(
            pygame.image.load(os.path.join(config. TEXTURE_DIR, "base.png")).convert_alpha()
            )
        self.chunk_width = self.floor_sprite.get_width()

        for x in range(self.CHUNKS):
            self._chunks.append([self.floor_sprite, x * self.chunk_width])

    def move(self, speed=None):
        current_speed = speed if speed is not None else self.SPEED
        for i, chunk in enumerate(self._chunks):
            chunk[1] -= current_speed
            if chunk[1] < -self.chunk_width:
                chunk[1] = self.get_last_chunk_offset() + self.chunk_width

    def draw(self, screen):
        for chunk in self._chunks:
            screen.blit(chunk[0], (chunk[1], self.y))

    def get_last_chunk_offset(self):
        offset = 0
        for chunk in self._chunks:
            if chunk[1] > offset:
                offset = chunk[1]
        return offset