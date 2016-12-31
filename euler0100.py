# Arranged probability
# Problem 100
#
# If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)x(14/20) = 1/2.
#
# The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.
#
# By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.

import math;
import time;

start_time = time.time();

def print_execution_time():
    print "Execution time = %f seconds." % (time.time() - start_time);

def is_perfect_square(n):
    return (int(math.sqrt(n)) ** 2) == n;

"""
# This code produces the following output.
total = 2;
y = 0;
while (True):
    if is_perfect_square((2 * total * (total - 1)) + 1):
        x = ((2 * total * (total - 1)) + 1);
        last_y = y;
        y = int(math.sqrt(x));
        if last_y > 0:
            print "%10d, %10d, %.16f, %.16f " % (last_y, y, float(last_y) / y, y / float(last_y));
    total += 1;
"""
"""
See above. Note that the ratio of y / last_y = 3 + 2 * sqrt(2). Whoa!
         5,         29, 0.1724137931034483, 5.7999999999999998
        29,        169, 0.1715976331360947, 5.8275862068965516
       169,        985, 0.1715736040609137, 5.8284023668639051
       985,       5741, 0.1715728967078906, 5.8284263959390863
      5741,      33461, 0.1715728758853591, 5.8284271032921096
     33461,     195025, 0.1715728752724010, 5.8284271241146408
    195025,    1136689, 0.1715728752543572, 5.8284271247275994
   1136689,    6625109, 0.1715728752538260, 5.8284271247456427
   6625109,   38613965, 0.1715728752538104, 5.8284271247461739
  38613965,  225058681, 0.1715728752538099, 5.8284271247461898
 225058681, 1311738121, 0.1715728752538099, 5.8284271247461898
"""

TARGET = 10 ** 12;
RATIO = 3 + (2 * math.sqrt(2));
y = 5;
total = 0;
blue = 0;
while total <= TARGET:
    y = int(round(y * RATIO));
    total = int(math.sqrt(((y ** 2) - 1) / 2)) + 1;
    blue = int((1 + math.sqrt((2 * total * (total - 1)) + 1)) / 2);
    print "(%d/%d)x(%d/%d) = %.10f." % (blue, total, blue - 1, total - 1, (float(blue) / total) * (float(blue - 1) / (total - 1)));
print;
print "%d blues, %d reds, %d total." % (blue, total - blue, total);
print;

print_execution_time();
