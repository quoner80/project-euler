# 10001st prime
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10001st prime number?

N = 10001;
PRIME_CEILING = 110000;

prime_count = 0;
primes = [0] * N;

# Initialize the sieve of Eratosthenes.
sieve = range(PRIME_CEILING + 1);

prime = 2;
while prime_count < N:
    print prime;
    primes[prime_count] = prime;
    prime_count += 1;

    # Use the current prime to zero out its multiples.
    for i in range(prime * 2, PRIME_CEILING + 1, prime):
        sieve[i] = 0;

    # Find the next prime.
    for i in range(prime + 1, PRIME_CEILING + 1):
        if sieve[i] != 0:
            prime = i;
            break;

    # Exit criterion in case PRIME_CEILING is too small.
    if i >= PRIME_CEILING:
        print "%dth prime = %d is the largest determinable. Increase PRIME_CEILING (currently %d)." % (prime_count, prime, PRIME_CEILING);
        break;

print "%dth prime = %d" % (N, primes[N - 1]);
