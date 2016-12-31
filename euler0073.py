# Counting fractions in a range
#
# Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
#
# If we list the set of reduced proper fractions for d <= 8 in ascending order of size, we get:
#
#   1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
#
# It can be seen that there are 3 fractions between 1/3 and 1/2.
#
# How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d <= 12,000?

import math;
import sys;
import time;

start_time = time.time();

# DENOMINATOR_MAX = 8;
DENOMINATOR_MAX = 12000;

def get_gcd(a, b):
    r = a % b;
    while r != 0:
        a = b;
        b = r;
        r = a % b;
    return b;

TARGET_NUMERATOR_LOW    = 1;
TARGET_DENOMINATOR_LOW  = 3;
TARGET_FRACTION_LOW     = float(TARGET_NUMERATOR_LOW) / TARGET_DENOMINATOR_LOW;
TARGET_NUMERATOR_HIGH   = 1;
TARGET_DENOMINATOR_HIGH = 2;
TARGET_FRACTION_HIGH    = float(TARGET_NUMERATOR_HIGH) / TARGET_DENOMINATOR_HIGH;

count = 0;
for denominator in range(2, DENOMINATOR_MAX + 1):
    # Print a progress indication.
    if denominator % 100 == 0:
        print "completed %d of %d" % (denominator, DENOMINATOR_MAX);
    numerator_low = int(math.ceil(denominator * TARGET_FRACTION_LOW));
    # If numerator_low / denominator == TARGET_NUMERATOR_LOW / TARGET_DENOMINATOR_LOW exactly, test the next larger
    # numerator_low.
    if (numerator_low * TARGET_DENOMINATOR_LOW) == (denominator * TARGET_NUMERATOR_LOW):
        numerator_low += 1;
    numerator_high = int(denominator * TARGET_FRACTION_HIGH);
    # If numerator_high / denominator == TARGET_NUMERATOR_HIGH / TARGET_DENOMINATOR_HIGH exactly, test the next smaller
    # numerator_high.
    if (numerator_high * TARGET_DENOMINATOR_HIGH) == (denominator * TARGET_NUMERATOR_HIGH):
        numerator_high -= 1;
    # If numerator_low > numerator_high, there are no qualifying fractions for this denominator.
    if numerator_low <= numerator_high:
        for numerator in range(numerator_low, numerator_high + 1):
            # Because all the denominators from 2 to N are included, any non-reduced fraction would reduce to a fraction
            # already counted in the list for a smaller denominator. It therefore suffices to count the number of already
            # reduced fractions for each denominator.
            if get_gcd(numerator, denominator) == 1:
                count += 1;
print;
print "number of reduced fractions = %d." % count;

print;
print "Execution time = %f seconds." % (time.time() - start_time);
