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

squares = [];
i = 0;
while True:
    square = primes[i] ** 2;
    if square > MAXIMUM:
        break;
    squares.append(square);
    i += 1;

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
print squares;
print len(squares);
print cubes;
print len(cubes);
print tesseracts;
print len(tesseracts);
'''

solutions = set();
for tesseract in tesseracts:
    for cube in cubes:
        for square in squares:
            solution = square + cube + tesseract;
            if solution <= MAXIMUM:
                # print "%d = %d^2 + %d^3 + %d^4" % (solution, primes[squares.index(square)], primes[cubes.index(cube)], primes[tesseracts.index(tesseract)]);
                solutions.add(solution);
# print solutions;
print "solution_count = %d." % len(solutions);

print_execution_time();
