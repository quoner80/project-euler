# Cuboid route
# Problem 86
#
# A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner. By travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10 and the path is shown on the diagram.
#
#                                    F
#       +---------------------------+
#      /|                         ./|
#     / |                       . / |
#    /  |                     .  /  | 3
#   +---------------------------+   |
#   |   |                 .     |   |
#   |   +---------------+-------|---+
#   |  /           .            |  /
#   | /       .                 | / 5
#   |/   .                      |/
#   +---------------------------+
#  S              6
#
# However, there are up to three "shortest" path candidates for any given cuboid and the shortest route doesn't always have integer length.
#
# It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, with integer dimensions, up to a maximum size of M by M by M, for which the shortest route has integer length when M = 100. This is the least value of M for which the number of solutions first exceeds two thousand; the number of solutions when M = 99 is 1975.
#
# Find the least value of M such that the number of solutions first exceeds one million.

import math;
import sys;
import time;

start_time = time.time();

def print_execution_time():
    print "Execution time = %f seconds." % (time.time() - start_time);

def is_square(n):
    return (int(math.sqrt(n)) ** 2) == n;

# The solution to the general problem of finding the distance from S to F is illustrated by unfolding the sides of the room as if it were a cardboard box formed by folding along the edges of this familar pattern:
#
#           +---------------------------+
#           |                           |
#           |                           |
#           |                           |
#   +-------+---------------------------+-------+
#   |       |                         . |       |
#   |       |                      .    |       |
#   |       |                   .       | b     |
#   |       |           d    .          |       |
#   |       |             .             |       |
#   +-------+----------+----------------+-------+
#           |       .                   |
#           |    .                      | c
#           | .                         |
#           +---------------------------+
#           |             a             |
#           |                           |
#           |                           |
#           |                           |
#           |                           |
#           +---------------------------+
#
# By the Pythagorean theorem, d (distance) = a^2 + (b + c)^2.
#
# That d is minimal when a >= b and a >= c is shown by the following:
#     a >= b,     a >= c
#    ac >= bc,   ab >= bc
#   2ac >= 2bc, 2ab >= 2bc
# Add a^2 + b^2 + c^2 to each side:
#   a^2 + 2ac + c^2 + b^2 >= a^2 + b^2 + 2bc + c^2, a^2 + 2ab + b^2 + c^2 >= a^2 + b^2 + 2bc + c^2
#   (a + c)^2 + b^2 >= a^2 + (b + c)^2, (a + b)^2 + c^2 >= a^2 + (b + c)^2
#   distance crossing b >= distance crossing a, distance crossing c >= distance crossing a

TARGET = 1000000;

# solution_count_slow = 0;
solution_count = 0;
M = 0;
while solution_count < TARGET:
    M += 1;
    a = M;
    '''
    # This is too slow for the actual target, but can show patterns with a smaller target.
    print;
    for b in range(1, a + 1):
        for c in range(1, b + 1):
            distance = (a ** 2) + ((b + c) ** 2);
            if is_square(distance):
                solution_count_slow += 1;
                # print "%d^2 + (%d + %d)^2 = %d" % (a, b, c, distance);
    print "solution_count_slow = %d @ M = %d." % (solution_count_slow, M);
    '''
    for b_plus_c in range(2, (2 * a) + 1):
        distance = (a ** 2) + (b_plus_c ** 2);
        if is_square(distance):
            # If b and c were not bounded, the number of different combinations of b and c would be (b_plus_c + 1) / 2.
            # But b and c are bounded by M, so the upper limit of c (remember c <= b) is the lesser of M and b_plus_c = 1.
            # The lower limit of c is (b_plus_c + 1) / 2.
            # So the number of solutions is the upper limit minus the lower limit plus 1:
            solution_count += min(b_plus_c - 1, M) - ((b_plus_c + 1) / 2) + 1;
            # print "%d^2 + %d^2 = %d" % (a, b_plus_c, distance);
    print "solution_count = %d @ M = %d." % (solution_count, M);
print;

print_execution_time();
