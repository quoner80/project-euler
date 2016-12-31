# Almost equilateral triangles
# Problem 94
#
# It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the almost equilateral triangle 5-5-6 has an area of 12 square units.
#
# We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.
#
# Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).

import math;
import time;

start_time = time.time();

N = 1000000000;
# N = 1000000;

def print_execution_time():
    print "Execution time = %f seconds." % (time.time() - start_time);

# This brute force approach is a bit slow (669 seconds) but produces the correct solution.
#
# There are 2 cases: the third side = s+1 and = s-1:
#
#   case 1:         case 2:
#         .               .
#        /|\             /|\ 
#       / | \           / | \
#    c /  |h \ c     c /  |h \ c
#     /   |   \       /   |   \
#    /    |    \     /    |    \ 
#   +-----+-----+   +-----+-----+
#   | c+1 | c+1 |   | c-1 | c-1 |
#   | --- | --- |   | --- | --- |
#   |  2  |  2  |   |  2  |  2  |   
#
# The height is smaller when the third side is larger, and vice-versa:
#
#   case 1: small height = sqrt[c^2 - ([c+1]/2)^2] = sqrt(c^2 - [c^2 + 2*c + 1]/4) = [sqrt(3*c^2 - 2*c - 1)] / 2
#   case 2: large height = sqrt[c^2 - ([c-1]/2)^2] = sqrt(c^2 - [c^2 - 2*c + 1]/4) = [sqrt(3*c^2 + 2*c - 1)] / 2
#
# The area of each right tringle is base * height / 2. Since the main tringle comprises 2 right triangles, its area is:
#
#   case 1: [(c + 1) / 2] * [sqrt(3*c^2 - 2*c - 1)] / 2 = [(c + 1) * sqrt(3*c^2 - 2*c - 1)] / 4
#   case 2: [(c - 1) / 2] * [sqrt(3*c^2 + 2*c - 1)] / 2 = [(c + 1) * sqrt(3*c^2 + 2*c - 1)] / 4
#
perimeter_sum = 0;
c_max = (N / 3) + 1;
for c in range(3, c_max, 2):
    three_c_squared_minus_1 = (3 * c * c) - 1;
    two_c = 2 * c;
    small = three_c_squared_minus_1 - two_c;
    large = three_c_squared_minus_1 + two_c;
    small_sqrt = int(math.sqrt(small));
    if (small_sqrt * small_sqrt) == small:
        perimeter = (3 * c) + 1;
        perimeter_sum += perimeter;
        area = small_sqrt * (c - 1.0) / 4;
        is_area_integral = area == int(area);
        print c, c + 1, is_area_integral, perimeter;
    large_sqrt = int(math.sqrt(large));
    if (large_sqrt * large_sqrt) == large:
        perimeter = (3 * c) - 1;
        perimeter_sum += perimeter;
        area = large_sqrt * (c + 1.0) / 4;
        is_area_integral = area == int(area);
        print c, c - 1, is_area_integral, perimeter;
print;
print "perimeter_sum = %d." % perimeter_sum;
print;

print_execution_time();
