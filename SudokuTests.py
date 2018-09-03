import unittest
from sudoku import *



withZerosinput = '160523849984176523325489671798315264642798135531642798476831952213957486859264317'

#160523849 984176523 325489671 798315264 642798135 531642798 476831952 213957486 859264317

class SudokuBoardTest(unittest.TestCase):

    def setUp(self):
        self.board = CreateSudokuBoard(withZerosinput)

    def test_FindEmptySquares(self):
        self.assertEqual('A3',FindEmptySquares(self.board))

   # def test_MeetConstraints_row1Bad(self):

class SudokuBoardTestConstraints(unittest.TestCase):

    def setUp(self):
        self.board = CreateSudokuBoard(withZerosinput)

    def test_Row1Fails(self):
        self.board = CreateSudokuBoard(withZerosinput)
        self.assertEqual('A3', FindEmptySquares(self.board))


# def test_MeetConstraints_row1Bad(self):

if __name__ == '__main__':
    unittest.main()