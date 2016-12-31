# Diophantine reciprocals I
# Problem 108
#
# In the following equation x, y, and n are positive integers.
#
#   1   1   1
#   - + - = -
#   x   y   n
#
# For n = 4 there are exactly three distinct solutions:
#
#   1    1   1
#   - + -- = -
#   5   20   4
#
#   1    1   1
#   - + -- = -
#   6   12   4
#
#   1   1   1
#   - + - = -
#   8   8   4
#
# What is the least value of n for which the number of distinct solutions exceeds one-thousand?
#
# NOTE: This problem is an easier version of Problem 110; it is strongly advised that you solve this one first.

import numpy;
import time;

start_time = time.time();

def print_execution_time():
    print 'Execution time = %f seconds.' % (time.time() - start_time);

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
print;
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

# These are not needed in this program but may be useful in future Project Euler programs.
"""
def get_integer_partition_pretty_string(partition):
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
        print "partitions_list[%d] length = %d" % (integer, len(partitions_list[integer]));
    return partitions_list;

# Incorporates the specified factor into the specified factorizations list. For example, [[2, 2], [4]] and 3 become
# [[2, 2, 3], [2, 6], [3, 4], [12]].
def incorporate_factor_into_factorizations(factorizations, factor):
    new_factorizations = [];
    for factorization in factorizations:
        new_factorization = list(factorization);
        new_factorization.append(factor);
        new_factorization.sort();
        if not new_factorization in new_factorizations:
            # print new_factorization;
            new_factorizations.append(new_factorization);
        for s in range(len(factorization) - 1, -1, -1):
            member = new_factorization[s];
            previous_member = member;
            new_factorization = list(factorization);
            new_factorization[s] *= factor;
            new_factorization.sort();
            if not new_factorization in new_factorizations:
                # print new_factorization;
                new_factorizations.append(new_factorization);
    return new_factorizations;

# Generates all factorizations of n.
def generate_factorizations(n):
    factorizations = [];
    prime_factorization = get_prime_factorization(n);
    # Start the prime with the largest exponent, and generate all factors using that prime and exponent by finding all integer
    # partitions of the exponent and creating a factorization by raising the prime to each partition member in each partition.
    # This optimization greatly reduces the number of factors that need to be incorporated into the factorizations in the
    # slower incorporate_factor_into_partitions() steps.
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
    # For the remaining primes, for each factor (each prime separately, e.g. if a prime has an exponent of 3, process that
    # prime separately 3 times), incorporate that factor into the factorizations list.
    for prime_and_exponent in prime_factorization:
        prime = prime_and_exponent[0];
        exponent = prime_and_exponent[1];
        for e in range(exponent):
            factorizations = incorporate_factor_into_factorizations(factorizations, prime);

max_integer_partition_size = 20;
integer_partitions_list = generate_integer_partitions(max_integer_partition_size);
"""

candidates = [];
for twos in range(8):
    a = (2 ** twos);
    for threes in range(4):
        b = (3 ** threes);
        for fives in range(3):
            c = (5 ** fives);
            for sevens in range(3):
                d = (7 ** sevens);
                for elevens in range(2):
                    e = (11 ** elevens);
                    for thirteens in range(2):
                        f = (13 ** thirteens);
                        candidates.append(a * b * c * d * e * f);
candidates.sort();

for N in [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]:
    for n in candidates:
        count = 0;
        x = n + 1;
        while (True):
            if (n * x) % (x - n) == 0:
                count += 1;
                # print x - n, n * x, (n * x) % (x - n), x, (n * x) / (x - n);
                if x == ((n * x) / (x - n)):
                    break;
            x += 1;
        # print n, count;
        if count > N:
            print 'n = %d (factorization = %s) has %d solutions.' % (n, get_prime_factorization(n), count);
            break;
print;

print_execution_time();
