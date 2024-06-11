"""
This is the main program for the snake game.
"""

import time

from gui import Gui
from room import Room
from snake import Snake
from apple import Apple
from explosion import Explosion
from wall import Wall
from apple import collides


def main():
    try:
        # Create the new Gui and start it. This clears the screen
        # and the Gui now controls the screen
        gui = Gui()
        user_score = 0
        sleep_time = 0.1
        # Create the room, the snake and the apple.
        # You will need to change the constructors later to pass more
        # information to the Snake and Apple constructors
        room = Room(gui.get_width(), gui.get_height(), "#", "WHITE", "BLUE")
        snake = Snake(gui.get_width(),gui.get_height(), "GREEN", "BLUE")
        apples = [Apple(gui.get_width(),gui.get_height(),snake.get_snake())]
        extra_walls = []
        # The main loop of the game. Use "break" to break out of the loop
        continuePlaying = True
        while continuePlaying:
            # Get a key press from the user
            c = gui.get_keypress()
            # Do something with the key press
            if c == 'q':
                break
            elif c == "KEY_UP":
                snake.change_direction("UP")
            elif c == "KEY_DOWN":
                snake.change_direction("DOWN")
            elif c == "KEY_RIGHT":
                snake.change_direction("RIGHT")
            elif c == "KEY_LEFT":
                snake.change_direction("LEFT")

            #     do something else

            # Add your code to move the snake
            # around the screen here.
            snake.move()
            
           

            # The redraw part of the game. First clear the screen
            gui.clear()
            gui.draw_text(f"Score: {user_score}", 0, 0, "RED", "BLACK")
            # Redraw everything on the screen into an offscreen buffer,
            # including the room, the Snake and the apple
            room.draw(gui)
            for apple in apples:
                apple.draw(gui)
            apple.draw(gui)
            snake.draw(gui)
            for wall in extra_walls:
                wall.draw(gui)

            for apple in apples:
                if apple.check_collides(snake.get_snake()):
                    user_score += 10
                    snake.grow()
                    sleep_time = max(sleep_time - 0.005, 0.005)
                    if user_score % 50 == 0:
                        apples.append(Apple(gui.get_width(), gui.get_height(), snake.get_snake()))
                        new_wall = Wall(gui.get_width(), gui.get_height(), snake.get_snake(), [apple.get_apple() for apple in apples])
                        extra_walls.append(new_wall)
                        new_wall.draw(gui)


            # When done redrawing all the elements of the screen, refresh will
            # make the new graphic appear on the screen all at once
            gui.refresh()

            # Detect whether the snake ate the apple, or it hit the wall
            # or it hit its own tail here
            x = snake.get_snake()[0].get_x()
            y = snake.get_snake()[0].get_y()
            if (x >= gui.get_width() - 1 or y >= gui.get_height() - 1 or x <= 0 or y <= 1) or (collides(snake.get_snake()[0],[wall.get_wall() for wall in extra_walls])):
                explosion = Explosion(x, y)
                explosion.draw(gui)
                gui.refresh()
                time.sleep(1)
                break

            if x == snake.get_snake()[-1].get_x() and y == snake.get_snake()[-1].get_y():
                explosion = Explosion(x, y)
                explosion.draw(gui)
                gui.refresh()
                time.sleep(1)
                break
            # This call makes the program go quiescent for some time, so
            # that it doesn't run so fast. If the value in the call to
            # time.sleep is decreased, the game will speed up.
            time.sleep(sleep_time)

    except Exception as e:
        # Some error occured, so we catch it, clear the screen,
        # print the log output, and then reraise the Exception
        # This will cause the program to quit and the error will be displayed
        gui.quit()
        raise e

    # Stop the GUI, clearing the screen and restoring the screen
    # back to its original state. Print the saved log output
    gui.quit()

    # The game has ended since we broke out of the main loop
    # Display the user's score here
    print(f"Game Over! Your score: {user_score}")


if __name__ == "__main__":
    main()
