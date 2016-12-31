# Summation of primes
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

max_possible_prime = 2000000;

# Initialize the sieve of Eratosthenes.
sieve = range(max_possible_prime + 1);
prime = 2;
print prime;
prime_sum = prime;
while True:
    # Use the current prime to zero out its multiples.
    for prime_multiple in range(prime * 2, max_possible_prime + 1, prime):
        sieve[prime_multiple] = 0;
    # Find the next prime.
    i = prime + 1;
    while i <= max_possible_prime:
        if sieve[i] != 0:
            prime = i;
            print prime;
            prime_sum += prime;
            break;
        i += 1;
    # Main loop exit criterion.
    if i >= max_possible_prime:
        break;
print "sum of primes below %d = %d" % (max_possible_prime, prime_sum);
