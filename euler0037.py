# Truncatable primes
#
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

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

N = 11;

truncatable_prime_count = 0;
truncatable_prime_sum = 0;
for n in range(10, prime_max + 1):
    is_truncatable_prime = False;
    if sieve[n]:
        is_truncatable_prime = True;
        s = str(n);
        length = len(s);
        for i in range(1, length):
            if not sieve[int(s[i : ])]:
                is_truncatable_prime = False;
                break;
        if is_truncatable_prime:
            for i in range(1, length):
                if not sieve[int(s[0 : i])]:
                    is_truncatable_prime = False;
                    break;
        if is_truncatable_prime:
            truncatable_prime_count += 1;
            truncatable_prime_sum += n;
            print n;
    if truncatable_prime_count >= N:
        break;
print "truncatable_prime_count = %d." % truncatable_prime_count;
print "truncatable_prime_sum = %d." % truncatable_prime_sum;

print "Execution time = %f seconds." % (time.time() - start_time);
