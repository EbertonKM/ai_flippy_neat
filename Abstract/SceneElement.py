import pygame
import config
import os

from abc import ABC, abstractmethod

class SceneElement(ABC):
    def __init__(self, sprite_name, speed, chunk_count, y=0):
        self.sprite_name = sprite_name
        self.speed = speed
        self.chunk_count = chunk_count
        self.bg_sprite = None
        self.chunk_width = 0
        self.y = y
        self._chunks = []

    @abstractmethod
    def load_sprite(self):
        ...

    def move(self, speed=None):
        current_speed = speed if speed is not None else self.speed
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