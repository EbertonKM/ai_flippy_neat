from Abstract.SceneElement import SceneElement
import pygame
import os
import config

class Floor(SceneElement):
    def load_sprite(self):
        sprite = pygame.image.load(os.path.join(
            config.TEXTURES_DIR, self.sprite_name
            )).convert_alpha()
        self.bg_sprite = pygame.transform.scale2x(sprite)
        self.chunk_width = self.bg_sprite.get_width()

        for x in range(self.chunk_count):
            self._chunks.append([self.bg_sprite, x * self.chunk_width])