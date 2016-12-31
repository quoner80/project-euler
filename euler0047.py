# Distinct primes factors
#
# The first two consecutive numbers to have two distinct prime factors are:
#   14 = 2 x 7
#   15 = 3 x 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#   644 = 2^2 x 7 x 23
#   645 = 3 x 5 x 43
#   646 = 2 x 17 x 19
#
# Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?

import time;

start_time = time.time();

# Returns the prime factorization of n as a list of 2-tuples [p, m] where p is the prime factor and m is the multiplicity of
# that prime factor. For example, if n is 2000, the prime factorization is [[2, 4], [5, 3]] since 2000 = 2^4 * 5^3.
def get_prime_factorization(n):
    global primes;
    global prime_count;
    global prime_max;
    global sieve;
    # Start with 1 sonce the loop below will not add it.
    prime_factorization = [];
    prime_index = 0;
    prime = primes[prime_index];
    while n > 1:
        if n <= prime_max and sieve[n]:
            # print n;
            prime_factorization.append([n, 1]);
            break;
        prime = primes[prime_index];
        prime_multiplicity = 0;
        while n % prime == 0:
            # print prime;
            prime_multiplicity += 1;
            n /= prime;
        if prime_multiplicity > 0:
            prime_factorization.append([prime, prime_multiplicity]);            
        prime_index += 1;
        if prime_index >= prime_count:
            print "get_prime_factorization(%d) failed due to insufficiently large primes table." % n;
            sys.exit();
    return prime_factorization;

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

N = 4;
x = 2;
consecutive_count = 0;
while True:
    if len(get_prime_factorization(x)) < N:
        consecutive_count = 0;
    else:
        consecutive_count += 1;
    if consecutive_count >= N:
        for i in range(N):
            x_i = x - (N - 1) + i;
            print "%d: %s" % (x_i, str(get_prime_factorization(x_i)));
        break;
    x += 1;

print "Execution time = %f seconds." % (time.time() - start_time);
