import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.services.video_service import VideoService

class HandleCollisionsAction(Action):
    """
    An update action that handles icolissions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when a cycle collides
    with the other one or when the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction.
        
        Attributes:
        _is_game_over (boolean): It is False until there is a colission between the ship and an asteroid.
        _video_service(videoService): A video service object"""
        self._is_game_over = False
        self._video_service = VideoService()


    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        ship = cast.get_first_actor("ship")
        if not ship.get_collided_state():
            self._check_asteroids_collisions(cast)
            self._check_actors_on_screen(cast)
        
    def _check_asteroids_collisions(self, cast):
        """Check if one of the asteroids on screen touches the ship or the laser.
        Args:
            cast(Cast): A collection of the game's Actors"""

        ship = cast.get_first_actor("ship")
        all_asteroids = cast.get_actors("asteroid")
        lasers_shooted = cast.get_actors("laser")
        
        for asteroid in all_asteroids:
            if ship.get_position().equals(asteroid.get_position()):
                ship.change_to_collided()
                self._handle_game_over(cast)

        for asteroid in all_asteroids:
            for laser in lasers_shooted:
                if asteroid.get_position().equals(laser.get_position()):
                    laser.was_collision()
                    ship.add_points()
                    cast.remove_actor("asteroid",asteroid)
                    cast.remove_actor("laser",laser)

    def _check_actors_on_screen(self, cast):
        """ Checks the position of the asteroids and lasers on screen.
        If the laser reaches the top of the screen, it will be removed.
        If the asteroid reaches the bottom of the screen or touches the ship will be removed.
        Args:
            cast(Cast): A collection of the game's Actors"""
        
        all_asteroids = cast.get_actors("asteroid")
        lasers_shooted = cast.get_actors("laser")

        for asteroid in all_asteroids:
            if asteroid.get_position().get_y() >= constants.HEIGHT:
                asteroid.set_falling_state_false()
            if not asteroid.get_falling_state():
                cast.remove_actor("asteroid",asteroid)
        for laser in lasers_shooted:
            if laser.get_position().get_y() <= 10:
                cast.remove_actor("laser",laser)

    def _handle_game_over(self,cast):
        """Calls the draw game over method from _video_service and draw
        
        Args:
        cast (Cast): The cast of Actors in the game."""

        ship = cast.get_first_actor("ship")
        self._video_service.clear_buffer()
        self._video_service.draw_game_over(ship.get_score())
        self._video_service.flush_buffer()
