# Path sum: three ways
# Problem 82
#
# NOTE: This problem is a more challenging version of Problem 81.
#
# The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.
#
#   --                   --
#   | 131 673 234-103--18 |
#   |          |          |
#   | 201--96-342 965 150 |
#   |                     |
#   | 630 803 746 422 111 |
#   |                     |
#   | 537 699 497 121 956 |
#   |                     |
#   | 805 732 524  37 331 |
#   --                   --
#
# Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the left column to the right column.

import csv;
import sys
import time;

start_time = time.time();

PRINT_MATRICES = False;

FILENAME = "p081_matrix_toy_1.txt";
FILENAME = "p081_matrix_toy_2.txt";
FILENAME = "p082_matrix.txt";

def print_matrix(m):
    for r in m:
        for e in r:
            print "%6d" % e, # comma instead of semi-colon to suppress the newline
        print;
    print;

def update_column(m, c):
    d = len(m);
    column = [0] * d;
    column_plus_right = [0] * d;
    for r in range(d):
        column[r] = m[r][c];
        column_plus_right[r] = column[r] + m[r][c + 1];
    for r in range(d):
        element = column[r];
        sum_from_r_via_s = [0] * d;
        sum_from_r_via_s[r] = column_plus_right[r];
        column_only = element;
        for s in range(r - 1, -1, -1):
            sum_from_r_via_s[s] = column_only + column_plus_right[s];
            column_only += column[s];
        column_only = element;
        for s in range(r + 1, d):
            sum_from_r_via_s[s] = column_only + column_plus_right[s];
            column_only += column[s];
        # print sum_from_r_via_s;
        m[r][c] = min(sum_from_r_via_s);
    return m;

m = [];
with open(FILENAME) as matrix_file:
    matrix = csv.reader(matrix_file);
    for row in matrix:
        r = [];
        for element in row:
            r.append(int(element));
        m.append(r);
if PRINT_MATRICES:
    print_matrix(m);

d = len(m);
for c in range(d - 2, -1, -1):
    m = update_column(m, c);
    if PRINT_MATRICES:
        print_matrix(m);

minimum_path_sum = sys.maxint;
for r in range(d):
    if m[r][0] < minimum_path_sum:
        minimum_path_sum = m[r][0];

print "minimum path sum = %d." % minimum_path_sum;
print;

print "Execution time = %f seconds." % (time.time() - start_time);
