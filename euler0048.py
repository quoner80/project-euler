# Self powers
#
# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
#
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

import time;

start_time = time.time();

N = 1000;

self_power_sum = 0;
for i in range(1, N + 1):
    self_power_sum += (i ** i);
print self_power_sum;
print str(self_power_sum)[-10:];

print "Execution time = %f seconds." % (time.time() - start_time);
