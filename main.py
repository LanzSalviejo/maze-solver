from window import Window
from cell import Cell

def main():
    win = Window(800, 600)

    c = Cell(win)
    c.has_left_wall = False
    c.draw(50, 50, 100, 100)

    c = Cell(win)
    c.has_right_wall = False
    c.draw(100, 100, 200, 200)
    
    win.wait_for_close()

if __name__ == "__main__":
    main()