from UserInterface.elements.FrameCount import FrameCount

class InterfaceManager():
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock

        self.frame_count = FrameCount(self.clock)

    def update(self):
        self.screen.blit(self.frame_count.get_fps_text(), (10, 10))