# Prime permutations
#
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?

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

for n1 in range(1000, 10000):
    for separation in range(1, (10000 - n1) / 2):
        n2 = n1 + separation;
        n3 = n2 + separation;
        if sieve[n1] and sieve[n2] and sieve[n3]:
            s1 = sorted(list(str(n1)));
            s2 = sorted(list(str(n2)));
            s3 = sorted(list(str(n3)));
            if (s1 == s2) and (s2 == s3):
                print "%d, (+ %d =) %d, (+ %d =) %d -> %s." % (n1, separation, n2, separation, n3, str(n1) + str(n2) + str(n3));

print "Execution time = %f seconds." % (time.time() - start_time);
