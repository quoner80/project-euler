# Circular primes
#
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

import time;

N = 200;
N = 1000000;

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

circular_prime_count = 0;
for n in range(2, N):
    s = str(n);
    is_circular_prime = True;
    for i in range(len(s)):
        if not sieve[int(s)]:
            is_circular_prime = False;
            break;
        s = s[1:] + s[0];
    if is_circular_prime:
        circular_prime_count += 1;
        print n;
print "Total number of circular primes below %d = %d." % (N, circular_prime_count);

print "Execution time = %f seconds." % (time.time() - start_time);
