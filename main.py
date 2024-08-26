from graphics import *

def main():
    win = Window(800, 600)
    l = Line(Point(100,300), Point(200, 400))
    win.draw_line(l, "black")
    win.wait_for_close()

if __name__ == "__main__":
    main()