# Generates the list of primes at or below max_possible_prime.

import sys;
import time;

start_time = time.time();

max_possible_prime = 10000000000;
max_possible_prime = 1000000000;
#max_possible_prime = 179424674;
#max_possible_prime = 10000000;

sys.stderr.write('max_possible_prime = %d.\n' % max_possible_prime);

wheel_size = 60;

# Arbitrary search limit.
limit = max_possible_prime;

# Initialize the sieve of Atkin.
is_prime = [False] * (limit + 1);

# Set of wheel "hit" positions for a 2/3/5 wheel rolled twice as per the Atkin algorithm.
# s = [1, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49, 53, 59];
s31 = [1, 13, 17, 29, 37, 41, 49, 53];
s32 = [7, 19, 31, 43];
s33 = [11, 23, 47, 59];
s = sorted(s31 + s32 + s33);

# Initialize the sieve with enough wheels to include limit.
# This is not necessary since there is an is_prime list already large enough to contain the sieve at the front end.
"""
w_limit_plus_one = (limit / wheel_size) + 1;
for w in range(w_limit_plus_one):
    for x in s:
        n = (wheel_size * w) + x;
        if n <= limit:
            is_prime[n] = False;
print is_prime;
"""

# Put in candidate primes: integers which have an odd number of representations by certain quadratic forms.

# Algorithm step 3.1, all x's and odd y's:
x = 1;
#n31 = set();
n31 = [];
while True:
    y = 1;
    n = (4 * x * x) + (y * y);
    while n <= limit:
        # print '4*%d^2 + %d^2 = %d' % (x, y, n);
        n31.append(n);
        y += 2;
        n = (4 * x * x) + (y * y);
    if y == 1 and n > limit:
        break;
    x += 1;
for n in n31:
    # print '%d %% %d = %d' % (n, wheel_size, n % wheel_size);
    if n % wheel_size in s31:
        is_prime[n] = not is_prime[n];
sys.stderr.write('Step 3.1 complete.\n');

# Algorithm step 3.2, odd x's and even y's:
x = 1;
#n32 = set();
n32 = [];
while True:
    y = 2;
    n = (3 * x * x) + (y * y);
    while n <= limit:
        # print '3*%d^2 + %d^2 = %d' % (x, y, n);
        n32.append(n);
        y += 2;
        n = (3 * x * x) + (y * y);
    if y == 2 and n > limit:
        break;
    x += 2;
for n in n32:
    # print '%d %% %d = %d' % (n, wheel_size, n % wheel_size);
    if n % wheel_size in s32:
        is_prime[n] = not is_prime[n];
sys.stderr.write('Step 3.2 complete.\n');

# Algorithm step 3.3, even/odd and odd/even combos:
x = 2;
#n33 = set();
n33 = [];
while True:
    y = x - 1;
    n = (3 * x * x) - (y * y);
    while n <= limit and y >= 1:
        # print '3*%d^2 - %d^2 = %d' % (x, y, n);
        n33.append(n);
        y -= 2;
        n = (3 * x * x) - (y * y);
    if y == (x - 1) and n > limit:
        break;
    x += 1;
for n in n33:
    # print '%d %% %d = %d' % (n, wheel_size, n % wheel_size);
    if n % wheel_size in s33:
        is_prime[n] = not is_prime[n];
sys.stderr.write('Step 3.3 complete.\n');

# Eliminate composites by sieving, only for those occurrences on the wheel:
w = -1;
keep_going = True;
while keep_going:
    w += 1;
    for x in s:
        n = (wheel_size * w) + x;
        if n < 7:
            continue;
        if (n * n) > limit:
            keep_going = False;
            break;
        # If n is prime, omit multiples of its square; this is sufficient because square-free composites can't get on this list:
        if is_prime[n]:
            n_squared = n * n;
            keep_going_inner = True;
            w_inner = -1;
            while keep_going_inner:
                w_inner += 1;
                for x_inner in s:
                    c = n_squared * ((wheel_size * w_inner) + x_inner);
                    if c > limit:
                        keep_going_inner = False;
                        break;
                    is_prime[c] = False;

# One sweep to produce a sequential list of primes up to limit:
is_prime[2] = is_prime[3] = is_prime[5] = True;
for i in range(2, len(is_prime)):
    if is_prime[i]:
        print i;

sys.stderr.write('Execution time = %f seconds.\n' % (time.time() - start_time));
