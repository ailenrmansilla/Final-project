import constants, random
from game.shared.point import Point
from game.casting.cast import Cast
from game.casting.asteroid import Asteroid

class GenerateAsteroids():
    """An asteroid object that participates in the game moving form the top of the screen to the bottom.
    If it touches the ship, the game is over.
    
    Attributes:
        _asteroids_sprites (Array): contains the file for the asteroids sprites"""

    def __init__(self):
        """Initializes the GenerateAsteroids class creating an array with the sprites sources.
        """
        self._asteroids_sprites = ["game\images\game-asteroid1.png","game\images\game-asteroid2.png","game\images\game-asteroid3.png","game\images\game-asteroid4.png","game\images\game-asteroid5.png","game\images\game-asteroid6.png"]

    def create_asteroid(self):
        """Creates an asteroid on the top of the screen and set a random decreasing velocity"""
        asteroid = Asteroid()
        x = (random.randint(0,constants.WIDTH))
        y = 10
        position = Point(x,y)
        vx = random.randint(-7,7)
        vy = random.randint(5,15)
        velocity = Point(vx, vy)
        asteroid.set_position(position) # we set it somehwere on the top of the screen
        asteroid.set_velocity(velocity)  # it will move horizontally and from top to bottom
        asteroid.set_src(self._asteroids_sprites[random.randint(0,5)])  #we choose randomly the sprite of the asteroid
        return asteroid

    