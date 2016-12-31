# Reciprocal cycles
#
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
# 1/2  = 0.5
# 1/3  = 0.(3)
# 1/4  = 0.25
# 1/5  = 0.2
# 1/6  = 0.1(6)
# 1/7  = 0.(142857)
# 1/8  = 0.125
# 1/9  = 0.(1)
# 1/10 = 0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

import decimal;
import math;
import sys;
import time;

N = 1000;

def process_one_over_n(n):
    period = 0;
    # Get n * 6 digits of the fractional part of which n digits will later be chopped from each end.
    precision = n * 6;
    decimal.getcontext().prec = precision;
    string = str(decimal.Decimal(1.0) / decimal.Decimal(n));
    string = string[2:];
    leading_zeros = 0;
    for i in range(len(string)):
        if string[i] == '0':
            leading_zeros += 1;
        else:
            break;
    if (n > 1) and (leading_zeros != math.floor((math.log10(n - 1)))):
        print "Critical error: The leading zero theory is wrong!"
        sys.exit(-1);
    if len(string) < (precision / 2):
        print "1/%d has no repeating decimal." % n;
    else:
        # Chop n digits off each end to remove any transient (non-repeating prefix) and any rounding inaccuracies.
        string = string[n : len(string) - n];
        is_repeating = False;
        # According to https://en.wikipedia.org/wiki/Repeating_decimal, the period of 1/n for integer n is always <= n - 1.
        for i in range(1, n):
            length = len(string);
            expected_repetend_count = length / i;
            length_to_test = i * expected_repetend_count;
            repetend_count = string[0 : length_to_test].count(string[0 : i]);
            if repetend_count == expected_repetend_count:
                is_repeating = True;
                period = i;
                print "1/%d has a repeating decimal with period %d." % (n, i);
                break;
        if not is_repeating:
            print "Critical error: 1/%d determined to be neither repeating nor non-repeating!" % n;
            sys.exit(-1);
    return period;

start_time = time.time();
max_period = 0;
arg_max_period = 0;
for n in range(1, N):
    period = process_one_over_n(n);
    if period > max_period:
        max_period = period;
        arg_max_period = n;
print;
print "1/%d has the largest repeating decimal period, %d." % (arg_max_period, max_period);
print "Execution time = %f seconds." % (time.time() - start_time);
