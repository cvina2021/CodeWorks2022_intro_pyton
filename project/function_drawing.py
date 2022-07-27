import arcade
screen_width = 600
screen_height = 600
screen_title = "New Game"

def draw_bird(x, y):

    #arcade.draw_arc_outline(x,y,width, height, color, start_angle, end_angle, line_width)
    arcade.draw_arc_outline(x,y,20, 20, arcade.color.BLACK, 0, 180, 4)
    arcade.draw_arc_outline(x + 20,y,20, 20, arcade.color.BLACK, 0, 180, 4)
def main():
    arcade.open_window(screen_width, screen_height, screen_title)
    #set background color
    arcade.set_background_color( (123,215,255))

    arcade.start_render( )

    #call drawing functioncs
    draw_bird(300, 300)
    draw_bird(400, 150)
    draw_bird(100, 100)
    draw_bird(530, 350)

    arcade.finish_render()
    arcade.run()

if __name__ == "__main__":
    main()
