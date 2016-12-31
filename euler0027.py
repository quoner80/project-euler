# Quadratic primes
#
# Euler discovered the remarkable quadratic formula:
#   n^2 + n + 41
#
# It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.
#
# The incredible formula  n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, -79 and 1601, is -126479.
#
# Considering quadratics of the form:
#   n^2 + an + b, where |a| < 1000 and |b| < 1000
#
#   where |n| is the modulus/absolute value of n
#   e.g. |11| = 11 and |-4| = 4
#
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

import sys;
import time;

start_time = time.time();

# N = 1605;
N = 1000;

# Read the primes from a file, and initialize the Sieve of Eratosthenes.
primes = [];
infile = open("primes.txt", "r");
for line in infile:
    primes.append(int(line));
infile.close();
prime_count = len(primes);
prime_max = primes[-1];
print "known prime count = %d" % prime_count;
print "known prime max   = %d" % prime_max;
sieve = [False] * (prime_max + 1);
for prime in primes:
    sieve[prime] = True;

max_n = 0;
a_max_n = 0;
b_max_n = 0;
for a in range(-N + 1, N):
    for b in range(-N + 1, N):
        n = 0;
        while True:
            x = (n * n) + (a * n) + b;
            if x > prime_max:
                print "The program failed due to insufficiently large primes table." % n;
                sys.exit(-1);
            if x < 0 or not sieve[x]:
                break;
            # print "%d^2 + %d * %d + %d = %d (prime)." % (n, a, n, b, x);
            n += 1;
        if n > max_n:
            max_n = n;
            a_max_n = a;
            b_max_n = b;
print "a = %d, b = %d, n = %d; a * b = %s." % (a_max_n, b_max_n, max_n, a_max_n * b_max_n);

print "Execution time = %f seconds." % (time.time() - start_time);
