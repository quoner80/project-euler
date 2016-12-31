# Diophantine reciprocals II
# Problem 110
#
# In the following equation x, y, and n are positive integers.
#
#   1   1   1
#   - + - = -
#   x   y   n
#
# It can be verified that when n = 1260 there are 113 distinct solutions and this is the least value of n for which the total number of distinct solutions exceeds one hundred.
#
# What is the least value of n for which the number of distinct solutions exceeds four million?
#
# NOTE: This problem is a much more difficult version of Problem 108 and as it is well beyond the limitations of a brute force approach it requires a clever implementation.

import sys;
import time;

start_time = time.time();

def print_execution_time():
    print 'Execution time = %f seconds.' % (time.time() - start_time);

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
print;
sieve = [False] * (prime_max + 1);
for prime in primes:
    sieve[prime] = True;

# Returns the prime factorization of n as a list of prime factors; multiply occurring primes occur multiply in the list. For
# example, if n is 2000, the prime factorization is [[2, 4], [5, 3]] since 2000 = 2^4 * 5^3.
def get_prime_factorization(n):
    prime_factorization = [];
    prime_index = 0;
    prime = primes[prime_index];
    while n > 1:
        if n <= prime_max and sieve[n]:
            prime_factorization.append(n);
            break;
        prime = primes[prime_index];
        while n % prime == 0:
            prime_factorization.append(prime);            
            n /= prime;
        prime_index += 1;
        if prime_index >= prime_count:
            print "get_prime_factorization(%d) failed due to insufficiently large primes table." % n;
            sys.exit();
    return prime_factorization;

# From Andreescu, Titu, "An Introduction to Diophantine Equations", Part I, Example 2, Remark:
#   1   1   1
#   - + - = -
#   x   y   n
# is equivalent to (x - n)(y - n) = n^2, and:
#   n^2 = p_1^(2*a_1) * p_2^(2*a_2) * .. * p_k^(2*a_k)
# which has the many positive divisors:
#   (2*a_1 + 1) * (2*a_2 + 1) * .. * (2*a_k + 1)
#
# This is supported by the results from euler0108.py:
#   n =   1260 (factorization = [[2, 2], [3, 2], [5, 1], [7, 1]])                   has  113 solutions.
#   n =   4620 (factorization = [[2, 2], [3, 1], [5, 1], [7, 1], [11, 1]])          has  203 solutions.
#   n =  13860 (factorization = [[2, 2], [3, 2], [5, 1], [7, 1], [11, 1]])          has  338 solutions.
#   n =  27720 (factorization = [[2, 3], [3, 2], [5, 1], [7, 1], [11, 1]])          has  473 solutions.
#   n =  55440 (factorization = [[2, 4], [3, 2], [5, 1], [7, 1], [11, 1]])          has  608 solutions.
#   n =  55440 (factorization = [[2, 4], [3, 2], [5, 1], [7, 1], [11, 1]])          has  608 solutions.
#   n = 110880 (factorization = [[2, 5], [3, 2], [5, 1], [7, 1], [11, 1]])          has  743 solutions.
#   n = 120120 (factorization = [[2, 3], [3, 1], [5, 1], [7, 1], [11, 1], [13, 1]]) has  851 solutions.
#   n = 180180 (factorization = [[2, 2], [3, 2], [5, 1], [7, 1], [11, 1], [13, 1]]) has 1013 solutions.
#   n = 180180 (factorization = [[2, 2], [3, 2], [5, 1], [7, 1], [11, 1], [13, 1]]) has 1013 solutions.
# For example:
#   n = 27720 = 2^3 * 3^2 * 5^1 * 7^1 * 11^1
# has:
#   (2*3 + 1) * (2*2 + 1) * (2*1 + 1) * (2*1 + 1) * (2*1 + 1) = 7 * 5 * 3 * 3 * 3 = 945 total solutions
# For the number of distinct solutions (where 1/x, 1/y and 1/y, 1/x are not distinct), there is the one "middle" solution where
# 1/x == 1/y, and half of the remaining total solutions:
#   1 + ((945 - 1) / 2) = 1 + (944 / 2) = 1 + 472 = 473 distinct solutions

# sys.maxint is only 9223372036854775807, so initialize n_minimum with something much larger. Empirically, 10^99 is sufficient.
n_minimum = 10 ** 99;
n_minimum_arg_max_solution_count = None;
# Per the above argument, for > 4,000,000 distinct solutions, the number of total (non-distinct) solutions is:
#   1 + ((total_solution_count - 1) / 2) > 4,000,000
#   ((total_solution_count - 1) / 2) > 4,000,000 - 1
#   ((total_solution_count - 1) / 2) >= 4,000,000
#   total_solution_count - 1 >= 2 * 4,000,000
#   total_solution_count - 1 >= 2 * 4,000,000 = 8,000,000
#   total_solution_count >= 8,000,000 + 1
#   total_solution_count > 8,000,000
# The relationship between n and the total solution count is not strictly linear, but grossly, the total solution count
# increases as n increases. So, start with 8,000,001 and search to 9,000,000, which is more than enough. Also, the total
# solution count must be odd because all the prime factors must be odd (i.e. 2 is not allowed) because per the above, each
# prime factor must be in the form ((2 * a) + 1).
for total_solution_count in range(8000001, 9000000, 2):
    prime_factorization = get_prime_factorization(total_solution_count);
    # As an optimization, consider only total solution counts with the highest prime factor less than 100, which would
    # correspond to the exponent of the smallest base prime, or 2, since 2^100 = 1.2676506 * 10^30 which is empirically
    # already too large to be part of the smallest n with > 8,000,000 total solutions. (Just guessing gives n values below
    # 10^30).
    if prime_factorization[-1] < 100:
        prime_factor_count = len(prime_factorization);
        # From the factorization of total_solution_count, the smallest n which would produce that count is the one with
        # the smallest base prime, or 2, raised to the largest prime factor of total_solution_count, times the second
        # smallest base prime, or 2, raised to the second largest prime factor of total_solution_count, and so on.
        n = 1;
        for prime_factor_index in range(prime_factor_count - 1, -1, -1):
            prime_factor = prime_factorization[prime_factor_index];
            exponent = (prime_factor - 1) / 2;
            n *= (primes[prime_factor_count - prime_factor_index - 1] ** exponent);
        # print total_solution_count, n, prime_factorization;
        if n < n_minimum:
            n_minimum = n;
            n_minimum_arg_max_solution_count = total_solution_count;
distinct_solution_count = 1 + ((n_minimum_arg_max_solution_count - 1) / 2);
print 'n = %d is the smallest n which gives more than 4 million (%d) distinct solutions.' % (n_minimum, distinct_solution_count);
print;

print_execution_time();
