# Maximum path sum II
#
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
#
#    3
#   7 4
#  2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.
#
# NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 2^99 altogether! If you could check one trillion (10^12) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)

import csv;
import time;

start_time = time.time();

FILENAME = "p067_triangle_toy.txt";
FILENAME = "p067_triangle.txt";

triangle = [];
with open(FILENAME) as csvfile:
    reader = csv.reader(csvfile, delimiter = ' ');
    for line in reader:
      row = [];
      triangle.append(row);
      for node in line:
        row.append(int(node));
print triangle;
row_count = len(triangle);
for row_index in range(row_count - 2, -1, -1):
    row = triangle[row_index];
    next_row = triangle[row_index + 1];
    for node_index in range(len(row)):
        row[node_index] += max(next_row[node_index], next_row[node_index + 1]);
print;
print triangle[0][0];

print;
print "Execution time = %f seconds." % (time.time() - start_time);
