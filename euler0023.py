# Non-abundant sums
#
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import sys;

N = 28123;
# N = 100;

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

# Determine the abundant numbers less than N.
abundant_numbers = [];
abundant_numbers_by_index = [False] * (N + 1);
for n in range(N):
    if n < get_proper_divisors_sum(n):
        abundant_numbers.append(n);
        abundant_numbers_by_index[n] = True;
abundant_numbers_count = len(abundant_numbers);
'''
print abundant_numbers[abundant_numbers_count - 1];
print abundant_numbers[-1];
print abundant_numbers_by_index[abundant_numbers[-1]];
print abundant_numbers_by_index[abundant_numbers[-1] - 1];
'''

total_sum_impossible = 0;
for n in range(1, N + 1):
    i = 0;
    a = abundant_numbers[i];
    sum_impossible = True;
    while a < n:
        b = n - a;
        if abundant_numbers_by_index[b]:
            # print "%d = %d + %d." % (n, a, b);
            sum_impossible = False;
            break;
        i += 1;
        if (i >= abundant_numbers_count):
            break;
        a = abundant_numbers[i];
    if sum_impossible:
        # print "%d cannot be written as the sum of two abundant numbers." % n;
        total_sum_impossible += n;
print total_sum_impossible;












