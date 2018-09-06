
# TODO - Next add tests for constraints on columns, then boxes.
# TODO - Need function to get all values from squares into a list


#input = '167523849984176523325489671798315264642798135531642798476831952213957486859264317'

#withZerosinput = '160523849984176523325489671098315264642798135531642790476831952213957486859204317'

#bad_input = '166523849984176523325489671798315264642798135531642798476831952213957486859264317'

square1_keys = ['A1','B1','C1', 'A2', 'B2', 'C2', 'A3','B3','C3']
square4_keys = ['A4','B4','C4', 'A5', 'B5', 'C5', 'A6','B6','C6']
square7_keys = ['A7','B7','C7', 'A8', 'B8', 'C8', 'A9','B9','C9']
square2_keys = ['D1','E1','F1', 'D2', 'E2', 'F2', 'D3','E3','F3']
square5_keys = ['D4','E4','F4', 'D5', 'E5', 'F5', 'D6','E6','F6']
square8_keys = ['D7','E7','F7', 'D8', 'E8', 'F8', 'D9','E9','F9']
square3_keys = ['G1','H1','I1', 'G2', 'H2', 'I2', 'G3','H3','I3']
square6_keys = ['G4','H4','I4', 'G5', 'H5', 'I5', 'G6','H6','I6']
square9_keys = ['G7','H7','I7', 'G8', 'H8', 'I8', 'G9','H9','I9']

def CreateSudokuBoard(assignments):
    sudoku_board = {}
    prefix = 'ABCDEFGHI'
    prefix_index = 0
    input_index = 0
    for x in range(1,10):
        for x in range(1,10):
            key = prefix[prefix_index] + str(x)
            sudoku_board[key] = assignments[input_index]
            input_index += 1
        prefix_index += 1
    return sudoku_board


def Alldiff(in_list):
    unique = set(in_list)
    for each in unique:
        count = in_list.count(each)
        if count > 1 and each != '0':
          return False
    return True

def MeetsAllContraints(sudoku_board):
    #check that all rows and all columns are different
    rows = 'ABCDEFGHI'
    for x in range (0,8):
        rowy = ReturnRow(sudoku_board, rows[x])
        if Alldiff(rowy) == False:
            return False
    # now check all columns
    for z in range (1,9):
        col1 = ReturnColumn(sudoku_board, str(z))
        if Alldiff(col1) == False:
            return False
    return SquaresMeetConstraints(sudoku_board)


def SquaresMeetConstraints(sudoku_board):
   values_square1 = ReturnSquare(sudoku_board, square1_keys)
   if Alldiff(values_square1) == False:
       return False
   values_square2 = ReturnSquare(sudoku_board, square2_keys)
   if Alldiff(values_square2) == False:
       return False
   values_square3 = ReturnSquare(sudoku_board, square3_keys)
   if Alldiff(values_square3) == False:
       return False
   values_square4 = ReturnSquare(sudoku_board, square4_keys)
   if Alldiff(values_square4) == False:
       return False
   values_square5 = ReturnSquare(sudoku_board, square5_keys)
   if Alldiff(values_square5) == False:
       return False
   values_square6 = ReturnSquare(sudoku_board, square6_keys)
   if Alldiff(values_square6) == False:
       return False
   values_square7 = ReturnSquare(sudoku_board, square7_keys)
   if Alldiff(values_square7) == False:
       return False
   values_square8 = ReturnSquare(sudoku_board, square8_keys)
   if Alldiff(values_square8) == False:
       return False
   values_square9 = ReturnSquare(sudoku_board, square9_keys)
   if Alldiff(values_square9) == False:
       return False
   return True

#def PrintBoard(sudoku_board):
 #   for key in sorted(sudoku_board.iteritems(), key=lambda (k,v): (v,k)):
#        print ("%s %s" % (key, sudoku_board[key]))



def AllSquaresCompleted(sudoku_board):
    if ('0' in sudoku_board.values()):
        return False
    return True

def isComplete(sudoku_board):
   # if (MeetsAllContraints(sudoku_board) == False):
    #    return False
    if (AllSquaresCompleted(sudoku_board) == False):
        return False
    return True

def FindEmptySquares(board):
    return list(board.keys())[list(board.values()).index('0')]

def ReturnRow(board, char):
    row = {k: v for k, v in board.items() if k.startswith(char)}
    return list(row.values())

def ReturnColumn(board, num):
    col = {k: v for k, v in board.items() if k.endswith(num)}
    return list(col.values())

def ReturnSquare(board, square_keys):
    square = {k: v for k, v in board.items() if k in square_keys}
    return list(square.values())

def Backtrack(sudoku_board):
    domain_values = ['1','2','3','4','5','6','7','8','9']
    # find a zero to fill in
    if (isComplete(sudoku_board)):
        return sudoku_board
    else:
        empty_square = FindEmptySquares(sudoku_board)
        row_list = ReturnRow(sudoku_board, empty_square[0])
        col_list = ReturnColumn(sudoku_board, empty_square[1])
        print(row_list)
        found_number = 0
        for number in domain_values:
            if number not in row_list and number not in col_list:
                found_number = number
                break;
        if found_number != 0:
            sudoku_board[empty_square] = found_number
        Backtrack(sudoku_board)

#sudoku_board = CreateSudokuBoard(withZerosinput)
#finished_board = Backtrack(sudoku_board)

#if (finished_board.__len__()==0):
#    print("failure")
#else:
#for key,val in sorted(sudoku_board.items()):
#    print(key, "=>", val)




