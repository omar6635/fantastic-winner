<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sudoku Website</title>
    <link href="/static/sudoku-9x9-css.css" rel="stylesheet">
</head>
<body>
<div class="sudoku_alignment">
<form method="post" id="form1" name="form1" action="check">
        <div class="sudoku">
        % counter = 0
        % for row in range(1, 10):
            % for column in range(1, 10):
            <% pulse_class = ""
             if "pulg" in solvable_sudoku[row-1][column-1]:
                pulse_class = "entry-field-flash-green"
             elif "pulr" in solvable_sudoku[row-1][column-1]:
                pulse_class = "entry-field-flash-red"
            end
            %>
            <% class_str = ""
            if column % 3 != 0 and row % 3 != 0 or column == 9 and row % 3 != 0:
                class_str = "single-field"
            elif column % 3 == 0 and row % 3 != 0:
                class_str = "single-field third-column"
            elif row % 3 == 0 and column % 3 != 0 or row % 3 == 0 and column == 9:
                class_str = "single-field third-row"
            elif row % 3 == 0 and column % 3 == 0 and column != 9:
                class_str = "single-field third-row third-column"
            end
            %>
            <div class="{{class_str}}">
                % if solvable_sudoku[row-1][column-1][0:3] == "dis":
                    <input style="color: gray" type="text" class="entry-field {{pulse_class}}" name="field{{str(counter)}}" value="{{solvable_sudoku[row-1][column-1][3:4]}}" readonly>
                % elif sudoku_input_grid[row-1][column-1] != "0":
                    <input style="color: black" type="text" maxlength="1" class="entry-field {{pulse_class}}" min="1" max="9" pattern="[1-9]" inputmode="numeric" name="field{{str(counter)}}" value="{{sudoku_input_grid[row-1][column-1]}}">
                % end
                </div>
            % counter += 1
            % end
        % end
</div>
% if "solved_grid" in locals():
    <div class="check_boxes_section">
     <p class="titles">Options</p>
        <label style="float: left; color: transparent ">
		<input type='checkbox' name='gray_out_correct' id='gray_out_correct' value='yes' checked>
            <div class="button"></div>
        </label>
        <div class="real_label">Gray out correct inputs?</div>
        <br><br><br>
        <label style="float: left; color: transparent">
		<input type='checkbox' name='graphic_feedback' id='graphic_feedback' value='yes' checked>
            <div class="button"></div>
        </label>
        <div class="real_label">Graphical feedback?</div>
        <br><br><br>
        <label style="float: left; color: transparent">
		<input type='checkbox' name='sudoku_text' id='sudoku_text' value='yes' checked>
            <div class="button"></div>
        </label>
        <div class="real_label">Text feedback?</div>
    </div>
% end
</form>

% if "text_feedback" in locals():
    % if text_feedback:
        <div class="text-output">
        <p class="titles">Feedback</p>
        % if grids_comparison[0] == "no_error":
            <p style="color: mediumseagreen">the inputs are right so far...</p>
            <p>{{grids_comparison[1]}}% of the sudoku is complete</p>
        % elif grids_comparison[0] == "error":
            <p style="color: red">One or more of the inputs are incorrect!</p>
            <p>{{grids_comparison[1]}}% of the sudoku is complete</p>
        % elif grids_comparison[0] == "complete":
            <p class="sudoku-complete">You have solved the Sudoku!</p>
        % end
        </div>
    % end
% end
<div class="sudoku_outputs">
    % if generate_button == True:
        <a href="sudoku_def"><button class="btns" type="button">Generate Sudoku</button></a>
    % else:
        <a href="restart"><button class="btns" type="button">Restart Sudoku</button></a>
    % end
    % if "solved_grid" in locals():
        <button class="btns" form="form1" type="submit" >Check Completion</button>
        <a href="sudoku_def"><button class="btns" type="button">New Sudoku</button></a>
    % end

</div>
</div>
</body>
</html>
