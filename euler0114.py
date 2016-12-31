# Counting block combinations I
# Problem 114
#
# A row measuring seven units in length has red blocks with a minimum length of three units placed on it, such that any two red blocks (which are allowed to be different lengths) are separated by at least one black square. There are exactly seventeen ways of doing this.
#
#       +---+---+---+---+---+---+---+    +---+---+---+---+---+---+---+    +---+---+---+---+---+---+---+
#       |   |   |   |   |   |   |   |    | R | R | R |   |   |   |   |    |   | R | R | R |   |   |   |
#       +---+---+---+---+---+---+---+    +---+---+---+---+---+---+---+    +---+---+---+---+---+---+---+
#
#       +---+---+---+---+---+---+---+    +---+---+---+---+---+---+---+    +---+---+---+---+---+---+---+
#       |   |   | R | R | R |   |   |    |   |   |   | R | R | R |   |    |   |   |   |   | R | R | R |
#       +---+---+---+---+---+---+---+    +---+---+---+---+---+---+---+    +---+---+---+---+---+---+---+
#
#       +---+---+---+---+---+---+---+    +---+---+---+---+---+---+---+    +---+---+---+---+---+---+---+
#       | R | R | R |   | R | R | R |    | R | R | R | R |   |   |   |    |   | R | R | R | R |   |   |
#       +---+---+---+---+---+---+---+    +---+---+---+---+---+---+---+    +---+---+---+---+---+---+---+
#
#       +---+---+---+---+---+---+---+    +---+---+---+---+---+---+---+    +---+---+---+---+---+---+---+
#       |   |   | R | R | R | R |   |    |   |   |   | R | R | R | R |    | R | R | R | R | R |   |   |
#       +---+---+---+---+---+---+---+    +---+---+---+---+---+---+---+    +---+---+---+---+---+---+---+
#
#       +---+---+---+---+---+---+---+    +---+---+---+---+---+---+---+    +---+---+---+---+---+---+---+
#       |   | R | R | R | R | R |   |    |   |   | R | R | R | R | R |    | R | R | R | R | R | R |   |
#       +---+---+---+---+---+---+---+    +---+---+---+---+---+---+---+    +---+---+---+---+---+---+---+
#
#       +---+---+---+---+---+---+---+    +---+---+---+---+---+---+---+
#       |   | R | R | R | R | R | R |    | R | R | R | R | R | R | R |
#       +---+---+---+---+---+---+---+    +---+---+---+---+---+---+---+
#
# How many ways can a row measuring fifty units in length be filled?
#
# NOTE: Although the example above does not lend itself to the possibility, in general it is permitted to mix block sizes. For example, on a row measuring eight units in length you could use red (3), black (1), and red (4).

import time;

start_time = time.time();

def print_execution_time():
    print 'Execution time = %f seconds.' % (time.time() - start_time);

# n = row size, m = minimum block length
#
# For the cases with at least one red cell, when m = 3, the first n that can contain a red block is when n = m = 3, and there
# is 1 way to fill the row:
#
#       +---+---+---+
#       | R | R | R |
#       +---+---+---+
#
# So for cases where row[2] = row[m - 1] is red, there is 1 way to fill it. Represent this with an array where the value at
# index i equals the number of ways to fill the row such that the rightmost red square is at i. So far, the array is:
#
#       [ 0,  0,  1 ]
#
# Add a square to the right. There are 2 more ways to fill the newly formed row, each with the rightmost red square at the new
# square at index 3. Update the array accordingly:
#
#       +---+---+---+---+
#       |   | R | R | R |
#       +---+---+---+---+
#       | R | R | R | R |                    [0, 0, 1, 2]
#       +---+---+---+---+
#
# Continue by adding 1 more cell to the right, then another. Each time, the value in the corresponding position in the array
# increases by 1:
#
#       +---+---+---+---+---+
#       |   |   | R | R | R |
#       +---+---+---+---+---+
#       |   | R | R | R | R |
#       +---+---+---+---+---+
#       | R | R | R | R | R |                [0, 0, 1, 2, 3]
#       +---+---+---+---+---+
#
#       +---+---+---+---+---+---+
#       |   |   |   | R | R | R |
#       +---+---+---+---+---+---+
#       |   |   | R | R | R | R |
#       +---+---+---+---+---+---+
#       |   | R | R | R | R | R |
#       +---+---+---+---+---+---+
#       | R | R | R | R | R | R |            [0, 0, 1, 2, 3, 4]
#       +---+---+---+---+---+---+
#
# After adding the next cell on the right, there is the same pattern of i - m + 2 = 6 - 3 + 2 = 5 ways, each with 1 block
# pushed all the way to the right. But there is for the first time a new way of placing 2 blocks, and there is 1 way to place
# 2 blocks. Accordingly, the new array entry is 1 more than the previous pattern would have produced:
#
#       +---+---+---+---+---+---+---+
#       |   |   |   |   | R | R | R |
#       +---+---+---+---+---+---+---+
#       |   |   |   | R | R | R | R |
#       +---+---+---+---+---+---+---+
#       |   |   | R | R | R | R | R |
#       +---+---+---+---+---+---+---+
#       |   | R | R | R | R | R | R |
#       +---+---+---+---+---+---+---+
#       | R | R | R | R | R | R | R |
#       +---+---+---+---+---+---+---+
#       | R | R | R |   | R | R | R |        [0, 0, 1, 2, 3, 4, 6]
#       +---+---+---+---+---+---+---+
#
# After adding the next cell on the right, there is again the same pattern of i - m + 2 = 7 - 3 + 2 = 6 ways of rightmost
# single blocks. But there are again 2-block ways, this time 4 such ways. The total is 6 + 4 = 10:
#
#       +---+---+---+---+---+---+---+---+
#       |   |   |   |   |   | R | R | R |
#       +---+---+---+---+---+---+---+---+
#       |   |   |   |   | R | R | R | R |
#       +---+---+---+---+---+---+---+---+
#       |   |   |   | R | R | R | R | R |
#       +---+---+---+---+---+---+---+---+
#       |   |   | R | R | R | R | R | R |
#       +---+---+---+---+---+---+---+---+
#       |   | R | R | R | R | R | R | R |
#       +---+---+---+---+---+---+---+---+
#       | R | R | R | R | R | R | R | R |
#       +---+---+---+---+---+---+---+---+
#       |   | R | R | R |   | R | R | R |
#       +---+---+---+---+---+---+---+---+
#       | R | R | R | R |   | R | R | R |
#       +---+---+---+---+---+---+---+---+
#       | R | R | R |   |   | R | R | R |
#       +---+---+---+---+---+---+---+---+
#       | R | R | R |   | R | R | R | R |    [0, 0, 1, 2, 3, 4, 6, 10]
#       +---+---+---+---+---+---+---+---+
#
# The 2-block ways may be divided into 2 groups: one with a rightmost 3-cell block and the other with a rightmost 4-cell
# block. The number of ways is dictated by the minimal 3-block requiring its 3 cells plus 1 for the space plus 3 for the first
# way's rightmost block, and the minimal 3 plus 1 plus 4 for the second way's rightmost block. The number of groups is
# therefore i - 2m = 8 - 3(2) = 8 - 6 = 2 in this case.
#
# The first group has 4 spaces in which to place the left block after allowing for the space cell and the rightmost 3-cell
# block. If these left 4 blocks are isolated, as they are in the lower group below, the isolated rows are identical to the
# first 2 cases above:
#
#       +---+---+---+---+---+---+---+---+
#       |   | R | R | R |   | R | R | R |
#       +---+---+---+---+---+---+---+---+
#       | R | R | R | R |   | R | R | R |
#       +---+---+---+---+---+---+---+---+
#       | R | R | R |   |   | R | R | R |
#       +---+---+---+---+---+---+---+---+
#
#       +---+---+---+---+ ---
#       |   | R | R | R |
#       +---+---+---+---+  Same as 4-cell case above (2nd overall case) when i = 3: array[3] = 2 ways.
#       | R | R | R | R |
#       +---+---+---+---+ ---
#       | R | R | R |      Same as 3-cell case above (1st overall case) when i = 2: array[2] = 1 way.
#       +---+---+---+     ---
#
# The number of additional second block ways is therefore array[2] + array[3] + .. + array[1 + number of groups] =
# array[2] + array[3] = 1 + 2 = 3 for this group.
# 
# The second group has 3 spaces in which to place the left block after allowing for the space cell and the rightmost 4-cell
# block. Following the same treatment as for the first group:
#
#       +---+---+---+---+---+---+---+---+
#       | R | R | R |   | R | R | R | R |
#       +---+---+---+---+---+---+---+---+
#
#       +---+---+---+     ---
#       | R | R | R |      Same as 3-cell case above (1st overall case) when i = 2: array[2] = 1 way.
#       +---+---+---+     ---
#
# The number of additional multi-block ways is array[2] = 1 for this group.
#
# In general, for a given group, the number of additional multi-block ways is the summation of the first m-cell case, the
# second (m + 1)-cell case, and so on until the number of groups is reached. This is the sum of array[m - 1], array[m], ...
# array[m + group_count].

"""
# This is the first experimental solution which also gives the correct answer. It is however more difficult to explain.
n = 50;
m = 3;
row = [0] * n;
row[m - 1] = 1;
for i in range(m, n):
    row[i] += i - m + 2;
    for j in range(2 * m, i + 1):
        # print i, j, j - m - 1;
        for k in range(2, j - m):
            row[i] += row[k];
"""
n = 50;
m = 3;
row = [0] * n;
row[m - 1] = 1;
for i in range(m, n):
    row[i] += i - m + 2;
    for group in range(i - (2 * m) + 1):
        #for left_subset in range(2, group + 3):
        for left_subset in range(m - 1, m + group):
            row[i] += row[left_subset];

print row;
# Add 1 for the completely empty row.
print sum(row) + 1;

print_execution_time();
