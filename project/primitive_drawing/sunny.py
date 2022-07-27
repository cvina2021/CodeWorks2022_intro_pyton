#import arcade module
import arcade

#define screen properties (width, height, and title)
screen_width = 600
screen_height = 600
screen_title = "New Game"

#open window
arcade.open_window(screen_width, screen_height, screen_title)

#set background color
arcade.set_background_color( (135,206,235))
#start render
arcade.start_render( )

#drawing code here
arcade.draw_circle_filled(300, 300, 75, arcade.color.YELLOW)

#finish render
arcade.finish_render( )
#run
arcade.run()
