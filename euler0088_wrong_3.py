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

K= 6;
K = 12;
K = 12000;

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

def extend_partitions(partitions, new_member):
    new_partitions_list = [];
    for partition in partitions:
        new_partition = list(partition);
        new_partition.append(new_member);
        new_partition.sort();
        if not new_partition in new_partitions_list:
            # print new_partition;
            new_partitions_list.append(new_partition);
        previous_member = 0;
        for s in range(len(partition) - 1, -1, -1):
            member = new_partition[s];
            if member != previous_member:
                previous_member = member;
                new_partition = list(partition);
                new_partition[s] *= new_member;
                new_partition.sort();
                if not new_partition in new_partitions_list:
                    # print new_partition;
                    new_partitions_list.append(new_partition);
    return new_partitions_list;

max_integer_partition_size = int(math.log(2 * K, 2));
integer_partitions_list = generate_integer_partitions(max_integer_partition_size);

product_sums = [None] * (K + 1);
for k in range(K + 1):
    product_sums[k] = [];

for n in range(2, (2 * K) + 1):

    # Generate all factorizations of n.
    factorizations = [];
    prime_factorization = get_prime_factorization(n);
    max_exponent = 0;
    max_exponent_prime = 0;
    max_exponent_index = -1;
    prime_factorization_length = len(prime_factorization);
    for index in range(prime_factorization_length):
        prime_and_exponent = prime_factorization[index];
        exponent = prime_and_exponent[1];
        if exponent > max_exponent:
            max_exponent = exponent;
            max_exponent_index = index;
            max_exponent_prime = prime_and_exponent[0];
    del prime_factorization[max_exponent_index];
    integer_partitions = integer_partitions_list[max_exponent];
    for partition in integer_partitions:
        factorization = [];
        partition_index_length = len(partition);
        # Start at index at 1 rather than 0 because partition[0] is always 0.
        for partition_index in range(1, partition_index_length):
            factor_count = partition[partition_index];
            for f in range(factor_count):
                factorization.append(max_exponent_prime ** partition_index);
        factorizations.append(factorization);
    for prime_and_exponent in prime_factorization:
        prime = prime_and_exponent[0];
        exponent = prime_and_exponent[1];
        for e in range(exponent):
            factorizations = extend_partitions(factorizations, prime);
    # print factorizations; print;

    for factorization in factorizations:
        summation = sum(factorization);
        ones_count = n - summation;
        k = len(factorization) + ones_count;
        if k <= K:
            product_sums[k].append(n);

min_product_sum_set = set();
for k in range(2, K + 1):
    min_product_sum = min(product_sums[k]);
    min_product_sum_set.add(min_product_sum);
    print k, min_product_sum, product_sums[k];
print sorted(min_product_sum_set);

'''
for partitions in integer_partitions_list:
    for partition in partitions:
        print get_partition_pretty_string(partition);
    print;
'''

print "sum of minimal product-sum numbers for (2 <= k <= %d) = %d." % (K, sum(min_product_sum_set));

print_execution_time();













