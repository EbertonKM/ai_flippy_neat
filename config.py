import os

# Configurações do sistema
WINDOW_SIZE = (288, 512)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEXTURES_DIR = os.path.join(BASE_DIR, "textures/")

# Configurações do background
BACKGROUND_SPEED = 0.012

# Configurações do pássaro
MAX_FALLING_SPEED = 1

# Configurações dos canos
PIPE_DISTANCE = 200