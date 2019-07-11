import arcade
import timeit

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Space Adventure"

HALF_SQUARE_WIDTH = 2.5
HALF_SQUARE_HEIGHT = 2.5
SQUARE_SPACING = 10

class MyGame(arcade.Window):
    # Main application class

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)

        self.draw_time = 0
        self.shape_list = None
    
    def setup(self):
        self.shape_list = arcade.ShapeElementList()

        point_list = []
        color_list = []