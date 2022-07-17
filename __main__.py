import constants
from game.casting.cast import Cast
from game.casting.ship import Ship
from game.directing.director import Director
from game.scripting.script import Script
from game.scripting.move_actor import MoveActorsAction
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.handle_collisions import HandleCollisionsAction
from game.scripting.draw_actor import DrawActorsAction
from game.scripting.move_actor import MoveActorsAction
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.point import Point

def main():
    """Creates the necessary classes and stores the actors in the Cast object. 
    Calls the Director to start the game."""
    cast = Cast()
    ship = Ship()
    x = constants.WIDTH//2
    y = constants.HEIGHT - 150
    ship.set_position(Point(x,y))
    ship.set_velocity(Point(0,0))
    ship.set_src("Final-project/asteroids/game/images/player_ship.png")
    cast.add_actor("ship", ship) 
    keyboard_service = KeyboardService()  #check if the cell size is necessary
    video_service = VideoService()

    script = Script() 
    # add each action to script
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))

    director = Director(video_service)
    director.start_game(cast, script)

if __name__ == "__main__":
    main()