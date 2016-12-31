# Prime power triples
# Problem 87
#
# The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:
#
#   28 = 2^2 + 2^3 + 2^4
#   33 = 3^2 + 2^3 + 2^4
#   49 = 5^2 + 2^3 + 2^4
#   47 = 2^2 + 3^3 + 2^4
#
# How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?

import math;
import time;

start_time = time.time();

MAXIMUM = 50;
MAXIMUM = 50000000;

# Read the primes from a file.
primes = [];
infile = open("primes.txt", "r");
for line in infile:
    primes.append(int(line));
infile.close();

def print_execution_time():
    print "Execution time = %f seconds." % (time.time() - start_time);

# Optimized over "n in primes" by exiting once the prime tested is greater than n.
def is_prime(n):
    n_is_prime = False;
    for prime in primes:
        if prime == n:
            n_is_prime = True;
            break;
        if prime > n:
            break;
    return n_is_prime;

# Returns the square root if n is a perfect square and the squre root is prime. Returns 0 otherwise.
def get_prime_square_root(n):
    prime_square_root = 0;
    square_root = int(math.sqrt(n));
    if ((square_root ** 2) == n) and is_prime(square_root):
        prime_square_root = square_root;
    return prime_square_root;

cubes = [];
i = 0;
while True:
    cube = primes[i] ** 3;
    if cube > MAXIMUM:
        break;
    cubes.append(cube);
    i += 1;

tesseracts = [];
i = 0;
while True:
    tesseract = primes[i] ** 4;
    if tesseract > MAXIMUM:
        break;
    tesseracts.append(tesseract);
    i += 1;

'''
print cubes;
print len(cubes);
print tesseracts;
print len(tesseracts);
'''

solution_count = 0;
for n in range(MAXIMUM):
    n_determined = False;
    for t in tesseracts:
        n_minus_t = n - t;
        if n_minus_t <= 0:
            break;
        for c in cubes:
            n_minus_t_minus_c = n_minus_t - c;
            if n_minus_t_minus_c <= 0:
                break;
            if get_prime_square_root(n_minus_t_minus_c):
                n_determined = True;
                solution_count += 1;
                # Print every 1000 solutions as a progress indicator.
                if solution_count % 1000 == 0:
                    print n;
                '''
                square_root = get_prime_square_root(n_minus_t_minus_c);
                cube_root = primes[cubes.index(c)];
                tesseract_root = primes[tesseracts.index(t)];
                print "%d = %d^2 + %d^3 + %d^4" % (n, square_root, cube_root, tesseract_root);
                '''
                break;
        if n_determined:
            break;
print;
print "solution_count = %d." % (solution_count);

print_execution_time();
