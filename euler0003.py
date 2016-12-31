# Largest prime factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143?

import math

def get_max_possible_prime(N):
   return int(math.ceil(math.sqrt(N)));

# N = 500003;     # = 7 * 71429
# N = 71429;      # = 71429
# N = 1500009;    # = 3 * 7 * 71429
# N = 4500027;    # = 3 * 3 * 7 * 71429
N = 600851475143; # = 71 * 839 * 1471 * 6857
print "N = %d" % N;
prime_factors = [];
max_possible_prime = get_max_possible_prime(N);
print "max_possible_prime = %d" % max_possible_prime;
print;
# Initialize the sieve of Eratosthenes.
sieve = range(max_possible_prime + 1);
prime = 2;
while True:
    # Use the current prime to zero out its multiples.
    for i in range(prime * 2, max_possible_prime + 1, prime):
        sieve[i] = 0;
    # Find the next prime.
    for i in range(prime + 1, max_possible_prime + 1):
        if sieve[i] != 0:
            prime = i;
            break;
    # Exit criterion.
    if i >= max_possible_prime:
        break;
    # print prime;
    # Factor out the prime as many times as it is a factor of N.
    remaining = N;
    while remaining % prime == 0:
        remaining /= prime;
        prime_factors.append(prime);
        print "prime_factors = %s" % prime_factors;
    # Update N and its max_possible_prime if N changed.
    if N != remaining:
        N = remaining;
        max_possible_prime = get_max_possible_prime(N);
        print "N = %d" % N;
        print "max_possible_prime = %d" % max_possible_prime;
        print;
if (N != 1):
    prime_factors.append(N);
    print "prime_factors = %s" % prime_factors;
