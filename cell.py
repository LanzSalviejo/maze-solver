from graphics import *

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None
        self.win = win
    
    def draw(self, x1, y1, x2, y2):
        if self.win is None:
            return
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x2, y2))
            self.win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x1, y1), Point(x2, y2))
            self.win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y1), Point(x2, y2))
            self.win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y2))
            self.win.draw_line(line)
        
    def draw_move(self, to_cell, undo=False):
        half_length = abs(self.x1 + self.x2) // 2
        x_center = half_length + self.x1
        y_center = half_length + self.y1
        
        half_length2 = abs(to_cell.x1 + to_cell.x2) // 2
        x_center2 = half_length2 + self.x2
        y_center2 = half_length2 + self.y2
        
        fill_color = "red"
        if undo:
            fill_color = "gray"
        
        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self.win.draw_line(line, fill_color)