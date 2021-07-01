# lets solve a sudoku with recursion =)

# recursive method to find the next empty field and try numbers
def fill_field(sudoku: list, row: int, column: int) -> bool:
    for values_to_try in range(1, 10):
        if column == 8 and sudoku[row][column] != 0 or column == 9:
            row += 1
            column = 0
        elif sudoku[row][column] == 0:
            if valid_number(sudoku, values_to_try, row, column):
                sudoku[row][column] = values_to_try
                if fill_field(sudoku, row, column+1):
                    print(2)
                else:
                    sudoku[row][column] = 0
        else:
            column += 1
        if column == row == 8:
            return True
    return False


# tests if number fits in row column and box
def valid_number(sudoku: list, number: int, row: int, column: int) -> bool:
    # add your code here
    # check for value in row
    for value in range(9):
        if sudoku[row][value] == number:
            return False
    # check for value in lists
    for lists in range(9):
        if sudoku[lists][column] == number:
            return False
    # check for value in block
    for lists in range(3):
        for values in range(3):
            if sudoku[((row // 3) * 3) + lists][((column // 3) * 3) + values] == number:
                return False
    return True


# prints the sudoku field properly
def print_sudoku(field: list) -> None:
    # add your code here
    for lists in range(9):
        print(*field[lists])


# create a 2d sudoku field
sudoku_field = [[0, 8, 0, 0, 0, 0, 1, 0, 4], [1, 0, 0, 2, 0, 0, 8, 5, 0], [0, 0, 0, 0, 4, 8, 0, 9, 0],
                [0, 0, 7, 0, 3, 0, 0, 0, 5], [0, 3, 0, 0, 9, 0, 0, 8, 0], [9, 0, 0, 0, 2, 0, 7, 0, 0],
                [0, 2, 0, 3, 7, 0, 0, 0, 0], [0, 7, 5, 0, 0, 6, 0, 0, 9], [3, 0, 1, 0, 0, 0, 0, 7, 0]]

'''
print("Please enter the rows of the sudoku line by line (space separated, 0 = emtpy):")
for row_number in range(1, 10):
    entered_row = [int(x) for x in input("Row " + str(row_number) + ": ").split()]
    while len(entered_row) != 9:
        entered_row = [int(x) for x in input("Row " + str(row_number) + ": ").split()]
    sudoku_field[row_number - 1] = entered_row
'''
# print field
print_sudoku(sudoku_field)

# solve sudoku by starting in the upper left corner
if fill_field(sudoku_field, 0, 0):
    print()
    print("Solution: ")
    print_sudoku(sudoku_field)
else:
    print("This sudoku is not solvable")
