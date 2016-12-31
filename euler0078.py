# Coin partitions
#
# Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.
#
#      OOOOO
#     OOOO  O
#     OOO  OO
#    OOO  O  O
#    OO  OO  O
#   OO  O  O  O
#  O  O  O  O  O
#
# Find the least value of n for which p(n) is divisible by one million.

import time;

start_time = time.time();

N = 1000000;

# Hardy, Godfrey & Wright, Edward, An Introduction To The Theory Of Numbers, 4th Edition:
#   (19.10.2) p(n) - p(n-1) - p(n-2) + p(n-5) + ... + [(-1)^k * p{n-(1/2)k(3k-1)}] + [(-1)^k * p{n-(1/2)k(3k+1)}] + ... = 0
#             p(n) = p(n-1) + p(n-2) - p(n-5) - ... + [(-1)^(k+1) * p{n-(1/2)k(3k-1)}] + [(-1)^(k+1) * p{n-(1/2)k(3k+1)}] + ...
# Note that p(n) includes n itself, unlike how the number of ways is defined in this problem, which is describing p(n) - 1.
# That is, p(5) = 7 (not 6), and p(1) = 1 (not 0).
# Note also that by convention, p(0) = 1.
p = [1];
n = 0;
while True:
    n += 1;
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
    print "p[%d] = %d." % (n, summation_count);
    p.append(summation_count);
    if summation_count % N == 0:
        print "p[%d] = %d." % (n, summation_count);
        break;
print "p[%d] is the first p[n] divisible by %d." % (n, N);

print;
print "Execution time = %f seconds." % (time.time() - start_time);
