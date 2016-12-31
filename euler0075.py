# Singular integer right triangles
#
# It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.
#
#   12 cm: ( 3,  4,  5)
#   24 cm: ( 6,  8, 10)
#   30 cm: ( 5, 12, 13)
#   36 cm: ( 9, 12, 15)
#   40 cm: ( 8, 15, 17)
#   48 cm: (12, 16, 20)
#
# In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.
#
#   120 cm: (30, 40, 50), (20, 48, 52), (24, 45, 51)
#
# Given that L is the length of the wire, for how many values of L <= 1,500,000 can exactly one integer sided right angle triangle be formed?

import math;
import time;

start_time = time.time();

def get_gcd(a, b):
    r = a % b;
    while r != 0:
        a = b;
        b = r;
        r = a % b;
    return b;

L = 1500000;

# Generate all the primitive Pythagorean triples with lengths greater than 2 and less than or equal to L.
triples = [0] * (L + 1);
primitive_triples_count = 0;
for l in range(2, L + 1, 2):
    # This optimization avoids the Pythagorean triple calculations for lengths that have already been shown to have more than
    # one triple, but at the cost of not generating some primitive triples.
    if triples[l] <= 1:
    # if True:
        # From https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple, the following generates all primitive
        # triples:
        #   a = m^2 - n^2
        #   b = 2mn
        #   c = m^2 + n^2
        # where m > n, m and n are coprime, and m - n is odd.
        #
        # To determine upper limit for m, first note that any one side of a triangle must be less than 1/2 the perimeter:
        #   c < l/2
        # Since c = m^2 + n^2:
        #   m^2 + n^2 < l/2
        # Since n^2 >= 0:
        #   m^2 < m^2 + n^2 < l/2
        #   m < sqrt(l/2)
        for m in range(1, int(math.sqrt(l / 2)) + 1):
            # From above:
            #   l = a + b + c = m^2 - n^2 + 2mn + m^2 + n^2 = 2(m^2) + 2mn = 2m(m + n)
            # Solving for n:
            #   2m(m + n) = l
            #   m + n = l/2m
            #   n = (l/2m) - m
            m_2 = 2 * m;
            if l % m_2 == 0:
                l_over_m_2 = l / m_2;
                if m < l_over_m_2:
                    n = l_over_m_2 - m;
                    if m > n and (m + n) % 2 != 0:
                        if get_gcd(m, n) == 1:
                            primitive_triples_count += 1;
                            # Increment the triples count for l and all multiples of l.
                            for i in range(l, L + 1, l):
                                triples[i] += 1;
                            # Set this to False not to display the generated Pythagorean triples.
                            if True:
                                m_squared = m * m;
                                n_squared = n * n;
                                a = m_squared - n_squared;
                                b = 2 * m * n;
                                c = m_squared + n_squared;
                                if a > b:
                                    temp = a;
                                    a = b;
                                    b = temp;
                                print "%7d: %7d %7d %7d" % (l, a, b, c);
        # This optimization, akin to the one above, seems like it should work, but doesn't.
        '''
            if triples[l] > 1:
                break;
        if triples[l] > 1:
            break;
        '''

singlular_triples_count = 0;
for i in range(len(triples)):
    # print i, triples[i];
    if triples[i] == 1:
        # print "length %d is singular" % i;
        singlular_triples_count += 1;

print;
print "primitive_triples_count = %d." % primitive_triples_count;
print "singlular_triples_count = %d." % singlular_triples_count;

print;
print "Execution time = %f seconds." % (time.time() - start_time);
