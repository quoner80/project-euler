# Amicable chains
# Problem 95
#
# The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.
#
# Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.
#
# Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:
#
# 12496 -> 14288 -> 15472 -> 14536 -> 14264 (-> 12496 -> ...)
#
# Since this chain returns to its starting point, it is called an amicable chain.
#
# Find the smallest member of the longest amicable chain with no element exceeding one million.

import sys;
import time;

start_time = time.time();

def print_execution_time():
    print "Execution time = %f seconds." % (time.time() - start_time);

# Reads primes from a file, and initializes the Sieve of Eratosthenes.
def load_primes_and_sieve():
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
    return (primes, sieve);

# Returns the prime factorization of n as a list of 2-tuples [p, m] where p is the prime factor and m is the multiplicity of
# that prime factor. For example, if n is 2000, the prime factorization is [[2, 4], [5, 3]] since 2000 = 2^4 * 5^3.
def get_prime_factorization(n, primes, sieve):
    prime_count = len(primes);
    prime_max = primes[-1];
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
            sys.exit("get_prime_factorization(%d) failed due to insufficiently large primes table." % n);
    return prime_factorization;

def get_divisors(n, primes, sieve):
    divisors = [1];
    prime_factorization = get_prime_factorization(n, primes, sieve);
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

def get_proper_divisors(n, primes, sieve):
    proper_divisors = get_divisors(n, primes, sieve);
    # Remove n itself, which is the final element in the sorted list.
    del proper_divisors[-1];
    return proper_divisors;

def get_proper_divisors_sum(n, primes, sieve):
    proper_divisors_sum = 0;
    proper_divisors = get_proper_divisors(n, primes, sieve);
    for i in range(len(proper_divisors)):
        proper_divisors_sum += proper_divisors[i];
    return proper_divisors_sum;

N = 1000000;

# If a number reaches a number exceeding N, that number and all numbers in that sequence have no amicable chain.
#
# If a number reaches a number that already has a chain length, all other numbers (except the number iteslf) in that sequence
# have no amicable chain.
#
# If an amicable chain is discovered, all numbers in the amicable chain have that chain length, but all numbers before the
# start of the chain have no amicable chain.
#
max_chain_length = 0;
longest_chain = [];
chain_lengths = [0] * (N + 1);
(primes, sieve) = load_primes_and_sieve();
print;
for n in range(N + 1):
    number = n;
    sequence = [];
    while True:
        sequence.append(number);
        number = get_proper_divisors_sum(number, primes, sieve);
        if number > N:
            none_sequence_length = len(sequence);
            for i in range(0, none_sequence_length):
                chain_lengths[sequence[i]] = None;
            # print sequence;
            break;
        elif chain_lengths[number] != 0:
            none_sequence_length = len(sequence) - 1;
            for i in range(0, none_sequence_length):
                chain_lengths[sequence[i]] = None;
            # print sequence[:-1];
            break;
        elif number in sequence:
            starting_index = sequence.index(number);
            sequence_length = len(sequence);
            chain_length = sequence_length - starting_index;
            if chain_length > max_chain_length:
                max_chain_length = chain_length;
                longest_chain = sequence[starting_index:];
                print max_chain_length, longest_chain;
            for i in range(0, starting_index):
                chain_lengths[sequence[i]] = None;
            for i in range(starting_index, sequence_length):
                chain_lengths[sequence[i]] = chain_length;
            # print chain_length, sequence;
            break;
print;
print "Smallest member of the longest amicable chain = %d." % min(longest_chain);
print;

print_execution_time();
