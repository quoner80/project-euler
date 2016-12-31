# Goldbach's other conjecture
#
# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
#  9 =  7 + 2 x 1^2
# 15 =  7 + 2 x 2^2
# 21 =  3 + 2 x 3^2
# 25 =  7 + 2 x 3^2
# 27 = 19 + 2 x 2^2
# 33 = 31 + 2 x 1^2
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

import math;
import sys;
import time;

start_time = time.time();

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

x = 1;
while True:
    x += 2; # odd numbers only
    if sieve[x]:
        continue;
    qualifies = False;
    for n in range(1, int(math.sqrt(x / 2)) + 1):
        prime_candidate = x - (2 * n * n);
        if prime_candidate > prime_max:
            print "Program failed due to insufficiently large primes table (%d > %d)." % (prime_candidate, prime_max);
            sys.exit(-1);
        if sieve[prime_candidate]:
            qualifies = True;
            print "%d = %d + 2 x %d^2." % (x, prime_candidate, n);
            break;
    if qualifies:
        continue;
    print "%d cannot be written as the sum of a prime and twice a square." % x;
    break;

print "Execution time = %f seconds." % (time.time() - start_time);
