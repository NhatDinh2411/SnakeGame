class Explosion:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self, gui):
        gui.draw_text('*', self.x, self.y, 'RED', 'BLACK')