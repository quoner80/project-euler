# Square root digital expansion
#
# It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.
#
# The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.
#
# For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.

import math;
import decimal;
import time;

start_time = time.time();

DIGIT_COUNT = 100;
N = 100;

def get_digit_sum(string):
    digit_sum = 0;
    for c in string:
        if c.isdigit():
            digit_sum += int(c);
    return digit_sum;

non_square_count = 0;
digit_sum = 0;
for n in range(N):
    if (int(math.sqrt(n)) ** 2) != n:
        non_square_count += 1;
        decimal.getcontext().prec = 102;
        digits = str(decimal.Decimal(n).sqrt());
        # Add 1 to compensate for the decimal point.
        digits = digits[: DIGIT_COUNT + 1];
        digit_sum += get_digit_sum(digits);
print "non_square_count = %d." % non_square_count;
print "digit_sum = %d." % digit_sum;

print;
print "Execution time = %f seconds." % (time.time() - start_time);
