from bottle import route, run, template, request, static_file
from Sudokutools_UPDATED import main2
from python_grids import *
from random import choice


@route("/")
def sudoku_grid_site():
    try:
        empty_grid = empty_sudoku_grid()
    except TypeError:
        return template("error_page.tpl")
    return template('sudoku_grid_tmpl.tpl',
                    sudoku_input_grid=empty_grid,
                    solvable_sudoku=empty_grid,
                    generate_button=True,
                    text_outputs=False)


@route("/restart")
def restart_sudoku():
    try:
        solvable_sudoku = read_and_append_sudoku("./start_grid.txt")
        write_the_sudoku(solvable_sudoku, "./sudoku_grid_for_project")
        solved_grid = sudoku_grid_solved(solvable_sudoku)
        write_the_sudoku(solved_grid, "./solved_grid_for_project")
    except TypeError:
        return template("error_page.tpl")
    return template("sudoku_grid_tmpl.tpl",
                    sudoku_input_grid=solvable_sudoku,
                    solvable_sudoku=solvable_sudoku,
                    solved_grid=solved_grid,
                    generate_button=False,
                    text_outputs=False)


@route("/sudoku_def")
def generate():
    try:
        solvable_sudoku = sudoku_gen()
        write_the_sudoku(solvable_sudoku, "./sudoku_grid_for_project")
        write_the_sudoku(solvable_sudoku, "./start_grid.txt")
        solved_grid = sudoku_grid_solved(solvable_sudoku)
        write_the_sudoku(solved_grid, "./solved_grid_for_project")
    except TypeError:
        return template("error_page.tpl")
    return template("sudoku_grid_tmpl.tpl",
                    sudoku_input_grid=solvable_sudoku,
                    solvable_sudoku=solvable_sudoku,
                    solved_grid=solved_grid,
                    generate_button=False,
                    text_outputs=False)


@route("/static/<filename>")
def server_static(filename):
    return static_file(filename, root="../static")


@route("/check", method="POST")
def sudoku_grid_post():
    try:
        checkbox_values = checkbox_values_post(request.forms)
        text_feedback = checkbox_values[2]
        write_checkboxes_html(checkbox_values)
        input_grid = user_sudoku_saver(request.forms)
        solvable_sudoku = read_and_append_sudoku("./sudoku_grid_for_project")
        solved_grid = read_and_append_sudoku("./solved_grid_for_project")
        grids_comparison = compare_input_and_solved(solved_grid, input_grid, solvable_sudoku, checkbox_values)
        write_the_sudoku(solvable_sudoku, "./sudoku_grid_for_project")
    except TypeError:
        return template("error_page.tpl")
    return template("sudoku_grid_tmpl.tpl",
                    sudoku_input_grid=input_grid,
                    solvable_sudoku=solvable_sudoku,
                    grids_comparison=grids_comparison,
                    solved_grid=solved_grid,
                    generate_button=False,
                    text_feedback=text_feedback,
                    checkbox_values=checkbox_values)


def user_sudoku_saver(forms):
    sudoku_input_grid = []
    counter = 0
    for empty_lists in range(9):
        sudoku_input_grid.append([])
    for lists in range(9):
        for values in range(9):
            sudoku_input_grid[lists].append(forms.get("field" + str(counter)))
            counter += 1
    return sudoku_input_grid


def sudoku_gen():
    test_sudoku = choice([grid_1, grid_2, grid_3, grid_4, grid_5, grid_6, grid_7, grid_8])
    return test_sudoku


def write_the_sudoku(sudoku_grid, path: str):
    open_file = open(path, "w")
    for outer_lists in sudoku_grid:
        for values in outer_lists:
            if type(values) == int:
                open_file.write(str(values) + "\n")
            else:
                open_file.write(values + "\n")
    open_file.close()


def read_and_append_sudoku(path):
    sudoku_grid_list = []
    for i in range(9):
        sudoku_grid_list.append([])
    open_file = open(path, "r")
    txt_file = open_file.readlines()
    counter = 0
    for outer_lists in range(9):
        for values in range(9):
            txt_file[counter] = txt_file[counter].replace("\n", "")
            sudoku_grid_list[outer_lists].append(txt_file[counter])
            counter += 1
    open_file.close()
    return sudoku_grid_list


def write_checkboxes_html(button_values):
    str_gray_out = ""
    str_graph_feed = ""
    str_outputs = ""
    if button_values[0]:
        str_gray_out = "checked"
    if button_values[1]:
        str_graph_feed = "checked"
    if button_values[2]:
        str_outputs = "checked"

    sudoku_tpl_r = open("sudoku_grid_tmpl.tpl", "r")
    sudoku_tpl_lines = sudoku_tpl_r.readlines()
    sudoku_tpl_lines[47] = f"\t\t<input type='checkbox' name='gray_out_correct' id='gray_out_correct' value='yes' {str_gray_out}>\n"
    sudoku_tpl_lines[53] = f"\t\t<input type='checkbox' name='graphic_feedback' id='graphic_feedback' value='yes' {str_graph_feed}>\n"
    sudoku_tpl_lines[59] = f"\t\t<input type='checkbox' name='sudoku_text' id='sudoku_text' value='yes' {str_outputs}>\n"
    sudoku_tpl_r.close()

    sudoku_tpl_w = open("sudoku_grid_tmpl.tpl", "w")
    sudoku_tpl_w.writelines(sudoku_tpl_lines)
    sudoku_tpl_w.close()


def empty_sudoku_grid():
    empty_grid = []
    nine_list = ["dis", "dis", "dis", "dis", "dis", "dis", "dis", "dis", "dis"]
    for i in range(9):
        empty_grid.append(nine_list)
    return empty_grid


def checkbox_values_post(forms):
    gray_out_inp = forms.get("gray_out_correct")
    graph_feedback = forms.get("graphic_feedback")
    text_outputs = forms.get("sudoku_text")
    return gray_out_inp, graph_feedback, text_outputs


def get_def_sudoku_length():
    open_grid = open("./start_grid.txt", "r")
    grid_list = open_grid.readlines()
    numbers = [number for number in grid_list if number != "\n"]
    return len(numbers)


def sudoku_grid_solved(grid):
    grid_deepcopy = []
    for lists in range(len(grid)):
        grid_deepcopy.append(grid[lists][:])
    counter_list_outer = 0
    counter_list_inner = 0
    for outer_lists in grid_deepcopy:
        for list_inner in outer_lists:
            if list_inner == "" or list_inner[1:5] == "pulr":
                grid_deepcopy[counter_list_outer][counter_list_inner] = "0"
            if list_inner[0:3] == "dis":
                grid_deepcopy[counter_list_outer][counter_list_inner] = list_inner[3:4]
            counter_list_inner += 1
        counter_list_inner = 0
        counter_list_outer += 1
    grid_int = [[int(j) for j in i] for i in grid_deepcopy]
    solved_grid = main2(grid_int)
    return solved_grid


def compare_input_and_solved(grid_solved, grid_input, solvable_sudoku, checkbox_values):
    def_sudoku_numbers = get_def_sudoku_length()
    pulsing = ""
    graying = ""
    if checkbox_values[1]:
        pulsing = "pul"
    if checkbox_values[0]:
        graying = "dis"
    return_list = []
    points_percentage = 0
    counter_lists = 0
    for list_outer in solvable_sudoku:
        counter_values = 0
        for inner_values in list_outer:
            # remove pulse string if field has already pulsed
            if "pulg" in inner_values:
                inner_values = inner_values.replace("pulg", "")
            # tracking points to print percentage using an if-clause
            if grid_input[counter_lists][counter_values] == grid_solved[counter_lists][counter_values]:
                points_percentage += 1
            # if grid_input returned a value and it wasn't disabled
            if grid_input[counter_lists][counter_values] != "" and "dis" not in inner_values:
                # if the returned value is correct
                if grid_input[counter_lists][counter_values] == grid_solved[counter_lists][counter_values]:
                    # regulating pulsing and graying sequences so they don't contradict each other
                    if "x" not in inner_values:
                        inner_values = str(graying) + grid_input[counter_lists][counter_values] + str(pulsing) + "gx"
                    elif "x" in inner_values:
                        inner_values = str(graying) + grid_input[counter_lists][counter_values] + "x"
                # else if returned value is incorrect
                else:
                    return_list.append("error")
                    inner_values = grid_input[counter_lists][counter_values] + str(pulsing) + "r"
                    inner_values.replace("x", "")
            # if given value was wrong and isn't now, remove red pulsing string
            elif "pulr" in inner_values:
                inner_values = inner_values.replace("pulr", "")
            solvable_sudoku[counter_lists][counter_values] = inner_values
            counter_values += 1
        counter_lists += 1

    if points_percentage == 81:
        return_list.append("complete")
    percentage_completed = round((points_percentage-def_sudoku_numbers) / (81-def_sudoku_numbers) * 100)
    if "complete" in return_list:
        return "complete", percentage_completed
    elif "error" in return_list:
        return "error", percentage_completed
    else:
        return "no_error", percentage_completed


run(debug=True, reloader=True)
