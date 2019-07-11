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
        # Credit for complex shape list code: http://arcade.academy/examples/shape_list_demo.html

        self.shape_list = arcade.ShapeElementList()

        point_list = []
        color_list = []

        for x in range(0, SCREEN_WIDTH, SQUARE_SPACING):
            for y in range(0, SCREEN_HEIGHT, SQUARE_SPACING):

                # calculate 4 points of the rectangle if x and y are the center coords
                top_left_corner = (x - HALF_SQUARE_WIDTH, y + HALF_SQUARE_HEIGHT)
                top_right_corner = (x + HALF_SQUARE_WIDTH, y + HALF_SQUARE_HEIGHT)
                bottom_right_corner = (x + HALF_SQUARE_WIDTH, y - HALF_SQUARE_HEIGHT)
                bottom_left_corner = (x - HALF_SQUARE_WIDTH, y - HALF_SQUARE_HEIGHT)

                # Add points to point_list
                point_list.append(top_left_corner)
                point_list.append(top_right_corner)
                point_list.append(bottom_right_corner)
                point_list.append(bottom_left_corner)

                # add color to each point
                for i in range(4):
                    color_list.append(arcade.color.BLACK)
        
        shape = arcade.create_rectangles_filled_with_colors(point_list, color_list)
        self.shape_list.append(shape)