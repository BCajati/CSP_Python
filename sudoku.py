
# improved method to pick empty square
# doesn't seem like back track recursion is working - must be missing something



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
#    for key in sorted(sudoku_board.iteritems(), key=lambda (k,v): (v,k)):
#        print ("%s %s" % (key, sudoku_board[key]))

def PrintBoard(sudoku_board):
   print("A:" + sudoku_board["A1"] + sudoku_board["A2"] + sudoku_board["A3"] + sudoku_board["A4"]+ sudoku_board["A5"]+sudoku_board["A6"]+sudoku_board["A7"]+sudoku_board["A8"]+sudoku_board["A9"])
   print("B:" + sudoku_board["B1"] + sudoku_board["B2"] + sudoku_board["B3"] + sudoku_board["B4"]+ sudoku_board["B5"]+sudoku_board["B6"]+sudoku_board["B7"]+sudoku_board["B8"]+sudoku_board["B9"])
   print("C:" + sudoku_board["C1"] + sudoku_board["C2"] + sudoku_board["C3"] + sudoku_board["C4"]+ sudoku_board["C5"]+sudoku_board["C6"]+sudoku_board["C7"]+sudoku_board["C8"]+sudoku_board["C9"])
   print("D:" + sudoku_board["D1"] + sudoku_board["D2"] + sudoku_board["D3"] + sudoku_board["D4"]+ sudoku_board["D5"]+sudoku_board["D6"]+sudoku_board["D7"]+sudoku_board["D8"]+sudoku_board["D9"])
   print("E:" + sudoku_board["E1"] + sudoku_board["E2"] + sudoku_board["E3"] + sudoku_board["E4"]+ sudoku_board["E5"]+sudoku_board["E6"]+sudoku_board["E7"]+sudoku_board["E8"]+sudoku_board["E9"])
   print("F:" + sudoku_board["F1"] + sudoku_board["F2"] + sudoku_board["F3"] + sudoku_board["F4"]+ sudoku_board["F5"]+sudoku_board["F6"]+sudoku_board["F7"]+sudoku_board["F8"]+sudoku_board["F9"])
   print("G:" + sudoku_board["G1"] + sudoku_board["G2"] + sudoku_board["G3"] + sudoku_board["G4"]+ sudoku_board["G5"]+sudoku_board["G6"]+sudoku_board["G7"]+sudoku_board["G8"]+sudoku_board["G9"])
   print("H:" + sudoku_board["H1"] + sudoku_board["H2"] + sudoku_board["H3"] + sudoku_board["H4"]+ sudoku_board["H5"]+sudoku_board["H6"]+sudoku_board["H7"]+sudoku_board["H8"]+sudoku_board["H9"])
   print("I:" + sudoku_board["I1"] + sudoku_board["I2"] + sudoku_board["I3"] + sudoku_board["I4"]+ sudoku_board["I5"]+sudoku_board["I6"]+sudoku_board["I7"]+sudoku_board["I8"]+sudoku_board["I9"])
   print("---------------------")

def AllSquaresCompleted(sudoku_board):
    #print("check Complete: ")
    if ('0' in sudoku_board.values()):
        #print("false")
        return False
    #print("true")
    return True

def FindEmptySquares(board):
    return list(board.keys())[list(board.values()).index('0')]

def FindLeastEmptySquares(sudoku_board):
    if AllSquaresCompleted(sudoku_board):
        return None
    rows = 'ABCDEFGHI'
    #least_zeros_row = 'A'
    #least_zeros_col = 1
    min_squares = []
    least_zeros = 9
    for x in range(0, 8):
        rowy = ReturnRow(sudoku_board, rows[x])
        count = rowy.count('0')
        if count > 0 and count < least_zeros:
            min_squares = ReturnEmptyRowKeys(sudoku_board, rows[x])
            least_zeros = count
           # if count < 3:
               # return min_squares
    # now check all columns
    for z in range(1, 9):
        col1 = ReturnColumn(sudoku_board, str(z))
        count = col1.count('0')
        if count > 0 and count < least_zeros:
            min_squares = ReturnEmptyColumnKeys(sudoku_board, str(z))
            least_zeros = count
    return min_squares

def FindAllEmptySquares(board):
    squares = {k: v for k, v in board.items() if v.startswith('0')}
    return list(squares.keys())

def ReturnRow(board, char):
    row = {k: v for k, v in board.items() if k.startswith(char)}
    return list(row.values())

def ReturnEmptyRowKeys(board, char):
    row = {k: v for k, v in board.items() if k.startswith(char) and v.startswith('0')}
    return list(row.keys())

def ReturnColumn(board, num):
    col = {k: v for k, v in board.items() if k.endswith(num)}
    return list(col.values())

def ReturnEmptyColumnKeys(board, num):
    col = {k: v for k, v in board.items() if k.endswith(num) and v.startswith('0')}
    return list(col.keys())

def ReturnSquare(board, square_keys):
    square = {k: v for k, v in board.items() if k in square_keys}
    return list(square.values())

def SelectUnassignedVariables(sudoku_board):
    return "tbd"

def Backtrack_Search(sudoku_board):
    return Backtrack(sudoku_board)

def Backtrack(sudoku_board):
    domain_values = ['1','2','3','4','5','6','7','8','9']
    PrintBoard(sudoku_board)
    # find a zero to fill in
    if (AllSquaresCompleted(sudoku_board)):
        return sudoku_board

    empty_squares = FindLeastEmptySquares(sudoku_board)
    for square in empty_squares:
        for number in domain_values:
            sudoku_board[square] = number
            if (MeetsAllContraints(sudoku_board)):
                print("Add " + square + ":" +  number)
                result = Backtrack(sudoku_board)
                if result != "failure":
                    return result
                sudoku_board[square] = 0
    return "failure"

#sudoku_board = CreateSudokuBoard(withZerosinput)
#finished_board = Backtrack(sudoku_board)

#if (finished_board.__len__()==0):
#    print("failure")
#else:
#for key,val in sorted(sudoku_board.items()):
#    print(key, "=>", val)




