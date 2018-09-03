import unittest
from sudoku import *

good_example = '849521736257863914163749258325196487498357621716482395984275163671938542532614879'
bad_data_rowA = '809501736207063000160000000000090407090307020706080000000000063000930502532604809'
bad_data_rowB = '809501736207063020160000000000090407090307020706080000000000063000930502532604809'
bad_data_rowC = '809501736207063000160000006000090407090307020706080000000000063000930502532604809'
bad_data_rowD = '849521736257863914163749258325196487498357624716482395984275163671938542532614879'
bad_data_rowE = '849521736257863914163749258325196487498357621716484395984275163671938542532614879'

class SudokuBoardTestConstraints(unittest.TestCase):

    def test_ConstraintsPass(self):
        self.board = CreateSudokuBoard(good_example)
        self.assertEqual(True, MeetsAllContraints(self.board))

    def test_ConstraintsRow1Fails(self):
        self.board = CreateSudokuBoard(bad_data_rowA)
        self.assertEqual(False, MeetsAllContraints(self.board))

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

if __name__ == '__main__':
    unittest.main()