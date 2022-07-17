from game.shared.point import Point
import constants


class Actor:
    """A visible, moveable thing that participates in the game. 
    
    The responsibility of Actor is to keep track of its sprite, position and velocity in 2d 
    space.

    Attributes:
        _position (Point): The screen coordinates.
        _velocity (Point): The speed and direction.
        _src (string): The path to the actor's image
        started(boolean): Control if the actor was created
    """

    def __init__(self):
        """Constructs a new Actor."""
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)
        self._src = ""
        self.started = True

    def get_position(self):
        """Gets the actor's position in 2d space.
        
        Returns:
            Point: The actor's position in 2d space.
        """
        return self._position
    
    def set_src(self,src):
        """Sets the actor's image's file path
        
        Args:
            src(string): the file source"""
        self._src = src

    def get_src(self):
        """Gets the actor's image's file path
        
        Returns:
            src(string): the file source"""
        return self._src 

    def get_velocity(self):
        """Gets the actor's speed and direction.
        
        Returns:
            Point: The actor's speed and direction.
        """
        return self._velocity

    def move_next(self):
        """Moves the actor to its next position according to its velocity. It can not move more than maximum x and y values.
        
        """
        x = self._position.get_x()
        y = self._position.get_y()
        if x < constants.WIDTH and x > 0:
            x = (self._position.get_x() + self._velocity.get_x()) % constants.WIDTH
        if y < constants.HEIGHT and y > 0:
            y = (self._position.get_y() + self._velocity.get_y()) % constants.HEIGHT
        self._position = Point(x, y)


    def set_position(self, position):
        """Updates the position to the given one.
        
        Args:
            position (Point): The given position.
        """
        self._position = position


    def set_velocity(self, velocity):
        """Updates the velocity to the given one.
        
        Args:
            velocity (Point): The given velocity.
        """
        self._velocity = velocity