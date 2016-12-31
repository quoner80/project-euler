# Red, green or blue tiles
# Problem 116
#
# A row of five black square tiles is to have a number of its tiles replaced with coloured oblong tiles chosen from red (length two), green (length three), or blue (length four).
#
# If red tiles are chosen there are exactly seven ways this can be done.
#
#       +---+---+---+---+---+    +---+---+---+---+---+    +---+---+---+---+---+    +---+---+---+---+---+
#       | R---R |   |   |   |    |   | R---R |   |   |    |   |   | R---R |   |    |   |   |   | R---R |
#       +---+---+---+---+---+    +---+---+---+---+---+    +---+---+---+---+---+    +---+---+---+---+---+
#
#       +---+---+---+---+---+    +---+---+---+---+---+    +---+---+---+---+---+
#       | R---R | R---R |   |    |   | R---R | R---R |    | R---R |   | R---R |
#       +---+---+---+---+---+    +---+---+---+---+---+    +---+---+---+---+---+
#
# If green tiles are chosen there are three ways.
#
#       +---+---+---+---+---+    +---+---+---+---+---+    +---+---+---+---+---+
#       | G---G---G |   |   |    |   | G---G---G |   |    |   |   | G---G---G |
#       +---+---+---+---+---+    +---+---+---+---+---+    +---+---+---+---+---+
#
# And if blue tiles are chosen there are two ways.
#
#       +---+---+---+---+---+    +---+---+---+---+---+
#       | B---B---B---B |   |    |   | B---B---B---B |
#       +---+---+---+---+---+    +---+---+---+---+---+
#
# Assuming that colours cannot be mixed there are 7 + 3 + 2 = 12 ways of replacing the black tiles in a row measuring five units in length.
#
# How many different ways can the black tiles in a row measuring fifty units in length be replaced if colours cannot be mixed and at least one coloured tile must be used?
#
# NOTE: This is related to Problem 117.

import time;

start_time = time.time();

def print_execution_time():
    print 'Execution time = %f seconds.' % (time.time() - start_time);

# n = row size, m = block length
#
# For the cases with at least one red cell, when m = 2, the first n that can contain a red block is when n = m = 2, and there
# is 1 way to fill the row:
#
#       +---+---+
#       | R---R |
#       +---+---+
#
# So for cases where row[2] = row[m - 1] is red, there is 1 way to fill it. Represent this with an array where the value at
# index i equals the number of ways to fill the row such that the rightmost red square is at i. So far, the array is:
#
#       [ 0,  1 ]
#
# Add a square to the right. There is 1 more way to fill the newly formed row, with the rightmost red square at the new square
# at index 3. Update the array accordingly:
#
#       +---+---+---+
#       |   | R---R |                    [0, 1, 1]
#       +---+---+---+
#
# After adding the next cell on the right, there is the same pattern of 1 way as above. But there is for the first time a new
# way of placing 2 blocks, and there is 1 way to place 2 blocks. Accordingly, the new array entry is 1 more than the previous
# pattern would have produced:
#
#       +---+---+---+---+
#       |   |   | R---R |
#       +---+---+---+---+
#       | R---R | R---R |                [0, 1, 1, 2]
#       +---+---+---+---+
#
# Adding 1 more cell on the right, then another gives:
#
#       +---+---+---+---+---+
#       |   |   |   | R---R |
#       +---+---+---+---+---+
#       | R---R |   | R---R |
#       +---+---+---+---+---+
#       |   | R---R | R---R |            [0, 1, 1, 2, 3]
#       +---+---+---+---+---+
#
#       +---+---+---+---+---+---+
#       |   |   |   |   | R---R |
#       +---+---+---+---+---+---+
#       | R---R |   |   | R---R |
#       +---+---+---+---+---+---+
#       |   | R---R |   | R---R |
#       +---+---+---+---+---+---+
#       |   |   | R---R | R---R |
#       +---+---+---+---+---+---+
#       | R---R | R---R | R---R |        [0, 1, 1, 2, 3, 5]
#       +---+---+---+---+---+---+
#
# For the final above case where i = 5, there is the 1 way with the single rightmost 2-cell block. And the remaining ways are
# identical to the first 3 cases above:
#
#       +---+---+---+---+---+---+
#       | R---R |   |   | R---R |
#       +---+---+---+---+---+---+
#       |   | R---R |   | R---R |
#       +---+---+---+---+---+---+
#       |   |   | R---R | R---R |
#       +---+---+---+---+---+---+
#       | R---R | R---R | R---R |
#       +---+---+---+---+---+---+
#
#       +---+---+         ---
#       | R---R |          Same as 2-cell case above (1st overall case) when i = 1: array[1] = 1 way.
#       +---+---+---+     ---
#       |   | R---R |      Same as 3-cell case above (2nd overall case) when i = 2: array[2] = 1 way.
#       +---+---+---+---+ ---
#       |   |   | R---R |
#       +---+---+---+---+  Same as 4-cell case above (3rd overall case) when i = 3: array[3] = 2 ways.
#       | R---R | R---R |
#       +---+---+---+---+ ---
#
# The number of additional second block ways is therefore array[1] + array[2] + .. + array[i - 2] = array[1] + array[2] +
# array[3] = 1 + 1 + 2 = 4 for this group.
# 
# In general, for a given group, the number of additional multi-block ways is the summation of the first m-cell case, the
# second (m + 1)-cell case, and so on through the (i - m + 1)-cell case. This is array[m - 1] + array[m] + ... + array[m - i].
def count_ways(n, m):
    row = [0] * n;
    row[m - 1] = 1;
    for i in range(m, n):
        row[i] += 1;
        for left_subset in range(m - 1, i - m + 1):
            row[i] += row[left_subset];
    # print row;  
    return sum(row);

n_2 = count_ways(50, 2);
n_3 = count_ways(50, 3);
n_4 = count_ways(50, 4);
print 'n_2 =', n_2;
print 'n_3 =', n_3;
print 'n_4 =', n_4;
print;
print 'total =', (n_2 + n_3 + n_4);
print;

print_execution_time();
