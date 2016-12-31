# Path sum: two ways
#
# In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.
#
#   --                   --
#   | 131 673 234 103  18 |
#   |  |                  |
#   | 201--96-342 965 150 |
#   |          |          |
#   | 630 803 746-422 111 |
#   |              |      |
#   | 537 699 497 121 956 |
#   |              |      |
#   | 805 732 524  37-331 |
#   --                   --
#
# Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.

import csv;
import sys
import time;

start_time = time.time();

PRINT_MATRICES = False;

FILENAME = "p081_matrix_toy_1.txt";
FILENAME = "p081_matrix_toy_2.txt";
FILENAME = "p081_matrix.txt";

def print_matrix(m):
    for r in m:
        for e in r:
            print "%6d" % e, # comma instead of semi-colon to suppress the newline
        print;
    print;

def collapse_triangle(m, r, c):
    d = len(m[0]);
    d_minus_1 = d - 1;
    right = sys.maxint;
    if c < d_minus_1:
        right = m[r][c + 1];
    lower = sys.maxint;
    if r < d_minus_1:
        lower = m[r + 1][c];
        del m[r + 1][c];
        if c == 0:
            del m[r + 1];
    if (r == 0) and (c == d - 2):
        del m[r][c + 1];
    # print m[r][c], right, lower, m[r][c] + min(right, lower);
    m[r][c] += min(right, lower);
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

for c_start in range(d - 2, 0, -1):
    if PRINT_MATRICES:
        print "--------------------------------------------------------------------------------------------------------------------------------";
    r_plus_c = c_start + d - 1;
    for r in range(d - 1, c_start - 1, -1):
        c = r_plus_c - r;
        # print r, c;
        m = collapse_triangle(m, r, c);
        if PRINT_MATRICES:
            print_matrix(m);

for r_start in range(d - 1, -1, -1):
    if PRINT_MATRICES:
        print "--------------------------------------------------------------------------------------------------------------------------------";
    for r in range(r_start, -1, -1):
        c = r_start - r;
        # print r, c;
        m = collapse_triangle(m, r, c);
        if PRINT_MATRICES:
            print_matrix(m);

print "minimum path sum = %d." % m[0][0];
print;

"""
# This doesn't work.

d = len(m);

while d > 1:
    for r in range(d - 1):
        r = d - c - 2;
        northwest = m[r][c];
        northeast = sys.maxint;
        southwest = sys.maxint;
        southeast = sys.maxint;
        if (c <= d - 2):
            northeast = m[r][c + 1];
        if (r <= d - c - 2):
            southwest = m[r + 1][c];
            if (c <= d - 2):
                southeast = m[r + 1][c + 1];
        '''
        print "%6d %6d" % (northwest, northeast);
        print "%6d %6d" % (southwest, southeast);
        print;
        '''
        m[r][c] = northwest + min(northeast, southwest) + southeast;
    print_matrix(m);
    print;
    for r in range(2, d):
        for c in range(d - r + 1, d):
            m[r - 1][c - 1] = m[r][c];
    print_matrix(m);
    print;
    for r in range(d - 1):
        del m[r][d - 1];
    del m[d - 1];
    print_matrix(m);
    print;

    d = len(m);
"""

print "Execution time = %f seconds." % (time.time() - start_time);
