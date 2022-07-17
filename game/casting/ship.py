from game.casting.actor import Actor
from game.casting.laser import Laser
from game.shared.point import Point
import constants


class Ship(Actor):
    """The player, a ship actor.
    The responsibility of the ship is to move itself to the right or to the left avoiding the asteroids or destroying them, and record the information about its position.
     Attributes:
        self._collided (boolean): It is false until it strikes an asteroid.
        self._score (int): It stores the player's score depending on how many asteroids it strikes.
    """
    def __init__(self):
        super().__init__()
        self._collided = False
        self._score = 0
        
    
    def move_next(self):
        """Moves the ship to the left of right to avoid the asteroids or to shoot them.
        Adds the velocity to its current position if it doesn't exceeds the width of the screen.
        """
        position = self.get_position()
        velocity = self.get_velocity()
        
        x = position.get_x()
        y = position.get_y()

        if x < constants.WIDTH and x >= 0:
            x += velocity.get_x()
       
        position_updated = Point(x,y)
        self.set_position(position_updated)

    def add_points(self):
        """Add 100 points for every asteroids succesfully shooted.
        """
        self._score += 10
    
    def get_score(self):
        """It returns the current score of the player."""
        return self._score

    def get_collided_state(self):
        """Returns the collided state (True or False)"""
        return self._collided

    def change_to_collided(self):
        """Chenges its state to collided"""
        self._collided = True