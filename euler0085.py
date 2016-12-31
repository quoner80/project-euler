# Counting rectangles
# Problem 85
#
# By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:
#
#   +-+-+-+   +-+-+-+   +-+-+-+
#   |x| | |   |x|x| |   |x|x|x|
#   +-+-+-+   +-+-+-+   +-+-+-+
#   | | | |   | | | |   | | | |
#   +-+-+-+   +-+-+-+   +-+-+-+
#      6         4         2
#
#   +-+-+-+   +-+-+-+   +-+-+-+
#   |x| | |   |x|x| |   |x|x|x|
#   +-+-+-+   +-+-+-+   +-+-+-+
#   |x| | |   |x|x| |   |x|x|x|
#   +-+-+-+   +-+-+-+   +-+-+-+
#      3         2         1
#
# Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.

import math;
import time;
import sys;

start_time = time.time();

TARGET = 2000000;

# m x n
#
# 1 x 1: m x n         rectangles
# 1 x 2: m x (n-1)     rectangles
# 2 x 1: (m-1) x n     rectangles
# 2 x 2: (m-1) x (n-1) rectangles
# ...
# m x n: 1             rectangle
# ========================================================
# sum(r=[1,m] sum(c=[1,n] {(m-r+1) x (n-c+1)})) rectangles
#   = sum(r=[0,m-1] sum(c=[0,n-1] {(m-r) x (n-c)}))
#   = sum(r=[0,m-1] sum(c=[0,n-1] {mn + rc - mc - nr}))
#   = m * n * mn + sum(r=[0,m-1] sum(c=[0,n-1] {rc})) - (m * m * sum(r=[0,n-1]{c})) - (n * n * sum(r=[0,m-1]{r}))
# From https://en.wikipedia.org/wiki/Summation, a summation of products equals the product of the summations:
#   = m * n * mn + sum(r=[0,m-1]{r} * sum(c=[0,n-1]{c}) - (m * m * sum(r=[0,n-1]{c})) - (n * n * sum(r=[0,m-1]{r}))
# A sum of a series equals one half the first term plus the last term times the number of terms:    
#   = m * n * mn + (((m-1) * m / 2) * ((n-1 * n / 2))) - (m * m * (n-1) * n / 2) - (n * n * (m-1) * m / 2)
#   = (m^2 * n^2) + ((mn * (m-1) * (n-1)) / 4) - ((m^2 * n^2 - m^2 * n) / 2) - ((m^2 * n^2 - m * n^2) / 2)
#   = (m^2 * n^2) + ((mn - m - n - 1) / 4)- ((m^2 * n^2 - m^2 * n) / 2) - ((m^2 * n^2 - m * n^2) / 2)
#   = (m^2 * n^2) + ((mn - m - n - 1) / 4)- ((m^2 * n^2 - m^2 * n) / 2) - ((m^2 * n^2 - m * n^2) / 2)
#   = (1 + 1/4 - 1/2 - 1/2)(m^2 * n^2) + (-1/4 + 1/2)(m^2 * n) + (-1/4 + 1/2)(m * n^2) + (1/4)(mn)
#   = (1/4)(m^2 * n^2) + (1/4)(m^2 * n) + (1/4)(m * n^2) + (1/4)(mn)
#   = (1/4)((m^2 * n^2) + (m^2 * n) + (m * n^2) + (mn))
#   = (1/4)((m^2 + m) * (n^2 + n))
#   = (1/4)(m * (m + 1) * n * (n + 1))
minimum_difference = sys.maxint;
minimum_difference_m = 0;
minimum_difference_n = 0;
minimum_difference_area = 0;
m = 0;
while True:
    m += 1;
    # From the second-to-last equation above:
    #   (1/4)((m^2 + m) * (n^2 + n)) = TARGET
    #   (1/4)((n^2 + n * (m^2 + m))) = TARGET
    #   (n^2 + n * (m^2 + m)) = 4 * TARGET
    #   n^2 + n = 4 * TARGET / (m^2 + m)
    #   n^2 + n - 4 * TARGET / (m^2 + m) = 0
    # Solve for n:
    #   n = (-1 +/- sqrt(1^2 + (4 * 4 * TARGET / (m^2 + m)))) / 2
    #   n = (+/- sqrt(1 + (16 * TARGET / (m * (m + 1)))) - 1) / 2
    # Take only the positive solution:
    #   n = (sqrt(1 + (16 * TARGET / (m * (m + 1)))) - 1) / 2
    n_fractional = (math.sqrt(1 + (16.0 * TARGET / (m * (m + 1)))) - 1) / 2;
    n = int(round(n_fractional));
    rectangle_count = m * (m + 1) * n * (n + 1) / 4;
    difference = abs(rectangle_count - TARGET);
    if difference < minimum_difference:
        minimum_difference = difference;
        minimum_difference_m = m;
        minimum_difference_n = n;
        minimum_difference_area = m * n;
    print "m = %4d, n = %4d, rectangles = %7d, difference = %7d." % (m, n, rectangle_count, difference);
    if n_fractional < 1.0:
        break;
print;
print "minimum_difference = %d, m = %d, n = %d, area = %d" % (minimum_difference, minimum_difference_m, minimum_difference_n, minimum_difference_area);
print;

print "Execution time = %f seconds." % (time.time() - start_time);
