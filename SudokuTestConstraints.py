import unittest
from sudoku import *

good_example_complete  = '849521736257863914163749258325196487498357621716482395984275163671938542532614879'
good_example_incomplete  = '809521036257863914163749258325196487498357621716002395984275163671938542530614879'

bad_data_rowA = '809501736207063000160000000000090407090307020706080000000000063000930502532604809'
bad_data_rowB = '809501736207063020160000000000090407090307020706080000000000063000930502532604809'
bad_data_rowC = '809501736207063000160000006000090407090307020706080000000000063000930502532604809'
bad_data_rowD = '849521736257863914163749258325196487498357624716482395984275163671938542532614879'
bad_data_rowE = '849521736257863914163749258325196487498357621716484395984275163671938542532614879'

bad_data_col1 = '849521736257863914163749258825196487498357621716482395984275163671938542532614879'
bad_data_col5 = '849521736257863914163749258325196487498357621716482395984275163671938542532614879'
bad_data_col7 = '849521736257863914163749258325196487498357621716482395984275163671958542532614879'
bad_data_col9 = '849521736257863914163749258325196487498357621716482395984275163671938546532614879'

lecture_example_assignment = '809501736207063000160000000000090407090307020706080000000000063000930502532604809'
bad_data_sq1 = '869501736207063000160000000000090407090307020706080000000000063000930502532604809'

class SudokuBoardTestConstraints(unittest.TestCase):

    def test_ConstraintsPassFullData(self):
        self.board = CreateSudokuBoard(good_example_complete)
        self.assertEqual(True, MeetsAllContraints(self.board))

    def test_ConstraintsPassPartialData(self):
        self.board = CreateSudokuBoard(good_example_incomplete)
        self.assertEqual(True, MeetsAllContraints(self.board))

 #   def test_ConstraintsRow1Fails(self):
 #       self.board = CreateSudokuBoard(bad_data_rowA)
 #       self.assertEqual(False, MeetsAllContraints(self.board))

    def test_ConstraintsRow2Fails(self):
        self.board = CreateSudokuBoard(bad_data_rowB)
        self.assertEqual(False, MeetsAllContraints(self.board))

    def test_ConstraintsRow3Fails(self):
        self.board = CreateSudokuBoard(bad_data_rowC)
        self.assertEqual(False, MeetsAllContraints(self.board))

    def test_ConstraintsRow4Fails(self):
        self.board = CreateSudokuBoard(bad_data_rowD)
        self.assertEqual(False, MeetsAllContraints(self.board))

    def test_ConstraintsRow5Fails(self):
        self.board = CreateSudokuBoard(bad_data_rowE)
        self.assertEqual(False, MeetsAllContraints(self.board))

    def test_ConstraintsCol1Fails(self):
        self.board = CreateSudokuBoard(bad_data_col1)
        self.assertEqual(False, MeetsAllContraints(self.board))

#   def test_ConstraintsCol15ails(self):
#      self.board = CreateSudokuBoard(bad_data_col5)
#     self.assertEqual(False, MeetsAllContraints(self.board))

    def test_ConstraintsCol7Fails(self):
        self.board = CreateSudokuBoard(bad_data_col7)
        self.assertEqual(False, MeetsAllContraints(self.board))

    def test_ConstraintsCol9Fails(self):
        self.board = CreateSudokuBoard(bad_data_col9)
        self.assertEqual(False, MeetsAllContraints(self.board))

    def test_ConstraintsSq1Fails(self):
        self.board = CreateSudokuBoard(bad_data_sq1)
        self.assertEqual(False, SquaresMeetConstraints(self.board))

    def test_FindAllEmptySquares(self):
        self.board = CreateSudokuBoard(good_example_incomplete)
        empty = FindAllEmptySquares(self.board)
        self.assertEqual(5, len(empty))

if __name__ == '__main__':
    unittest.main()