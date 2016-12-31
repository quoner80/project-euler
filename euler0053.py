# Combinatoric selections
#
# There are exactly ten ways of selecting three from five, 12345:
#   123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
#
# In combinatorics, we use the notation, 5C3 = 10.
#
# In general,
#   nCr = n! / (r! * (n-r)!), where r <= n, n! = n * (n-1) * ... * 3 * 2 * 1, and 0! = 1.
#
# It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
#
# How many, not necessarily distinct, values of nCr, for 1 <= n <= 100, are greater than one-million?

import math;
import time;
# import sys;

start_time = time.time();

M = 100;
N = 1000000;

def get_combinations(n, r):
    return math.factorial(n) / (math.factorial(n - r) * math.factorial(r));

count = 0;
for n in range(1, M + 1):
    for r in range(n + 1):
        # sys.stdout.write(str(get_combinations(n, r)) + " ");
        if get_combinations(n, r) > N:
            # Since the list from 0 to n is symmetrical, as soon as one value > N is found, the total can be calculated as the list
            # size minus 2 * r. (Since r is 0-based, and this is the first r | nCr > N, it's really 2 * (r - 1 + 1) == 2 * r.)
            count += (n + 1) - (2 * r);
            break;
print count;

print "Execution time = %f seconds." % (time.time() - start_time);
