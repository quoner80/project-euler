# Counting summations
#
# It is possible to write five as a sum in exactly six different ways:
#
#   4 + 1
#   3 + 2
#   3 + 1 + 1
#   2 + 2 + 1
#   2 + 1 + 1 + 1
#   1 + 1 + 1 + 1 + 1
#
# How many different ways can one hundred be written as a sum of at least two positive integers?

import time;

start_time = time.time();

N = 200;
p = [0] * (N + 1);

# Hardy, Godfrey & Wright, Edward, An Introduction To The Theory Of Numbers, 4th Edition:
#   (19.10.2) p(n) - p(n-1) - p(n-2) + p(n-5) + ... + [(-1)^k * p{n-(1/2)k(3k-1)}] + [(-1)^k * p{n-(1/2)k(3k+1)}] + ... = 0
#             p(n) = p(n-1) + p(n-2) - p(n-5) - ... + [(-1)^(k+1) * p{n-(1/2)k(3k-1)}] + [(-1)^(k+1) * p{n-(1/2)k(3k+1)}] + ...
# Note that p(n) includes n itself, unlike how the number of ways is defined in this problem, which is describing p(n) - 1.
# That is, p(5) = 7 (not 6), and p(1) = 1 (not 0).
# Note also that by convention, p(0) = 1.
p[0] = 1;
for n in range(1, N + 1):
    # print n;
    summation_count = 0;
    k = 0;
    while True:
        k += 1;
        sign = 1;
        if k % 2 == 0:
            sign = -1;
        d = k * ((3 * k) - 1) / 2;
        if d > n:
            break;
        summation_count += (sign * (p[n - d]));
        d = k * ((3 * k) + 1) / 2;
        if d > n:
            break;
        summation_count += (sign * (p[n - d]));
    p[n] = summation_count;
if N >= 200:
    print "p[200]     = %d." % p[200]; # p(200) = 3,972,999,029,388 (Macmahon)
if N >= 100:
    print "p[100]     = %d." % p[100];
    print "p[100] - 1 = %d." % (p[100] - 1);

print;
print "Execution time = %f seconds." % (time.time() - start_time);
