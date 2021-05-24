BOARD_RESOLUTION = (9, 9)

STONE_SIZE = 40
GAP_SIZE = 80
SCREEN_RESOLUTION = ((BOARD_RESOLUTION[0]-1) * STONE_SIZE, (BOARD_RESOLUTION[1]-1) * STONE_SIZE)
SCREEN_RESOLUTION_WITH_GAPS = (SCREEN_RESOLUTION[0]+GAP_SIZE, SCREEN_RESOLUTION[1]+GAP_SIZE)

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)

PLAYER_TURN = BLACK