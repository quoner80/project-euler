# Path sum: four ways
# Problem 83
#
# NOTE: This problem is a significantly more challenging version of Problem 81.
#
# In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up, and down, is indicated in bold red and is equal to 2297.
#
#   --                   --
#   | 131 673 234-103--18 |
#   |  |       |       |  |
#   | 201--96-342 965 150 |
#   |                  |  |
#   | 630 803 746 422-111 |
#   |              |      |
#   | 537 699 497 121 956 |
#   |              |      |
#   | 805 732 524  37-331 |
#   --                   --
#
# Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by moving left, right, up, and down.

import csv;
import sys
import time;

start_time = time.time();

INFINITE = sys.maxint;

PRINT_MATRICES = False;

FILENAME = "p081_matrix_toy_1.txt";
FILENAME = "p081_matrix_toy_2.txt";
FILENAME = "p083_matrix.txt";

def print_matrix(m):
    for r in m:
        for e in r:
            if e != INFINITE:
                print "%6d" % e, # comma instead of semi-colon to suppress the newline
            else:
                print "%6s" % "inf", # ibid.
        print;
    print;

def unrolled_index(r, c, d):
    return (r * d) + c;

def row_column(i, d):
    return (i / d, i % d);

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

# Source: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
d = len(m);
d_minus_1 = d - 1;
# Don't do this--all rows are the same object!
# minimum_path_sums = [[INFINITE] * d] * d; 
minimum_path_sums = []; 
for r in range(d):
    minimum_path_sums.append([INFINITE] * d);
minimum_path_sums[0][0] = m[0][0];
unvisited = range(d * d);
r = 0;
c = 0;
while len(unvisited) > 0:
    unvisited.remove(unrolled_index(r, c, d));
    center = minimum_path_sums[r][c];
    if PRINT_MATRICES:
        print "center @ %2d,%2d = %d." % (r, c, center);
        print unvisited;
        print_matrix(minimum_path_sums);
    if r <= 0 or unrolled_index(r - 1, c, d) not in unvisited:
        north = INFINITE;
    else:
        north = m[r - 1][c];
        minimum_path_sums[r - 1][c] = min(minimum_path_sums[r - 1][c], center + north);
    if r >= d_minus_1 or unrolled_index(r + 1, c, d) not in unvisited:
        south = INFINITE;
    else:
        south = m[r + 1][c];
        minimum_path_sums[r + 1][c] = min(minimum_path_sums[r + 1][c], center + south);
    if c <= 0 or unrolled_index(r, c - 1, d) not in unvisited:
        west = INFINITE;
    else:
        west = m[r][c - 1];
        minimum_path_sums[r][c - 1] = min(minimum_path_sums[r][c - 1], center + west);
    if c >= d_minus_1 or unrolled_index(r, c + 1, d) not in unvisited:
        east = INFINITE;
    else:
        east = m[r][c + 1];
        minimum_path_sums[r][c + 1] = min(minimum_path_sums[r][c + 1], center + east);
    minimum_direction = min([north, south, west, east]);
    minimum_unvisited = INFINITE;
    (r, c) = (-1, -1);
    for i in unvisited:
        (r_i, c_i) = row_column(i, d);
        if minimum_path_sums[r_i][c_i] < minimum_unvisited:
            minimum_unvisited = minimum_path_sums[r_i][c_i];
            (r, c) = (r_i, c_i);
    # This doesn't need to process the whole graph--just to the lower right element.
    if (r, c) == (d - 1, d - 1):
        break;
print "center @ %2d,%2d = %d." % (r, c, minimum_path_sums[r][c]);
print unvisited;
print_matrix(minimum_path_sums);

print "minimum path sum = %d." % minimum_path_sums[-1][-1];
print;

print "Execution time = %f seconds." % (time.time() - start_time);
