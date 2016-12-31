# Totient maximum
#
# Euler's Totient function, phi(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, phi(9) = 6.
#
#   n   Relatively Prime    phi(n)      n/phi(n)
#   2   1                   1           2
#   3   1, 2                2           1.5
#   4   1, 3                2           2
#   5   1, 2, 3, 4          4           1.25
#   6   1, 5                2           3
#   7   1, 2, 3, 4, 5, 6    6           1.1666...
#   8   1, 3, 5, 7          4           2
#   9   1, 2, 4, 5, 7, 8    6           1.5
#   10  1, 3, 7, 9          4           2.5
#
# It can be seen that n = 6 produces a maximum n/phi(n) for n <= 10.
#
# Find the value of n <= 1,000,000 for which n/phi(n) is a maximum.

import time;

start_time = time.time();

N = 1000000;

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

# Returns the prime factorization of n as a list of 2-tuples [p, m] where p is the prime factor and m is the multiplicity of
# that prime factor. For example, if n is 2000, the prime factorization is [[2, 4], [5, 3]] since 2000 = 2^4 * 5^3.
def get_prime_factorization(n):
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

# phi(n) = n * PI(1 - 1/p_i) where PI(1 - 1/p_i) is the product of all (1 - 1/p_i) where p_i is each prime factor of n.
# phi(n) = PI[p_i^k_i] * PI[(p_i - 1) / p_i]
# phi(n) = PI[p_i^(k_i - 1)] * PI[(p_i - 1)]
def get_totient(n):
    totient = 1;
    prime_factorization = get_prime_factorization(n);
    for p_k in prime_factorization:
        p = p_k[0];
        k = p_k[1];
        totient *= (p ** (k - 1)) * (p - 1);
    return totient;

max_n_over_totient = 0;
argmax_n = None;
for n in range(2, N + 1):
    totient = get_totient(n);
    n_over_totient = float(n) / totient;
    # print n, totient, n_over_totient;
    if n_over_totient > max_n_over_totient:
        max_n_over_totient = n_over_totient;
        argmax_n = n;
print "max(n/totient) = %f, argmax_n = %d" % (max_n_over_totient, argmax_n);

print;
print "Execution time = %f seconds." % (time.time() - start_time);
