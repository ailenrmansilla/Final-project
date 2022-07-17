from game.scripting.action import Action
from game.scripting.generate_laser import GenerateLaser
from game.scripting.generate_asteroids import GenerateAsteroids
from game.shared.point import Point
import random


class ControlActorsAction(Action):
    """
    An input action that controls the ship.
    
    The responsibility of ControlActorsAction is to get the direction and move the ship to the right or to the left

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(0, 0)

    def execute(self, cast, script):
        """Executes the control actors action.
        Moves the ship, shoots lasers and create asteroids randomly.
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        ship = cast.get_first_actor("ship")
        self._direction = self._keyboard_service.get_direction()
        ship.set_velocity(self._direction)
        
        if self._keyboard_service.is_key_down('space'):
            laser_generator = GenerateLaser() 
            # we send the current position of the ship to create a laser shooting from that point
            laser = laser_generator.create_laser(ship.get_position())
            cast.add_actor("laser",laser)

        if random.randint(0,10) == 1:
            # We check in each iteration of this execute method if a random number is 1 and just then we create another asteroid
            asteroids_generator = GenerateAsteroids()
            asteroid = asteroids_generator.create_asteroid()
            cast.add_actor("asteroid",asteroid)

       