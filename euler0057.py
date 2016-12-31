# Square root convergents
#
# It is possible to show that the square root of two can be expressed as an infinite continued fraction.
#   sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
#
# By expanding this for the first four iterations, we get:
#   1 + 1/2 = 3/2 = 1.5
#   1 + 1/(2 + 1/2) = 7/5 = 1.4
#   1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
#   1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
#
# The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.
#
# In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?

import time;

start_time = time.time();

MAX_EXPANSION_COUNT = 1000;

n = 1;
d = 2;

count = 0;
for i in range(MAX_EXPANSION_COUNT):
    # print i + 1, d + n, d, 1.0 + float(n) / d;
    N = d + n;
    D = d;
    length_N = len(str(N));
    length_D = len(str(D));
    if length_N > length_D:
        count += 1;
        # print i + 1, N, D, length_N, length_D;
    n += 2 * d;
    temp = n;
    n = d;
    d = temp;
print "In the first %d expansions, %d fractions contain a numerator with more digits than denominator." % (MAX_EXPANSION_COUNT, count);

print "Execution time = %f seconds." % (time.time() - start_time);
