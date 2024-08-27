from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width) # our default convas
        self.__canvas.pack() # packs canvas making it ready to be drawn
        self.__is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close) # for when closing window

    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self._is_running = True
        while self._is_running:
            self.redraw()
    
    def close(self):
        self._is_running = False