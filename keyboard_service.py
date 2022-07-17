import pyray
from game.shared.point import Point


class KeyboardService:
    """Detects player input. 
    
    The responsibility of a KeyboardService is to indicate whether or not a key is up or down.

     Attributes:
        _keys (Dict[string, int]): The letter to key mapping.
    """

    def __init__(self):
        """Constructs a new KeyboardService."""
        self._keys = {}
        
        self._keys['left'] = pyray.KEY_LEFT
        self._keys['right'] = pyray.KEY_RIGHT
        self._keys['space'] = pyray.KEY_SPACE
       
    def get_direction(self):
        """Gets the selected direction based on the currently pressed keys.
         """
        dx = 0
        if pyray.is_key_down(pyray.KEY_LEFT):
            dx = -10
        
        if pyray.is_key_down(pyray.KEY_RIGHT):
            dx = 10

        new_direction = Point(dx, 0)
        return new_direction

    def is_laser_shooting(self):
        """Check if the player press the space key and returns True if so.
        """
        if pyray.is_key_down(pyray.KEY_SPACE):
            return True
        else:
            return False


    def is_key_up(self, key):
        """Checks if the given key is currently up.
        
        Args:
            key (string): The given key (left, right)
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_up(pyray_key)

    def is_key_down(self, key):
        """Checks if the given key is currently down.
        
        Args:
            key (string): The given key (left, right)
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_down(pyray_key)