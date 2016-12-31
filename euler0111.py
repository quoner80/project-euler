# Primes with runs
# Problem 111
#
# Considering 4-digit primes containing repeated digits it is clear that they cannot all be the same: 1111 is divisible by 11, 2222 is divisible by 22, and so on. But there are nine 4-digit primes containing three ones:
#
#   1117, 1151, 1171, 1181, 1511, 1811, 2111, 4111, 8111
#
# We shall say that M(n, d) represents the maximum number of repeated digits for an n-digit prime where d is the repeated digit, N(n, d) represents the number of such primes, and S(n, d) represents the sum of these primes.
#
# So M(4, 1) = 3 is the maximum number of repeated digits for a 4-digit prime where one is the repeated digit, there are N(4, 1) = 9 such primes, and the sum of these primes is S(4, 1) = 22275. It turns out that for d = 0, it is only possible to have M(4, 0) = 2 repeated digits, but there are N(4, 0) = 13 such cases.
#
# In the same way we obtain the following results for 4-digit primes.
#
#   Digit, d    M(4, d)    N(4, d)    S(4, d)
#   --------    -------    -------    -------
#       0          2          13       67061
#       1          3           9       22275
#       2          3           1        2221
#       3          3          12       46214
#       4          3           2        8888
#       5          3           1        5557
#       6          3           1        6661
#       7          3           9       57863
#       8          3           1        8887
#       9          3           7       48073
#
# For d = 0 to 9, the sum of all S(4, d) is 273700.
#
# Find the sum of all S(10, d).

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

def get_sum_of_primes_with_1_replacement(base_ones, digit_count, base_digit):
    sum_of_primes = 0;
    base = base_digit * base_ones;
    for index in range(digit_count):
        first_test_digit = 0;
        # This prevents testing on a number with a leading 0.
        if index == digit_count - 1:
            first_test_digit = 1;
        for test_digit in range(first_test_digit, 10):
            n = base + ((test_digit - base_digit) * (10 ** index));
            # Still need to check this despite the leading 0 guard above (for when base_digit == 0).
            if n >= 1000000000:
                if is_prime(n):
                    print n;
                    sum_of_primes += n;
    return sum_of_primes;

def get_sum_of_primes_with_2_replacements(base_ones, digit_count, base_digit):
    sum_of_primes = 0;
    base = base_digit * base_ones;
    for index_0 in range(digit_count):
        first_test_digit_0 = 0;
        if index_0 == digit_count - 1:
            first_test_digit_0 = 1;
        # This prevents testing on a number with a leading 0.
        for test_digit_0 in range(first_test_digit_0, 10):
            n_0 = base + ((test_digit_0 - base_digit) * (10 ** index_0));
            for index_1 in range(index_0):
                for test_digit_1 in range(10):
                    n_1 = n_0 + ((test_digit_1 - base_digit) * (10 ** index_1));
                    # Still need to check this despite the leading 0 guard above (for when base_digit == 0).
                    if n_1 >= 1000000000:
                        if is_prime(n_1):
                            print n_1;
                            sum_of_primes += n_1;
    return sum_of_primes;

# To decrease the search space immensely, test each repeated digit first for 1 replacement, then, if needed, for 2. Testing for
# 0 replacements is not necessary because each is divisible by 11. It turns out that testing for 2 replacements is sufficient
# because there is at least 1 prime number for 1 or 2 replacements for each digit.
initialize_primes_lists();
base_ones = 1111111111;
digit_count = int(math.ceil(math.log10(base_ones)));
sum_for_all_base_digits = 0;
for base_digit in range(10):
    m = 9;
    sum_for_base_digit = get_sum_of_primes_with_1_replacement(base_ones, digit_count, base_digit);
    if sum_for_base_digit == 0:
        m = 8;
        sum_for_base_digit = get_sum_of_primes_with_2_replacements(base_ones, digit_count, base_digit);
        if sum_for_base_digit == 0:
            sys.exit('program failed at base_digit %d--need to test for 3 replacements.' % base_digit);
    print 'M(10, %d) = %d.' % (base_digit, m);
    print 'S(10, %d) = %d.' % (base_digit, sum_for_base_digit);
    print;
    sum_for_all_base_digits += sum_for_base_digit;
print 'sum for all 10 digits = %d.' % sum_for_all_base_digits;

print;
print_execution_time();
