square1_keys = ['A1','B1','C1', 'A2', 'B2', 'C2', 'A3','B3','C3']
square4_keys = ['A4','B4','C4', 'A5', 'B5', 'C5', 'A6','B6','C6']
square7_keys = ['A7','B7','C7', 'A8', 'B8', 'C8', 'A9','B9','C9']
square2_keys = ['D1','E1','F1', 'D2', 'E2', 'F2', 'D3','E3','F3']
square5_keys = ['D4','E4','F4', 'D5', 'E5', 'F5', 'D6','E6','F6']
square8_keys = ['D7','E7','F7', 'D8', 'E8', 'F8', 'D9','E9','F9']
square3_keys = ['G1','H1','I1', 'G2', 'H2', 'I2', 'G3','H3','I3']
square6_keys = ['G4','H4','I4', 'G5', 'H5', 'I5', 'G6','H6','I6']
square9_keys = ['G7','H7','I7', 'G8', 'H8', 'I8', 'G9','H9','I9']


def CreateSudokuBoard(input_list):
    sudoku_board = {}
    prefix = 'ABCDEFGHI'
    prefix_index = 0
    input_index = 0
    for x in range(1,10):
        for x in range(1,10):
            key = prefix[prefix_index] + str(x)
            sudoku_board[key] = input_list[input_index]
            input_index += 1
        prefix_index += 1
    return sudoku_board

def FindEmptySquares(board):
    return list(board.keys())[list(board.values()).index('0')]

def SquareValues(board, key_list):
    value_list = []
    for key in key_list:
        value_list.append(board[key])
    return value_list


def ReturnSquare(board, key):
    if key in square1_keys:
        return SquareValues(board, square1_keys)
    elif key in square2_keys:
        return SquareValues(board, square2_keys)
    elif key in square3_keys:
        return SquareValues(board, square3_keys)
    elif key in square4_keys:
        return SquareValues(board, square4_keys)
    elif key in square5_keys:
        return SquareValues(board, square5_keys)
    elif key in square6_keys:
        return SquareValues(board, square6_keys)
    elif key in square7_keys:
        return SquareValues(board, square7_keys)
    elif key in square8_keys:
        return SquareValues(board, square8_keys)
    elif key in square9_keys:
        return SquareValues(board, square9_keys)

input1 = '160523849'
input2 = '984176523325489671'

withZerosinput = '160523849984176523325489671798315264642798135531642798476831952213957486859264317'

testSquares = '111523849222176523333489671444315264555798135666642798777831952888957486999264317'

# '160523849 984176523 325489671 798315264 642798135 531642798476831952213957486 859264317'



board2 = CreateSudokuBoard(testSquares)

print(ReturnSquare(board2, "G3"))

#row_list = ReturnRow(board2, empty_square.index(0))

#empty = FindEmptySquares(board2)




#rowd = {k: v for k, v in board2.items() if k.startswith('D')}



#for key,val in sorted(board2.items()):
  # print(key, "=>", val)

#print(FindEmptySquares(board2))










