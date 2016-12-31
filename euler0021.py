# Amicable numbers
#
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

import sys;

N = 10000;

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

def get_divisors(n):
    divisors = [1];
    prime_factorization = get_prime_factorization(n);
    # print prime_factorization;
    for prime_factors_index in range(len(prime_factorization)):
        prime_factor = prime_factorization[prime_factors_index][0];
        multiplicity = prime_factorization[prime_factors_index][1];
        current_divisors = [];
        for multiplicity_index in range(multiplicity + 1):
            for divisors_index in range(len(divisors)):
                current_divisors.append(divisors[divisors_index] * (prime_factor ** multiplicity_index));
        divisors = list(current_divisors);
        # print prime_factor, multiplicity;
    return sorted(divisors);

def get_proper_divisors(n):
    proper_divisors = get_divisors(n);
    # Remove n itself, which is the final element in the sorted list.
    del proper_divisors[-1];
    return proper_divisors;

def get_proper_divisors_sum(n):
    proper_divisors_sum = 0;
    proper_divisors = get_proper_divisors(n);
    for i in range(len(proper_divisors)):
        proper_divisors_sum += proper_divisors[i];
    return proper_divisors_sum;

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

# print get_proper_divisors_sum(220);
# print get_proper_divisors_sum(284);

amicable_numbers_sum = 0;
proper_divisors_sums = [0] * N;
for n in range(N):
    proper_divisors_sums[n] = get_proper_divisors_sum(n);
for n in range(N):
    m = proper_divisors_sums[n];
    if (m < N) and (m != n) and (proper_divisors_sums[m] == n):
        print "%d and %d are an amicable pair." % (n, m);
        # Add only n because m will be repeated as n in a different iteration (optimization target).
        amicable_numbers_sum += n;
print "total = %d." % amicable_numbers_sum;
