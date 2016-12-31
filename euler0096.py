# Su Doku
# Problem 96
#
# Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called Latin Squares. The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical starting puzzle grid and its solution grid.
#
#   +-------+-------+-------+       +-------+-------+-------+
#   | 0 0 3 | 0 2 0 | 6 0 0 |       | 4 8 3 | 9 2 1 | 6 5 7 |
#   | 9 0 0 | 3 0 5 | 0 0 1 |       | 9 6 7 | 3 4 5 | 8 2 1 |
#   | 0 0 1 | 8 0 6 | 4 0 0 |       | 2 5 1 | 8 7 6 | 4 9 3 |
#   +-------+-------+-------+       +-------+-------+-------+
#   | 0 0 8 | 1 0 2 | 9 0 0 |       | 5 4 8 | 1 3 2 | 9 7 6 |
#   | 7 0 0 | 0 0 0 | 0 0 8 |       | 7 2 9 | 5 6 4 | 1 3 8 |
#   | 0 0 6 | 7 0 8 | 2 0 0 |       | 1 3 6 | 7 9 8 | 2 4 5 |
#   +-------+-------+-------+       +-------+-------+-------+
#   | 0 0 2 | 6 0 9 | 5 0 0 |       | 3 7 2 | 6 8 9 | 5 1 4 |
#   | 8 0 0 | 2 0 3 | 0 0 9 |       | 8 1 4 | 2 5 3 | 7 6 9 |
#   | 0 0 5 | 0 1 0 | 3 0 0 |       | 6 9 5 | 4 1 7 | 3 8 2 |
#   +-------+-------+-------+       +-------+-------+-------+
#
# A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary to employ "guess and test" methods in order to eliminate options (there is much contested opinion over this). The complexity of the search determines the difficulty of the puzzle; the example above is considered easy because it can be solved by straight forward direct deduction.
#
# The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).
#
# By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid; for example, 483 is the 3-digit number found in the top left corner of the solution grid above.

import copy;
import time;

start_time = time.time();

def print_execution_time():
    print "Execution time = %f seconds." % (time.time() - start_time);

def is_valid_in_row(sudoku, value, r, c):
    is_valid = True;
    found = [False] * 10;
    proposed_row = list(sudoku[r]);
    proposed_row[c] = value;
    for element in proposed_row:
        if element != 0 and found[element]:
            is_valid = False;
            break;
        else:
            found[element] = True;
    return is_valid;

def is_valid_in_column(sudoku, value, r, c):
    is_valid = True;
    found = [False] * 10;
    proposed_column = [];
    for row in sudoku:
        proposed_column.append(row[c]);
    proposed_column[r] = value;
    for element in proposed_column:
        if element != 0 and found[element]:
            is_valid = False;
            break;
        else:
            found[element] = True;
    return is_valid;

def is_valid_in_square(sudoku, value, r, c):
    is_valid = True;
    found = [False] * 10;
    proposed_square = [];
    i_start = 3 * (r / 3);
    i_end = i_start + 3;
    j_start = 3 * (c / 3);
    j_end = j_start + 3;
    for i in range(i_start, i_end):
        for j in range(j_start, j_end):
            proposed_square.append(sudoku[i][j]);
    index_in_square = ((r % 3) * 3) + (c % 3);
    proposed_square[index_in_square] = value;
    for element in proposed_square:
        if element != 0 and found[element]:
            is_valid = False;
            break;
        else:
            found[element] = True;
    return is_valid;

def is_valid(sudoku, value, r, c):
    #return is_valid_in_column(sudoku, value, r, c);
    return is_valid_in_row(sudoku, value, r, c) and is_valid_in_column(sudoku, value, r, c) and is_valid_in_square(sudoku, value, r, c);

# Returns the sudoku if there are no 0's in it as it is a complete solution. Otherwise finds the first 0 in the sudoku and the
# valid values for that 0. Returns an empty list if there are no valid values, as the starting sudoku is inconsistent.
# Otherwise, for every valid value, creates a deep copy of the sudoku and calls solve on it, returning its return values as an
# array of sodukus.
def solve(sudoku):
    solutions = [];
    r = None;
    c = None;
    found_zero = False;
    for r in range(9):
        for c in range(9):
            if sudoku[r][c] == 0:
                found_zero = True;
                break;
        if found_zero:
            break;
    if not found_zero:
        solutions.append(sudoku);
    else:
        for value in range(1, 10):
            if is_valid(sudoku, value, r, c):
                sudoku_copy = copy.deepcopy(sudoku);
                sudoku_copy[r][c] = value;
                solutions.extend(solve(sudoku_copy));
    return solutions;

sudokus = [];
infile = open("p096_sudoku.txt", "r");
for string in infile:
    if "Grid" in string:
        sudokus.append(list());
    else:
        sudokus[-1].append(list());
        for i in range(9):
            sudokus[-1][-1].append(int(string[i]));
infile.close();

'''
sudoku = sudokus[0];
print is_valid_in_row(sudoku, 4, 0, 0);
print is_valid_in_row(sudoku, 7, 0, 1);
print is_valid_in_row(sudoku, 1, 0, 2);
print is_valid_in_row(sudoku, 6, 0, 3);
print;
print is_valid_in_column(sudoku, 4, 0, 0);
print is_valid_in_column(sudoku, 7, 1, 0);
print is_valid_in_column(sudoku, 1, 2, 0);
print is_valid_in_column(sudoku, 6, 3, 0);
print;
print is_valid_in_square(sudoku, 3, 0, 0);
print is_valid_in_square(sudoku, 7, 1, 1);
print is_valid_in_square(sudoku, 9, 2, 2);
print is_valid_in_square(sudoku, 8, 3, 3);
print;
'''

upper_left_3_digit_sum = 0;
sudoku_number = 1;
#for sudoku in [sudokus[0], sudokus[1], sudokus[2]]:
for sudoku in sudokus:
    solutions = solve(sudoku);
    print "Sudoku %02d:" % sudoku_number;
    for solution in solutions:
        for row in solution:
            print row;
        upper_left_3_digits = (solution[0][0] * 100) + (solution[0][1] * 10) + (solution[0][2]);
        upper_left_3_digit_sum += upper_left_3_digits;
        print upper_left_3_digits;
        print;
    sudoku_number += 1;

print "upper_left_3_digit_sum = %d." % upper_left_3_digit_sum;
print;
print_execution_time();
