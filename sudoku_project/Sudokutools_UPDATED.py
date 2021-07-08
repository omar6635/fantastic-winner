from typing import List


# Create and display
def init_empty_grid() -> List[List[int]]:
    """
    Defines an empty list and then turns it to a two dimensional list, where each value is a zero.
    Author: Mohammad.

    :return: A two dimensional list
    """
    grid = []
    for i in range(9):
        grid_entries_list = []
        for x in range(9):
            grid_entries_list.append(0)
        grid.append(grid_entries_list)
    return grid


def init_candidates() -> List[List[str]]:
    """
    Defines an empty list and then turns it to a two dimensional list, where each value is the string
    value '123456789'. Author: Mohammad.

    :return: A two dimensional list
    """
    candidates = []
    for i in range(9):
        candidates_entries_list = []
        for x in range(9):
            candidates_entries_list.append('123456789')
        candidates.append(candidates_entries_list)
    return candidates


def print_grid(grid: List[List[int]]):
    """
    Prints a sudoku grid that uses the values in grid as sudoku numbers. Author: Mohammad.

    :param grid: Two dimensional list
    """
    for i in range(9):
        if i > 0 and i != 3 and i != 6:
            print()
        for x in range(9):
            if x >= 0 and x != 3 and x != 6 and grid[i][x] == 0:
                print(" " + " ", end="")

            if x >= 0 and x != 3 and x != 6 and grid[i][x] != 0:
                print(str(grid[i][x]) + " ", end="")

            if x == 3 and grid[i][x] == 0 or x == 6 and grid[i][x] == 0:
                print("| " + " " + " ", end="")

            if x == 3 and grid[i][x] != 0 or x == 6 and grid[i][x] != 0:
                print("| " + str(grid[i][x]) + " ", end="")

        if i == 2 or i == 5:
            print()
            print("---------------------")


def set_default_sudoku_grid(grid: List[List[int]]):
    """
    changes the values in grid. Author: Mohammad.

    :param grid: Two dimensional list
    """
    grid_replacement = [[0, 0, 1, 2, 0, 7, 0, 0, 0], [0, 6, 2, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 9, 4, 0],
                        [0, 0, 0, 9, 8, 0, 0, 0, 3], [5, 0, 0, 0, 0, 0, 0, 0, 0], [7, 0, 0, 0, 3, 0, 0, 2, 1],
                        [0, 0, 0, 1, 0, 2, 0, 0, 0], [0, 7, 0, 8, 0, 0, 4, 1, 0], [3, 0, 4, 0, 0, 0, 0, 8, 0]]
    for i in range(9):
        grid.pop(i)
        grid.insert(i, grid_replacement[i])


# verifying
def is_present_in_row(grid: List[List[int]], row_index: int, digit: int) -> bool:
    """
    Tries to find a specific digit in a specific row in grid. Author: Mohammad.

    :param grid: Two dimensional list
    :param row_index: Int value
    :param digit: Int value
    :return: Boolean value
    """
    points = 0
    for i in range(9):
        if digit == grid[row_index][i]:
            points += 1
    if points >= 1:
        return True
    else:
        return False


def is_present_in_column(grid: List[List[int]], column_index: int, digit: int) -> bool:
    """
    Tries to find a specific digit in a specific column in grid. Author: Mohammad.

    :param grid: Two dimensional list
    :param column_index: Int value
    :param digit: Int value
    :return: Boolean value
    """
    points = 0
    for i in range(9):
        if digit == grid[i][column_index]:
            points += 1
    if points >= 1:
        return True
    else:
        return False


def is_present_in_block(grid: List[List[int]], row_index: int, column_index: int, digit: int) -> bool:
    """
    Tries to find a specific digit in a specific block in grid. Author: Omar.

    :param grid: Two dimensional list
    :param row_index: Int value
    :param column_index: Int value
    :param digit: Int value
    :return: Boolean value
    """
    points = 0
    for i in range(3):
        for x in range(3):
            if digit == grid[((row_index//3) * 3) + i][((column_index//3) * 3) + x]:
                points += 1
    if points >= 1:
        return True
    else:
        return False


def is_possible_in_cell(grid: List[List[int]], row_index: int, column_index: int, digit: int) -> bool:
    """
    Checks if any of the is_present_in functions returns a true. Author: Omar.

    :param grid: Two dimensional list
    :param row_index: Int value
    :param column_index: Int value
    :param digit: Int value
    :return: Boolean value
    """
    points = 0
    if is_present_in_row(grid, row_index, digit):
        points += 1
    if is_present_in_column(grid, column_index, digit):
        points += 1
    if is_present_in_block(grid, row_index, column_index, digit):
        points += 1
    if points >= 1:
        return False
    else:
        return True


# solving
def remove_impossible_candidates(grid: List[List[int]], candidates: List[List[str]]):
    """
    Finds and removes candidates that cannot be placed in a certain cell in the grid. Author: Omar.

    :param grid: Two dimensional list
    :param candidates: Two dimensional list
    """
    for i in range(9):
        for x in range(9):
            if grid[i][x] != 0:
                candidates[i][x] = ''
            elif grid[i][x] == 0:
                candidates_list = []
                for z in candidates[i][x]:
                    candidates_list.append(z)
                for o in range(len(candidates_list)):
                    if not is_possible_in_cell(grid, i, x, int(candidates_list[o])):
                        candidates_replacement = candidates[i][x].replace(str(candidates_list[o]), '')
                        candidates[i][x] = candidates_replacement


def set_value_in_cell_by_last_candidate(grid: List[List[int]], candidates: List[List[str]]) -> bool:
    """
    Sets an index in grid to the value of that same index in candidates if that index only contains one string character. Author: Omar.

    :param grid: Two dimensional list
    :param candidates: Two dimensional list
    :returns: Boolean value
    """
    s = 0
    for i in range(9):
        for x in range(9):
            count = 0
            for z in range(len(candidates[i][x])):
                count += 1
            if count == 1:
                grid[i][x] = int(candidates[i][x])
                s = 2
    if s == 2:
        return True
    else:
        return False


def find_lonely_candidate_in_row(candidates: List[List[str]], row_index: int, column_index: int):
    """
    Goes through the candidates and tries to find a lone string value in a row. Author: Omar.

    :param candidates: Two dimensional list
    :param row_index: Int value
    :param column_index: Int value
    """
    counter_for_candidates_row = 0
    list_of_candidates_to_check = []
    for g in candidates[row_index][column_index]:
        list_of_candidates_to_check.append(g)

    for i in range(len(list_of_candidates_to_check)):
        for x in range(len(candidates[row_index])):
            if list_of_candidates_to_check[i] in candidates[row_index][x]:
                counter_for_candidates_row += 1
        if counter_for_candidates_row == 1:
            candidates[row_index][column_index] = str(list_of_candidates_to_check[i])
            break
        counter_for_candidates_row = 0


def find_lonely_candidate_in_column(candidates: List[List[str]], row_index: int, column_index: int):
    """
    Goes through the candidates and tries to find a lone string value in a column. Author: Omar.

    :param candidates: Two dimensional list
    :param row_index: Int value
    :param column_index: Int value
    """
    counter_for_candidates_column = 0
    list_of_candidates_to_check = []
    for i in range(len(candidates[row_index][column_index])):
        list_of_candidates_to_check.append(candidates[row_index][column_index][i])

    for s in range(len(list_of_candidates_to_check)):
        for m in range(9):
            if list_of_candidates_to_check[s] in candidates[m][column_index]:
                counter_for_candidates_column += 1
        if counter_for_candidates_column == 1:
            candidates[row_index][column_index] = str(list_of_candidates_to_check[s])
            break
        counter_for_candidates_column = 0


def find_lonely_candidate_in_block(candidates: List[List[str]], row_index: int, column_index: int):
    """
    Goes through the candidates and tries to find a lone string value in a block. Author: Omar.

    :param candidates: Two dimensional list
    :param row_index: Int value
    :param column_index: Int value
    """
    counter_for_candidates_block = 0
    list_of_candidates_to_check = []
    for i in candidates[row_index][column_index]:
        list_of_candidates_to_check.append(i)
    for i in range(len(list_of_candidates_to_check)):
        for x in range(3):
            for s in range(3):
                if list_of_candidates_to_check[i] in candidates[((row_index // 3) * 3) + x][((column_index // 3) * 3) + s]:
                    counter_for_candidates_block += 1
        if counter_for_candidates_block == 1:
            candidates[row_index][column_index] = str(list_of_candidates_to_check[i])
            break
        counter_for_candidates_block = 0


def find_lonely_candidates(candidates: List[List[str]]):
    """
    Combines all find_lonely_candidate_in functions and goes through each one of them with all possible
    lonely candidates. Author: Omar.

    :param candidates: Two dimensional list
    """
    for i in range(9):
        for x in range(9):
            find_lonely_candidate_in_row(candidates, i, x)
            find_lonely_candidate_in_column(candidates, i, x)
            find_lonely_candidate_in_block(candidates, i, x)


# Main program
def main():
    # initializing the sudoku grid and candidates
    sudoku_grid = init_empty_grid()
    generated_candidates = init_candidates()
    # putting the sudoku in the grid
    set_default_sudoku_grid(sudoku_grid)
    # printing the sudoku
    print_grid(sudoku_grid)
    round_number = 1
    # Endless loop
    while True:
        remove_impossible_candidates(sudoku_grid, generated_candidates)
        find_lonely_candidates(generated_candidates)
        if not set_value_in_cell_by_last_candidate(sudoku_grid, generated_candidates):
            break
        print()
        print()
        print(f"ROUND {round_number}")
        print()
        round_number += 1
        print_grid(sudoku_grid)


def main2(sudoku_grid):
    generated_candidates = init_candidates()
    while True:
        remove_impossible_candidates(sudoku_grid, generated_candidates)
        find_lonely_candidates(generated_candidates)
        if not set_value_in_cell_by_last_candidate(sudoku_grid, generated_candidates):
            break
    return sudoku_grid
