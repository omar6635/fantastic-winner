from typing import List
import random


# Recursion is like digging yourself in a hole and then digging yourself back out of it
def initialise_grid():
    """
    Create an empty two dimensional list with 9 lists each with 9 numbers, whereby all numbers are 0.
    """
    filled_grid = [[x-x for x in range(9)] for y in range(9)]
    return filled_grid


def initialise_candidates():
    """
    Create an empty two dimensional list with 9 lists each with 9 empty strings.
    """
    candidates_list = [["123456789" for x in range(9)] for y in range(9)]
    return candidates_list


def delete_impossible_candidates(candidates: List[List[str]], row, column, number):
    # set candidates index for the number to the number value
    candidates[row][column] = str(number)
    # remove that value from candidates in row
    for values in range(9):
        if str(number) in candidates[row][values]:
            candidates[row][values].replace(str(number), "")
    # remove that value from candidates in column
    for lists in range(9):
        if str(number) in candidates[lists][column]:
            candidates[lists][column].replace(str(number), "")
    # remove that value from candidates in block
    for lists in range(3):
        for values in range(3):
            if str(number) in candidates[((column//3) * 3) + lists][((row//3) * 3) + values]:
                candidates[((column // 3) * 3) + lists][((row // 3) * 3) + values].replace(str(number), "")


def fill_grid_with_solved_sudoku(grid: List[List[int]], candidates: List[List[str]]):
    for x in range(9):
        for y in range(9):
            # step 1: 'pick' between candidate index with least amount of candidates to put the number
            candidates_field_len = 9
            list_of_indexes = {}
            for i in range(2, 10):
                list_of_indexes[str(i)] = []
            for outer_lists in range(9):
                for inner_values in range(9):
                    if candidates[outer_lists][inner_values] != "":
                        if len(candidates[outer_lists][inner_values]) >= candidates_field_len:
                            candidates_field_len = len(candidates[outer_lists][inner_values])
                            list_of_indexes["candidates_field_len"].append([outer_lists, inner_values])
            random_index = random.choice(list_of_indexes[str(candidates_field_len)])
            # step 2: place a random number in a random cell in the grid
            if candidates[random_index[0]][random_index[1]]:
                random_numbers = list(candidates[random_index[0]][random_index[1]])
            else:
                random_numbers = [x for x in range(1, 10)]
            for numbers in random_numbers:
                grid[random_index[0]][random_index[1]] = int(random_numbers[numbers])
                if fill_grid_with_solved_sudoku(grid, candidates):
                    return True
                else:
                    grid[random_index[0]][random_index[1]] = 0
                    return False
    return True
