"""
This module represents the apple that appears at random places on the screen.
"""
import random
from typing import List

from gui import Gui
from position import Position



def collides(p, positions):
    """Return true if p is any of the positions in the list."""
    for position in positions:
        if p.get_x() == position.get_x() and p.get_y() == position.get_y():
            return True
    return False


class Apple:

    def __init__(self, width, height,snake):
        self.width = width
        self.height = height
        self.position = Position(random.randint(2,width- 2),random.randint(2,height- 2))
        while collides(self.position,snake):
            self.position = Position(random.randint(2,width- 2),random.randint(2,height- 2))

    def draw(self, gui):
        gui.draw_text("*",self.position.get_x(), self.position.get_y() ,"GREEN","RED")

    def check_collides(self,snake):
        if collides(self.position, snake[0:1]):
            self.position = Position(random.randint(2,self.width- 2),random.randint(2,self.height- 2))
            while collides(self.position,snake):
                self.position = Position(random.randint(2,self.width- 2),random.randint(2,self.height- 2))
            return True
        return False
    
    def get_apple(self):
        return self.position
        