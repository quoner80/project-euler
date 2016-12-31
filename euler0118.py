# Pandigital prime sets
# Problem 118
#
# Using all of the digits 1 through 9 and concatenating them freely to form decimal integers, different sets can be formed. Interestingly with the set {2,5,47,89,631}, all of the elements belonging to it are prime.
#
# How many distinct sets containing each of the digits one through nine exactly once contain only prime elements?

import math;
import sys;
import time;

start_time = time.time();

primes = [];
prime_count = None;
prime_max = None;
prime_sieve = None;

# Reads the primes from a file, and initializes the Prime_sieve of Eratosthenes.
def initialize_primes_lists():
    global primes;
    global prime_count;
    global prime_max;
    global prime_sieve;
    infile = open('primes.txt', 'r');
    for line in infile:
        primes.append(int(line));
    infile.close();
    prime_count = len(primes);
    prime_max = primes[-1];
    print 'known prime count = %d' % prime_count;
    print 'known prime max   = %d' % prime_max;
    print;
    prime_sieve = [False] * (prime_max + 1);
    for prime in primes:
        prime_sieve[prime] = True;

def is_prime(n):
    global primes;
    global prime_count;
    global prime_max;
    global prime_sieve;
    is_n_prime = True;
    if n <= prime_max:
        is_n_prime = prime_sieve[n];
    else:
        prime_factor_max = int(math.ceil(math.sqrt(n)));
        if prime_factor_max > prime_max:
            sys.exit('is_prime(%d) failed due to insufficiently large primes table.' % n);
        else:
            for p in primes:
                if p > prime_factor_max:
                    break;
                if n % p == 0:
                    is_n_prime = False;
                    break;
    return is_n_prime;

def print_execution_time():
    print 'Execution time = %f seconds.' % (time.time() - start_time);

# Returns the permutations of the 'count' chars in each string in the list 'strings'.
# For example, for (['123'], 3), returns (['123', '132', '213', '231', '312', '321']).
def get_permutations(strings, count):
    permutations = [];
    for string in strings:
        if count <= 1:
            for char in string:
                permutations.append(char);
        else:
            for c in range(len(string)):
                char = string[c];
                stringlet = string[:c] + string[(c + 1):];
                stringlet_permutations = get_permutations([stringlet], count - 1);
                for p in range(len(stringlet_permutations)):
                    permutations.append(char + stringlet_permutations[p]);
    return permutations;

pandigital_prime_sets = set();

def find_pandigital_prime_sets(string, prefix_length, history):
    prefix = None;
    if prefix_length != 0:
        prefix = int(string[:prefix_length]);
    string_length = len(string);
    if string_length == prefix_length:
        if is_prime(int(string)):
            history = list(history)
            history.append(prefix);
            # Sort the list in order to find duplicates.
            history.sort();
            # Convert the history list to a string, which is hashable, so it can be added to a set which eliminates duplicates.
            # print history;
            pandigital_prime_sets.add(str(history));
    elif (prefix_length == 0) or is_prime(prefix):
        root = string[prefix_length:];
        root_length = string_length - prefix_length;
        if prefix_length != 0:
            history = list(history)
            history.append(prefix);
        for next_prefix_length in range(1, root_length + 1):
            find_pandigital_prime_sets(root, next_prefix_length, history);

strings = ['123456789'];
# strings = ['12345'];
initialize_primes_lists();
string_length = len(strings[0]);
permutations = get_permutations(strings, string_length);
# find_pandigital_prime_sets('254789631', 0, []);
for permutation in permutations:
    find_pandigital_prime_sets(permutation, 0, []);
"""
print;
for pandigital_prime_set in pandigital_prime_sets:
    print pandigital_prime_set;
print;
"""
print len(pandigital_prime_sets);
print;
print_execution_time();
