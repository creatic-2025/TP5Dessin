"""
Créé par Dorian B. Girard le 15 Janvier 2026.
Une création d'une image statique avec Arcade.
"""
import arcade

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
WINDOW_TITLE = "Starting Template"


#RECTANGLES *
#CERCLES *
#TRIANGLES *
#ARC *
#ELLIPSE *
#LIGNE
#POLYGONE
#POINT
#TEXTE *

class GameView(arcade.View):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self):
        super().__init__()

        self.background_color = arcade.color.WHITE

        # If you have sprite lists, you should create them here,
        # and set them to None

    def reset(self):
        """Reset the game to the initial state."""
        # Do changes needed to restart the game here if you want to support that
        pass

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

    def on_draw(self):
        """
        Créé le couché de soleil avec des rectangles et des cercles.
        """
        self.clear()
        background_color = (255, 255, 255, 255)
        arcade.set_background_color(background_color)
        """
        Création des rectangles qui définit le couché de soleil
        """

        arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 335, 370, (255, 197, 79))
        arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 370, 405, (255, 164, 73))
        arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 405, 440, (255, 131, 66))
        arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 440, 475, (242, 131, 99))
        arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 475, 510, (228, 131, 132))
        arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 510, 545, (228, 106, 141))
        arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 545, 580, (227, 81, 150))
        arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 580, 615, (202, 105, 169))
        arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 615, 650, (176, 128, 188))
        arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 650, 685, (128, 124, 190))
        arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 685, SCREEN_HEIGHT, (79, 120, 192))

        """
        Créer le ballon de plage et la plage.
        """
        arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 0, 200, (236, 204, 162))
        arcade.draw_circle_filled(800, 130, 50, (255, 255, 255))
        arcade.draw_circle_filled(800, 130, 10, (0, 207, 250))
        arcade.draw_triangle_filled(800, 138, 780, 177, 820, 177, (253, 21, 0))
        arcade.draw_triangle_filled(809, 130, 847, 110, 847, 145, (255, 214, 38))
        arcade.draw_triangle_filled(793, 130, 755, 110, 755, 145, (1, 206, 253))
        arcade.draw_triangle_filled(800, 123, 780, 83, 820, 83, (0, 188, 64))
        arcade.draw_ellipse_filled(600, 170, 150, 60, (151, 112, 88))
        arcade.draw_ellipse_filled(650, 180, 150, 40, (151, 112, 88))
        arcade.draw_ellipse_filled(960, 180, 150, 40, (151, 112, 88))
        arcade.draw_ellipse_filled(700, 180, 150, 40, (151, 112, 88))
        arcade.draw_ellipse_filled(400, 180, 150, 40, (151, 112, 88))
        arcade.draw_ellipse_filled(520, 170, 150, 60, (151, 112, 88))
        arcade.draw_ellipse_filled(1000, 170, 150, 60, (151, 112, 88))
        arcade.draw_ellipse_filled(300, 170, 150, 60, (151, 112, 88))
        arcade.draw_ellipse_filled(820, 190, 150, 20, (151, 112, 88))

        """
        Le texte 
        """

        affichage = arcade.Text("plage.", 20, 40, arcade.csscolor.BLACK, 40)
        affichage.draw()

        """
        Créer l'océan avec les vagues
        """
        arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 200, 335, (0, 105, 148))
        arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 300, 335, (100, 178, 212))
        arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 265, 300, (50, 142, 180))

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main function """
    # Create a window class. This is what actually shows up on screen
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)

    # Create and setup the GameView
    game = GameView()

    # Show GameView on screen
    window.show_view(game)

    # Start the arcade game loop
    arcade.run()


if __name__ == "__main__":
    main()
