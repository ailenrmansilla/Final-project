from game.casting.actor import Actor
from game.shared.point import Point


class Laser(Actor):
    """The laser shooted by the ship.
    The responsibility of the laser is to move itself from the ship's position to the top of the screen.
    if it collides with an asteroid, the ship earns 10 points.

    Attributes:
        self._collided (boolean): It is false until it strikes an asteroid.
    """
    def __init__(self):
        super().__init__()
        self._collided = False
    
    def move_next(self):
        dx = self._position.get_x()
        dy = self._position.get_y()
        if dy > 0:
            dy -= 4
        self._position = Point(dx, dy)

    def get_collided(self):
        """Returns the colission state of the laser, False if it didn't touch an asteroid, True if it did.
        
        Returns:
            self._collided(boolean)"""

        return self._collided

    def was_collision(self):
        """Changes the state of _collided to True if the laser shooted the asteroid or if it tocuhes the top of the screen.
        """

        self._collided = True