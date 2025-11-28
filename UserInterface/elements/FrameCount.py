import pygame

class FrameCount():
    def __init__(self, clock):
        self.clock = clock
        self.fps_front = pygame.font.Font(None, 16)

    def get_fps_text(self):
        fps = self.clock.get_fps()
        fps_text = self.fps_front.render(f"FPS: {int(fps)}", True, (255, 255, 255))
        return fps_text