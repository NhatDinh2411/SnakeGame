"""
This module implements the snake class.
"""

from gui import Gui
from position import Position
from typing import List

class Snake:
    """This is the Snake.

    It has a list of positions. The head is at index 0.
    The tail occupies the rest of the list.
    """

    def __init__(self, width, height, fore_color, back_color):
        self.width = width
        self.height = height
        self.fore_color = fore_color
        self.back_color = back_color
        self.snake = []
        self.head = Position(width // 2, height // 2)
        self.snake.append(self.head)
        self.snake.append(Position(width // 2 - 1, height // 2))
        self.snake.append(Position(width // 2 - 2, height // 2))
        self.direction = ">"
        self.direction_deltas = {
            ">": (1, 0),
            "<": (-1, 0),
            "^": (0, -1),
            "v": (0, 1)
        }

    def draw(self, gui):
        for index, point in enumerate(self.snake):
            char = self.direction if index == 0 else "+"
            gui.draw_text(char, point.get_x(), point.get_y(), self.fore_color, self.back_color)

    def change_direction(self, c: str):
        direction_map = {
            "RIGHT": ">",
            "LEFT": "<",
            "UP": "^",
            "DOWN": "v"
        }
        if (c == "RIGHT" and self.direction != "<") or \
           (c == "LEFT" and self.direction != ">") or \
           (c == "UP" and self.direction != "v") or \
           (c == "DOWN" and self.direction != "^"):
            self.direction = direction_map.get(c, self.direction)

    def move(self):
        
        delta = self.direction_deltas[self.direction]
        new_head = Position(self.head.get_x() + delta[0], self.head.get_y() + delta[1])
        self.snake = [new_head] + self.snake[:-1]
        self.head = new_head

    def get_snake(self):
        return self.snake

    def grow(self):
        tail = self.snake[-1]
        delta = self.direction_deltas[self.direction]
        new_segment = Position(tail.get_x() + delta[0], tail.get_y() + delta[1])
        self.snake.append(new_segment)
     


