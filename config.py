import os

# Configurações do sistema
DEBUG = True

WINDOW_SIZE = (288, 512)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEXTURES_DIR = os.path.join(BASE_DIR, "textures/")

FPS = 60

# Configurações do background
BACKGROUND_SPEED = 1
FLOOR_PIPE_SPEED = BACKGROUND_SPEED * 3

# Configurações do chão
FLOOR_HEIGHT = 400

# Configurações do pássaro
GRAVITY = 0.5
FLAP_POWER = -7
MAX_FALLING_SPEED = 15

ROTATION_MAX_ANGLE = 25
ROTATION_SPEED = 20
AVALIABLE_COLORS = ["black", "blue", "green", "orange", "pink", "purple", "red", "teal", "toxic", "white", "yellow"]

# Configurações dos canos
PIPE_DISTANCE = 200
GAP_SIZE = 150