# Consecutive prime sum
#
# The prime 41, can be written as the sum of six consecutive primes:
#   41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

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

N = 1000;
N = 1000000;

max_terms = 0;
i_start = 0;
while primes[i_start] < N:
    i_offset = 0;
    prime_sum = 0;
    while prime_sum < N:
        prime_sum += primes[i_start + i_offset];
        i_offset += 1;
        if sieve[prime_sum]:
            if i_offset > max_terms:
                max_terms = i_offset;
                print "%d = %d + ... + %d (%d terms)." % (prime_sum, primes[i_start], primes[i_start + i_offset - 1], i_offset);
    i_start += 1;

print "Execution time = %f seconds." % (time.time() - start_time);
