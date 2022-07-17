from turtle import position
import pyray
import constants

class VideoService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state 
    on the screen. 
    """

    def __init__(self, debug = False):
        """Constructs a new VideoService using the specified debug mode.
        
        Args:
            debug (bool): whether or not to draw in debug mode.
        """
        self._debug = debug
    
    def close_window(self):
        """Closes the window and releases all computing resources."""
        pyray.close_window()

    def clear_buffer(self):
        """Clears the buffer in preparation for the next rendering. This method should be called at
        the beginning of the game's output phase.
        """
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        self.draw_background()
        if self._debug == True:
            self.draw_background()
    
    def draw_actor(self, actor, centered=False):
        """Show the given actor's sprite on the screen.

        Args:
            actor (Actor): The actor to draw on screen.
        """ 
        sprite = actor.get_src() # sprite file path
        position = actor.get_position()
        x = position.get_x()
        y = position.get_y()

        texture = pyray.load_texture(sprite)
        pyray.draw_texture(texture, x, y, pyray.WHITE)

        
    def draw_actors(self, actors, centered=False):
        """Draws the text for the given list of actors on the screen.

        Args:
            actors (list): A list of actors to draw.
        """ 
        for actor in actors:
            self.draw_actor(actor, centered)
    def draw_score(self, score):
        """Recieves the current score and draws it on the screen"""
        pyray.draw_text(score, constants.WIDTH//2, 20, 15, pyray.WHITE)

    def flush_buffer(self):
        """Copies the buffer contents to the screen. This method should be called at the end of
        the game's output phase.
        """ 
        pyray.end_drawing()

    def is_window_open(self):
        """Whether or not the window was closed by the user.

        Returns:
            bool: True if the window is closing; false if otherwise.
        """
        return not pyray.window_should_close()

    def open_window(self):
        """Opens a new window with the provided title.

        Args:
            title (string): The title of the window.
        """
        pyray.init_window(constants.WIDTH, constants.HEIGHT, "Asteroids game")
        pyray.set_target_fps(constants.FRAME_RATE)

    def draw_background(self):
        """Draws the background texture on the screen."""
        texture = pyray.load_texture("Final-project/asteroids/game/images/starfield.png")
        pyray.draw_texture(texture, 0, 0, pyray.WHITE)
        

    def draw_game_over(self, final_score):
        """Draw a game over message and the final score on the screen."""
        texture = pyray.load_texture("Final-project/asteroids/game/images/starfield.png")
        pyray.draw_texture(texture, 0, 0, pyray.WHITE)
        pyray.draw_text(final_score, constants.WIDTH//2, 20, 15, pyray.WHITE)
        pyray.draw_text("GAME OVER", constants.WIDTH//2, constants.HEIGHT//2, 25, pyray.WHITE)

