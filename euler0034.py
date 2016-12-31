# Digit factorials
#
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

#    f(999,999) = 6 * 9! = 2,177,280
#  f(9,999,999) = 7 * 9! = 2,540,160
# f(99,999,999) = 8 * 9! = 2,903,040
# So n = 9,999,999 is an upper limit since n > f(n) and n grows faster than f(n).

import time;

N = 10000000;
# N = 1000;

start_time = time.time();

sum = 0;
factorials = [1] * 10;
for i in range(2, len(factorials)):
    factorials[i] = i * factorials[i - 1];
print "factorials table: %s" % factorials;
for n in range(10, N):
    s = str(n);
    factorial_sum = 0;
    for i in range(len(s)):
        factorial_sum += factorials[int(s[i])];
    if n == factorial_sum:
        sum += n;
        print n;
print "sum of all qualifying numbers = %d." % sum;

print "Execution time = %f seconds." % (time.time() - start_time);
