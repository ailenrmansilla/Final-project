from game.casting.laser import Laser
from game.shared.point import Point

class GenerateLaser():
    """An asteroid object that participates in the game moving form the top of the screen to the bottom.
    If it touches the ship, the game is over.
    
    Attributes:
        _laser_sprite (string): contains the file path for the laser sprite
        """

    def __init__(self):
        """Initializes the GenerateLaser class and its attributes.
        """

        

    def create_laser(self, position):
        """Creates a laser in the current position of the ship and we set a fixed velocity
        
        Args:
            position(Point): The (x,y) position of the ship"""
        laser = Laser()
        x = position.get_x() + 47
        y = position.get_y()
        laser.set_position(Point(x,y)) # we send the current position of the ship
        laser.set_velocity(Point(0,12))
        laser.set_src("Final-project/asteroids/game/images/laser_red.png")
        return laser