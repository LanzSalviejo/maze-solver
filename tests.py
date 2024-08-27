import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)
    
    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)
        
    def test_maze_create_cells_coord(self):
        x = 100
        y = 200
        m1 = Maze(100, 200, 10, 10, 10, 10, None)
        self.assertEqual(m1._x1, 100)
        self.assertEqual(m1._y1, 200)

if __name__ == "__main__":
    unittest.main()