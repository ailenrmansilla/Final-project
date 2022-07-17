import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Asteroid(Actor):
    """An asteroid actor.
    The responsibility of the asteroid is to move itself from the top to the bottom and record the information about its position.
        Attributes:
            self._falling (boolean): it keeps the state of the actor. It will change to False when touches the bottom of the screen or the ship.
    """
    def __init__(self):
        super().__init__()
        self._falling = True
        
    def move_next(self):
        """The asteroid falls from the top of the screen to the bottom in a vertical line. It will dissapear when touches the bottom of the line"""
        dx = self._position.get_x() + self._velocity.get_x()
        dy = self._position.get_y() + self._velocity.get_y()
        if dy < constants.HEIGHT:
            self._position = Point(dx, dy)
        elif dy >= constants.HEIGHT:
            self._falling = False # we will remove it when it gets to the bottom of the screen

    def get_falling_state(self):
        """Returns the state of the asteroid.
        """
        return self._falling

    def set_falling_state_false(self):
        """Changes the falling state of the asteroid to false."""
        self._falling = False