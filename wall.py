
from gui import Gui
from position import Position
from apple import collides
import random

class Wall:

    def __init__(self, width, height, snake, apples):
        self.width = width
        self.height = height
        self.position = Position(random.randint(2,width - 2),random.randint(2,height - 2))
        while collides(self.position,snake):
            self.position = Position(random.randint(2,width - 2),random.randint(2,height - 2))
        while collides(self.position, apples):
            self.position = Position(random.randint(2,width - 2),random.randint(2,height - 2))

    def draw(self, gui):
        gui.draw_text("#",self.position.get_x(), self.position.get_y() ,"WHITE", "BLUE")

    def get_wall(self):
        return self.position