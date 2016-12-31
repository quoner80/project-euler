# Spiral primes
#
# Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.
#
#   37 36 35 34 33 32 31
#   38 17 16 15 14 13 30
#   39 18  5  4  3 12 29
#   40 19  6  1  2 11 28
#   41 20  7  8  9 10 27
#   42 21 22 23 24 25 26
#   43 44 45 46 47 48 49
#
# It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ~ 62%.
#
# If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

# From euler0028.py, but anticlockwise instead of clockwise (same result by symmetry):
#
# N = 7:
#
#   37 36 35 34 33 32 31
#   38 17 16 15 14 13 30
#   39 18  5  4  3 12 29
#   40 19  6  1  2 11 28
#   41 20  7  8  9 10 27
#   42 21 22 23 24 25 26
#   43 44 45 46 47 48 49
#
#   NW to SW Diagonal (excluding 1): 37, 17, 5, 9, 25, 49
#   SW to NE Diagonal (excluding 1): 43, 21, 7, 3, 13, 31
#
#   Sorted:
#   NW to SW Diagonal: 5, 9, 17, 25, 37, 49
#   SW to NE Diagonal: 3, 7, 13, 21, 31, 43
#
#   NW to SW Diagonal:
#   5, 9, 17, 25, 37, 49
#   (1 + 4), (0 + 9), (1 + 16), (0 + 25), (1 + 36), (0 + 49)
#   n = 2 to N: 1 + n^2 if n even, n^2 if n odd
#
#   SW to NE Diagonal:
#   3, 7, 13, 21, 31, 43
#   (1 + 2), (1 + 6), (1 + 12), (1 + 20), (1 + 30), (1 + 42)
#   (1 + (2 * 1)), (1 + (2 * 3)), (1 + (2 * 6)), (1 + (2 * 10)), (1 + (2 * 15)), (1 + (2 * 21))
#   (1 + (2 * T[1])), (1 + (2 * T[2])), (1 + (2 * T[3])), (1 + (2 * T[4])), (1 + (2 * T[5])), (1 + (2 * T[6])) where T[n] is the nth triangular number
#   n = 1 to N - 1: (1 + (2 * T[n]))
#   T[n] = n * (n + 1) / 2:
#   n = 1 to N - 1: (1 + (n * (n + 1)))

import math;
import sys;
import time;

start_time = time.time();

RATIO_THRESHOLD = 0.10;

def is_prime(n):
    is_n_prime = True;
    global primes;
    global prime_max;
    prime_factor_max = int(math.ceil(math.sqrt(n)));
    if prime_factor_max > prime_max:
        print "is_prime(%d) failed due to insufficiently large primes table." % n;
        sys.exit(-1);
    for p in primes:
        if p >= n:
            break;
        if n % p == 0:
            is_n_prime = False;
            break;
    return is_n_prime;

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

side_length = 1;   # Start with one element--the 1 in the center.
element_count = 1; # ibid.
prime_count = 0;   # 1 is not considered prime.
ratio = float(prime_count) / element_count;
while True:
    # Process 2 steps of side_length at a time since side_length must be odd after each processing step.
    for i in range(2):
        n = side_length + 1;

        # NW to SW Diagonal:
        element = n * n;
        # No need to check if element is prime if n is odd since element is a perfect square.
        if n % 2 == 0:
            element += 1;
            if is_prime(element):
                prime_count += 1;
        element_count += 1;
        # print element, prime_count, element_count;

        # SW to NE Diagonal:
        element = 1 + ((n - 1) * n);
        if is_prime(element):
            prime_count += 1;
        element_count += 1;
        # print element, prime_count, element_count;
        
        side_length += 1;
        i += 1;
    ratio = float(prime_count) / element_count;
    print ratio;
    if ratio < RATIO_THRESHOLD:
        break;
print "A square spiral with side length %d has a diagonal prime ratio of %f (smallest square spiral with ratio < %f)." % (side_length, ratio, RATIO_THRESHOLD);

print "Execution time = %f seconds." % (time.time() - start_time);
