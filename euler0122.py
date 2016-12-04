# Efficient exponentiation
# Problem 122
#
# The most naive way of computing n^15 requires fourteen multiplications:
#   n x n x ... x n = n^15
#
# But using a 'binary' method you can compute it in six multiplications:
#   n    x n   = n^2
#   n^2  x n^2 = n^4
#   n^4  x n^4 = n^8
#   n^8  x n^4 = n^12
#   n^12 x n^2 = n^14
#   n^14 x n   = n^15
#
# However it is yet possible to compute it in only five multiplications:
#   n    x n   = n^2
#   n^2  x n   = n^3
#   n^3  x n^3 = n^6
#   n^6  x n^6 = n^12
#   n^12 x n^3 = n^15
#
# We shall define m(k) to be the minimum number of multiplications to compute n^k; for example m(15) = 5.
# For 1 <= k <= 200, find summation(m(k)).

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
    infile = open('primes_below_2_million.txt', 'r');
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

# Returns the prime factorization of n as a list of prime factors; multiply occurring primes occur multiply in the list. For
# example, if n is 2000, the prime factorization is [[2, 4], [5, 3]] since 2000 = 2^4 * 5^3.
def get_prime_factorization(n):
    global primes;
    global prime_count;
    global prime_max;
    global prime_sieve;
    prime_factorization = [];
    prime_index = 0;
    prime = primes[prime_index];
    while n > 1:
        if n <= prime_max and prime_sieve[n]:
            prime_factorization.append([n, 1]);
            break;
        prime = primes[prime_index];
        exponent = 0;
        while n % prime == 0:
            exponent += 1;            
            n /= prime;
        prime_factorization.append([prime, exponent]);
        prime_index += 1;
        if prime_index >= prime_count:
            print 'get_prime_factorization(%d) failed due to insufficiently large primes table.' % n;
            sys.exit();
    return prime_factorization;

def print_execution_time():
    print 'Execution time = %f seconds.' % (time.time() - start_time);

# Case studies:
#
# k    m(k) example
# ---- ---- -------
# 1    0    n
# 2    1    n x n = n^2
# 3    2    n x n = n^2; n x n^2 = n^3
# 4    2    n x n = n^2; n^2 x n^2 = n^4
# 5    3    n x n = n^2; n^2 x n^2 = n^4; n x n^4 = n^5
# 6    3    n x n = n^2; n^2 x n^2 = n^4; n^2 x n^4 = n^6
# 7    4    n x n = n^2; n^2 x n^2 = n^4; n^2 x n^4 = n^6; n x n^6 = n^7
# 8    3    n x n = n^2; n^2 x n^2 = n^4; n^4 x n^4 = n^8
# 9    4    n x n = n^2; n^2 x n^2 = n^4; n^4 x n^4 = n^8; n x n^8 = n^9
# 10   4    n x n = n^2; n^2 x n^2 = n^4; n^4 x n^4 = n^8; n^2 x n^8 = n^10
# 11   5    n x n = n^2; n^2 x n^2 = n^4; n^4 x n^4 = n^8; n^2 x n^8 = n^10; n x n^10 = n^11
#
# In log space:
#
# k    m(k) example
# ---- ---- -------
# 1    0    1
# 2    1    1+1 = 2
# 3    2    1+1 = 2; 1+2 = 3
# 4    2    1+1 = 2; 2+2 = 4
# 5    3    1+1 = 2; 2+2 = 4; 1+4 = 5
# 6    3    1+1 = 2; 2+2 = 4; 2+4 = 6
# 7    4    1+1 = 2; 2+2 = 4; 2+4 = 6; 1+6 = 7
# 8    3    1+1 = 2; 2+2 = 4; 4+4 = 8
# 9    4    1+1 = 2; 2+2 = 4; 4+4 = 8; 1+8 = 9
# 10   4    1+1 = 2; 2+2 = 4; 4+4 = 8; 2+8 = 10
# 11   5    1+1 = 2; 2+2 = 4; 4+4 = 8; 2+8 = 10; 1+10 = 11

k_max = 10;
initialize_primes_lists();
# Use 1-based indexing so m(k) = m[index]; m[0] is not used.
m = [0] * (k_max + 1);
for k in range(2, k_max + 1):
    print k, get_prime_factorization(k);
print m;

print_execution_time();
