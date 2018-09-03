from sudoku import *

lecture_example_assignment = '809501736207063000160000000000090407090307020706080000000000063000930502532604809'

bad_data_row1 = '809501736207063000160000000000090407090307020706080000000000063000930502532604809'
bad_data_row2 = '809501736207063020160000000000090407090307020706080000000000063000930502532604809'
bad_data_row3 = '809501736207063000160000006000090407090307020706080000000000063000930502532604809'

lecture_example_answer = '849521736257863914163749258325196487498357621716482395984275163671938542532614879'

testCase1 = CreateSudokuBoard(lecture_example_answer)

testCase2 = CreateSudokuBoard(bad_data_row1)

testCase3 = CreateSudokuBoard(bad_data_row2)

testCase4 = CreateSudokuBoard(bad_data_row3)

#print(testCase1)

#print(sorted(testCase1, key=lambda pos: pos[0]) )  # sort by age

#print(sorted(testCase1.items(), key=lambda x: x[0]))
#print('Row A')
#PrintBoard(testCase1)

if (MeetsAllContraints(testCase1)):
    print(True)
else:
    print(False)

if (MeetsAllContraints(testCase2)):
    print(True)
else:
    print(False)

if (MeetsAllContraints(testCase3)):
    print(True)
else:
    print(False)

if (MeetsAllContraints(testCase4)):
    print(True)
else:
    print(False)
