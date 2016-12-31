# Pandigital prime
#
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?

import math;
import sys;
import time;

start_time = time.time();

# Returns the permutations of the "count" chars in each string in "strings".
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

def is_prime(n):
    is_n_prime = True;
    global primes;
    global prime_max;
    prime_factor_max = int(math.ceil(math.sqrt(n)));
    if prime_factor_max > prime_max:
        print "is_prime(%d) failed due to insufficiently large primes table." % n;
        sys.exit(-1);
    for p in primes:
        if p >= n:
            break;
        if n % p == 0:
            is_n_prime = False;
            break;
    return is_n_prime;

# Note that the digits go from 1 to n, i.e. they do _not_ include 0.
# The prime cannot contain all 9 digits 1 through 9 because such a number would be divisible by 3 (digits sum to 45) and therefore not prime.
# The prime cannot contain all 8 digits 1 through 8 because such a number would be divisible by 3 (digits sum to 36) and therefore not prime.
# The upper limit for the n-digit pandigital would therefore be 7654321.
N = 7654321;

# Read the primes from a file.
primes = [];
infile = open("primes.txt", "r");
for line in infile:
    primes.append(int(line));
infile.close();
prime_count = len(primes);
prime_max = primes[-1];
print "known prime count = %d" % prime_count;
print "known prime max   = %d" % prime_max;

S = str(N);
permutations = get_permutations([S], len(S));
for permutation in permutations:
    if is_prime(int(permutation)):
        print permutation;
        break;

print "Execution time = %f seconds." % (time.time() - start_time);
