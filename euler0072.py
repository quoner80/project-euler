# Counting fractions
#
# Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
#
# If we list the set of reduced proper fractions for d <= 8 in ascending order of size, we get:
#
#   1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
#
# It can be seen that there are 21 elements in this set.
#
# How many elements would be contained in the set of reduced proper fractions for d <= 1,000,000?

import sys;
import time;

start_time = time.time();

# D = 8;
D = 10 ** 6;

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
    prime_factorization = [];
    prime_index = 0;
    prime = primes[prime_index];
    while n > 1:
        if n <= prime_max and sieve[n]:
            prime_factorization.append([n, 1]);
            break;
        prime = primes[prime_index];
        prime_multiplicity = 0;
        while n % prime == 0:
            prime_multiplicity += 1;
            n /= prime;
        if prime_multiplicity > 0:
            prime_factorization.append([prime, prime_multiplicity]);            
        prime_index += 1;
        if prime_index >= prime_count:
            print "get_prime_factorization(%d) failed due to insufficiently large primes table." % n;
            sys.exit();
    return prime_factorization;

def get_gcd(a, b):
    gcd = 1;
    a_factorization = get_prime_factorization(a);
    b_factorization = get_prime_factorization(b);
    b_index = 0;
    b_length = len(b_factorization);
    for a_factor_exponent in a_factorization:
        a_factor = a_factor_exponent[0];
        while (b_index < b_length) and (b_factorization[b_index][0] < a_factor):
            b_index += 1;
        if b_index >= b_length:
            break;
        b_factor_exponent = b_factorization[b_index];
        b_factor = b_factor_exponent[0];
        if b_factor == a_factor:
            gcd_exponent = min(a_factor_exponent[1], b_factor_exponent[1])
            gcd *= (a_factor ** gcd_exponent);
    return gcd;

def get_reduced_fraction(n, d):
    gcd = get_gcd(n, d);
    return (n / gcd, d / gcd);

# Returns the combinations of "count" elements in "array".
# For example, for ([1,2,3,4], 2), returns ([1,2], [1,3], [1,4], [2,3], [2,4], [3,4]).
def get_combinations(array, count):
    combinations = [];
    if count == 1:
        for element in array:
            #print "[element]: " + str([element]);
            combinations.append([element]);
    else:
        for i in range(len(array) - count + 1):
            subcombinations = get_combinations(array[i + 1 : ], count - 1);
            #print "subcombinations: " + str(subcombinations);
            for subcombination in subcombinations:
                #print "[array[i]] + subcombination: " + str([array[i]] + subcombination);
                combinations.append([array[i]] + subcombination);
    return combinations;

# For any fractions less than 1, numerators range from 1 to (denominator - 1).
# The ones that are reduced are those for which the numerator and denominator
# are relatively prime, that is, for which gcd(numerator, denominator) == 1.
def get_reduced_fraction_count_naively(denominator):
    reduced_fraction_count = 0;
    for numerator in range (1, denominator):
        if get_gcd(numerator, denominator) == 1:
            reduced_fraction_count += 1;
    return reduced_fraction_count;

# This follows the same logic as get_reduced_fraction_count_naively() except
# that there is no loop from 1 to (denominator - 1), which become intractable
# for large denominators. This algorithm starts with the total number of
# reduced fractions as the denominator itself, then subtracts the numbers
# multiples of each prime factor for the denominator that is less than or equal
# to the denominator; this is similar to the approach of the Sieve of
# Eratosthenes. Since this multiply counts some numbers, this algorithm
# compensates by adding back the multiples of the products of the 2-member
# subgroups of prime factors, then by subtracting back the the products of the
# 3-member subgroups, and so on. In general, it subtracts the products of the
# odd-member subgroups, and adds the products of the even-member subgroups.
def get_reduced_fraction_count(denominator):
    reduced_fraction_count = denominator;
    prime_factorization = get_prime_factorization(denominator);
    factor_count = len(prime_factorization);
    factors = [None] * factor_count;
    for i in range(factor_count):
        factors[i] = prime_factorization[i][0];
    for subgroup_size in range(1, factor_count + 1):
        combinations = get_combinations(factors, subgroup_size);
        for combination in combinations:
            factor = 1;
            for element in combination:
                factor *= element;
            term = denominator / factor;
            if subgroup_size % 2 != 0:
                term *= -1;
            reduced_fraction_count += term;
    return reduced_fraction_count;

# Because all the denominators from 2 to N are included, any non-reduced
# fraction would reduce to a fraction already counted in the list for a smaller
# denominator. It therefore suffices to count the number of already reduced
# fractions for each denominator.
total_reduced_fraction_count = 0;
for d in range(2, D + 1):
    # Print a progress indication.
    if d % 10000 == 0:
        print "completed %d of %d" % (d, D);
    total_reduced_fraction_count += get_reduced_fraction_count(d);
print;
print "total_reduced_fraction_count = %d." % total_reduced_fraction_count;

print;
print "Execution time = %f seconds." % (time.time() - start_time);
