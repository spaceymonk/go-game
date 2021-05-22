import pygame
import config
from objects import Stone


class App:
    def __init__(self):
        self._running = True
        self.DISPLAYSURF = None
        self.stones = []

    def on_init(self):
        pygame.init()
        self.DISPLAYSURF = pygame.display.set_mode(config.SCREEN_RESOLUTION_WITH_GAPS)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        # -------------------------------- draw board -------------------------------- #
        self.DISPLAYSURF.fill(config.GREEN)
        for i in range(config.BOARD_RESOLUTION[0]):
            xmin = i * config.STONE_SIZE + config.GAP_SIZE//2
            ymin = 0 + + config.GAP_SIZE//2
            xmax = i * config.STONE_SIZE + config.GAP_SIZE//2
            ymax = config.SCREEN_RESOLUTION[1] + config.GAP_SIZE//2
            pygame.draw.line(self.DISPLAYSURF, config.RED, (xmin, ymin), (xmax, ymax))
        for i in range(config.BOARD_RESOLUTION[1]):
            xmin = 0 + + config.GAP_SIZE//2
            ymin = i * config.STONE_SIZE + config.GAP_SIZE//2
            xmax = config.SCREEN_RESOLUTION[0] + config.GAP_SIZE//2
            ymax = i * config.STONE_SIZE + config.GAP_SIZE//2
            pygame.draw.line(self.DISPLAYSURF, config.RED, (xmin, ymin), (xmax, ymax))
        for i in range(config.BOARD_RESOLUTION[0]):
            for j in range(config.BOARD_RESOLUTION[1]):
                s = 4
                x = i * config.STONE_SIZE + config.GAP_SIZE//2
                y = j * config.STONE_SIZE + config.GAP_SIZE//2
                pygame.draw.circle(self.DISPLAYSURF, config.RED, (x, y), s)
        # -------------------------------- draw stones ------------------------------- #
        for stone in self.stones:
            stone.draw(self.DISPLAYSURF)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
