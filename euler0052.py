# Permuted multiples
#
# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
#
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

import math;
import time;

start_time = time.time();

x1 = 0;
found = False;
while not found:
    x1 += 1;
    x6 = 6 * x1;
    # if x1 and x6 are the same magnitude, then the others will have the same length as well.
    if (int(math.log10(x1)) == int(math.log10(x6))):
        x1_elements = sorted(list(str(x1)));
        x6_elements = sorted(list(str(x6)));
        if (x1_elements == x6_elements):
            x2 = x1 + x1;
            x2_elements = sorted(list(str(x2)));
            if (x1_elements == x2_elements):
                x3 = x2 + x1;
                x3_elements = sorted(list(str(x3)));
                if (x1_elements == x3_elements):
                    x4 = x3 + x1;
                    x4_elements = sorted(list(str(x4)));
                    if (x1_elements == x4_elements):
                        x5 = x4 + x1;
                        x5_elements = sorted(list(str(x5)));
                        if (x1_elements == x5_elements):
                            print x1, x2, x3, x4, x5, x6;
                            found = True;
# print 1.0 / 7.0;
print "Execution time = %f seconds." % (time.time() - start_time);
