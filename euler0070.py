# Totient permutation
#
# Euler's Totient function, phi(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, phi(9)=6.
# The number 1 is considered to be relatively prime to every positive number, so phi(1)=1.
#
# Interestingly, phi(87109)=79180, and it can be seen that 87109 is a permutation of 79180.
#
# Find the value of n, 1 < n < 10^7, for which phi(n) is a permutation of n and the ratio n/phi(n) produces a minimum.

import sys;
import time;

start_time = time.time();

N = 10 ** 7;

# Read the primes from a file, and initialize the Sieve of Eratosthenes.
primes = [];
infile = open("primes_below_10_million.txt", "r");
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

minimum_ratio = sys.maxint;
argmin_n = None;
for n in range(2, N):
    totient = get_totient(n);
    ratio = float(n) / totient;
    if sorted(str(n)) == sorted(str(totient)):
        print n, totient, ratio;
        if ratio < minimum_ratio:
            minimum_ratio = ratio;
            argmin_n = n;
print "minimum_ratio = %f, argmin_n = %d." % (minimum_ratio, argmin_n);

print;
print "Execution time = %f seconds." % (time.time() - start_time);
