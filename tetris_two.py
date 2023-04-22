from settings import *
from tetrisShapes import TetShape

class Tetris:
    def __init__(self, app):
        self.app = app
        self.sprite_group = pg.sprite.Group() ## Add sprites
        self.tetrisShapes = TetShape(self)
    
    ## Makes the grid in the display
    def draw_grid(self):
        for x in range(FIELD_W):
            for y in range(FIELD_H):
                pg.draw.rect(self.app.screen, 'black', 
                             (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    ## Updates shapes and sprites
    def update(self):
        self.tetrisShapes.update()
        self.sprite_group.update()

    ## Draws the grid and sprites
    def draw(self):
        self.draw_grid()
        self.sprite_group.draw(self.app.screen)