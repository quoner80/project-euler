# Digit fifth powers
#
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#    1634 = 1^4 + 6^4 + 3^4 + 4^4
#    8208 = 8^4 + 2^4 + 0^4 + 8^4
#    9474 = 9^4 + 4^4 + 7^4 + 4^4
#
# As 1 = 1^4 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

import time;

start_time = time.time();

N = 5;

# 9^5 * 4 = 236196 (6 digits > 4 digits)
# 9^5 * 5 = 295245 (6 digits > 5 digits)
# 9^5 * 6 = 354294 (6 digits = 6 digits)
# 9^5 * 7 = 413343 (6 digits < 7 digits)
# So the maximum possible value for the number/sum is 9^5 * 6.
MAX_DIGITS = 6;
MAX_VALUE = (9 ** N) * MAX_DIGITS;

count = 0;
aggregate_sum = 0;
for n in range(1, MAX_VALUE + 1):
    s = "{number:0{width}}".format(number = n, width = MAX_DIGITS);
    sum = 0;
    for i in range(MAX_DIGITS):
        sum += int(s[i]) ** N;
    # Check for MAX_DIGITS - 1 or more 0's to exclude single digit non-sums.
    if (sum == n) and (s.count("0") < (MAX_DIGITS - 1)):
        count += 1;
        aggregate_sum += sum;
        print "%s = %s^%d + %s^%d + %s^%d + %s^%d + %s^%d + %s^%d." % (s, s[0], N, s[1], N, s[2], N, s[3], N, s[4], N, s[5], N);
print "Total count = %d." % count;
print "Aggregate sum = %d." % aggregate_sum;

print "Execution time = %f seconds." % (time.time() - start_time);
