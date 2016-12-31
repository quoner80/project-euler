# Generates the list of primes at or below max_possible_prime.

import time;

start_time = time.time();

max_possible_prime = 1000000;
print "max_possible_prime = %d." % max_possible_prime;

# Initialize the sieve of Eratosthenes.
sieve = [True] * (max_possible_prime + 1);

prime = 2;
print prime;
while True:
    # Use the current prime to zero out its multiples.
    for i in range(prime * 2, max_possible_prime + 1, prime):
        sieve[i] = False;
    # Find the next prime.
    for i in range(prime + 1, max_possible_prime + 1):
        if sieve[i] != 0:
            prime = i;
            print prime;
            break;
    # Exit criterion.
    if i >= max_possible_prime:
        break;

print "Execution time = %f seconds." % (time.time() - start_time);
