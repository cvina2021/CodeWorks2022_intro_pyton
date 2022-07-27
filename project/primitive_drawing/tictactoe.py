#import arcade module
import arcade
#define screen properties (width, height, and title)
screen_width = 600
screen_height = 600
screen_title = "New Game"

#open window
arcade.open_window(screen_width, screen_height, screen_title)
#set background color
arcade.set_background_color((121,206,204))
#start render
arcade.start_render( )
#drawing code here
arcade.draw_lrtb_rectangle_filled(200, 210, 600, 0, arcade.color.WHITE)
arcade.draw_lrtb_rectangle_filled(400, 410, 600, 0, arcade.color.WHITE)
arcade.draw_lrtb_rectangle_filled(0, 600, 400, 390, arcade.color.WHITE)
arcade.draw_lrtb_rectangle_filled(0, 600, 200, 190, arcade.color.WHITE)
#finish render
arcade.finish_render( )
#run
arcade.run()
