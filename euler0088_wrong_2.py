# Product-sum numbers
# Problem 88
#
# A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers, {a1, a2, ... , ak} is called a product-sum number: N = a_1 + a_2 + ... + a_k = a_1 x a_2 x ... x a_k.
#
# For example, 6 = 1 + 2 + 3 = 1 x 2 x 3.
#
# For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number. The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.
#   k = 2:  4 = 2 x 2 = 2 + 2
#   k = 3:  6 = 1 x 2 x 3 = 1 + 2 + 3
#   k = 4:  8 = 1 x 1 x 2 x 4 = 1 + 1 + 2 + 4
#   k = 5:  8 = 1 x 1 x 2 x 2 x 2 = 1 + 1 + 2 + 2 + 2
#   k = 6: 12 = 1 x 1 x 1 x 1 x 2 x 6 = 1 + 1 + 1 + 1 + 2 + 6
#
# Hence for 2 <= k <= 6, the sum of all the minimal product-sum numbers is 4 + 6 + 8 + 12 = 30; note that 8 is only counted once in the sum.
#
# In fact, as the complete set of minimal product-sum numbers for 2 <= k <= 12 is {4, 6, 8, 12, 15, 16}, the sum is 61.
#
# What is the sum of all the minimal product-sum numbers for 2 <= k <= 12000?

import math;
import time;

start_time = time.time();

K = 12;

def print_execution_time():
    print "Execution time = %f seconds." % (time.time() - start_time);

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

def get_partition_pretty_string(partition):
    pretty_string = "[";
    for integer in range(len(partition)):
        cardinality = partition[integer];
        if cardinality > 0:
            for i in range(cardinality):
                pretty_string += (str(integer) + " ");
            pretty_string = pretty_string[:-1];
            pretty_string += " ";
    pretty_string = pretty_string[:-1];
    pretty_string += "]";
    return pretty_string;

def generate_integer_partitions(integer_maximum):
    partitions_list = [[], [[0, 1]]];
    integer = 1;
    while integer < integer_maximum:
        integer += 1;
        previous_partitions = partitions_list[-1];
        partitions = list();
        for previous_partition in previous_partitions:
            partition = list(previous_partition);
            partition[1] += 1;
            # print partition;
            partitions.append(partition);
        for previous_partition in previous_partitions:
            partition_length = len(previous_partition);
            for i in range(partition_length):
                partition = list(previous_partition);
                if partition[i] > 0:
                    partition[i] -= 1;
                    if i + 1 == partition_length:
                        partition += [1];
                    else:
                        partition[i + 1] += 1;
                    if not partition in partitions:
                        # print partition;
                        partitions.append(partition);
        # print partitions;
        partitions_list.append(partitions);
        print "partitions_list[%d] = %d" % (integer, len(partitions_list[integer]));
    return partitions_list;

partition_size_max = int(math.log(2 * K, 2))
partitions_list = generate_integer_partitions(partition_size_max);
"""
for partitions in partitions_list:
    for partition in partitions:
        print get_partition_pretty_string(partition);
    print;
"""

class PrimeFactor:
    prime = None;
    exponent = None;
    combination_count = None;
    divisor = None;
    def __init__(self, prime, exponent, total_remaining_combination_count):
        self.prime = prime;
        self.exponent = exponent;
        self.combination_count = len(partitions_list[exponent]);
        self.divisor = total_remaining_combination_count / self.combination_count;
    def __str__(self):
        return "(p=%d;e=%d;c=%d;d=%d)" % (self.prime, self.exponent, self.combination_count, self.divisor);
    def __repr__(self):
        return  repr(str(self));

product_sums = [None] * (K + 1);
for k in range(K + 1):
    product_sums[k] = [];
for n in range(2, (2 * K) + 1):
    prime_factorization = get_prime_factorization(n);
    print n, prime_factorization;
    total_combination_count = 1;
    for prime_and_exponent in prime_factorization:
        exponent = prime_and_exponent[1];
        total_combination_count *= len(partitions_list[exponent]);
    prime_factors = [];
    total_remaining_combination_count = total_combination_count;
    for prime_and_exponent in prime_factorization:
        prime = prime_and_exponent[0];
        exponent = prime_and_exponent[1];
        prime_factor = PrimeFactor(prime, exponent, total_remaining_combination_count);
        total_remaining_combination_count = prime_factor.divisor;
        prime_factors.append(prime_factor);
    print prime_factors;
    for c in range(total_combination_count):
        factors = [];
        for prime_factor in prime_factors:
            partition_index = (c / prime_factor.divisor) % prime_factor.combination_count;
            partition = partitions_list[prime_factor.exponent][partition_index];
            # print partition;
            for integer in range(len(partition)):
                exponent = partition[integer];
                factor = prime_factor.prime ** integer;
                for e in range(exponent):
                    factors.append(factor);
        summation = sum(factors);
        ones = n - summation;
        k = len(factors) + ones;
        print k, ones, summation, factors;
        if k <= K:
            product_sums[k].append(n);
    print;

for i in range(K + 1):
    print product_sums[i];

print "sum of minimal product-sum numbers for (2 <= k <= %d) = %d." % (K, 0);

print_execution_time();













