# Counting block combinations II
# Problem 115
#
# NOTE: This is a more difficult version of Problem 114.
#
# A row measuring n units in length has red blocks with a minimum length of m units placed on it, such that any two red blocks (which are allowed to be different lengths) are separated by at least one black square.
#
# Let the fill-count function, F(m, n), represent the number of ways that a row can be filled.
#
# For example, F(3, 29) = 673135 and F(3, 30) = 1089155.
#
# That is, for m = 3, it can be seen that n = 30 is the smallest value for which the fill-count function first exceeds one million.
#
# In the same way, for m = 10, it can be verified that F(10, 56) = 880711 and F(10, 57) = 1148904, so n = 57 is the least value for which the fill-count function first exceeds one million.
#
# For m = 50, find the least value of n for which the fill-count function first exceeds one million.

import time;

start_time = time.time();

def print_execution_time():
    print 'Execution time = %f seconds.' % (time.time() - start_time);

# Algorithm from problem 114.
def count_ways(n, m):
    row = [0] * n;
    row[m - 1] = 1;
    for i in range(m, n):
        row[i] += i - m + 2;
        for group in range(i - (2 * m) + 1):
            for left_subset in range(m - 1, group + m):
                row[i] += row[left_subset];
    # Add 1 for the completely empty row.
    return sum(row) + 1;

target = 1000000;
m = 50;
n = m - 1;
count = 0;
while count <= target:
    n += 1;
    count = count_ways(n, m);
    print n, count;
print;
print n;
print;

print_execution_time();
