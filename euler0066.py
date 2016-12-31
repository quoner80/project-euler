# Diophantine equation
#
# Consider quadratic Diophantine equations of the form:
#   x^2 - D * y^2 = 1
#
# For example, when D = 13, the minimal solution in x is 649^2 - 13 * 180^2 = 1.
#
# It can be assumed that there are no solutions in positive integers when D is square.
#
# By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:
#   3^2 - 2 * 2^2 = 1
#   2^2 - 3 * 1^2 = 1
#   9^2 - 5 * 4^2 = 1
#   5^2 - 6 * 2^2 = 1
#   8^2 - 7 * 3^2 = 1
#
# Hence, by considering minimal solutions in x for D <= 7, the largest x is obtained when D = 5.
#
# Find the value of D <= 1000 in minimal solutions of x for which the largest value of x is obtained.

import math;
import time;
import sys;

start_time = time.time();

N = 1000;

# Extended Euclidean algorithm.
# Finds the gcd and the integral solutions to:
#   ax + by = gcd(a, b)
# Source: https://en.wikipedia.org/wiki/Euclidean_algorithm and https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm.
def extended_euclid(a, b):
    r0 = a;
    s0 = 1;
    t0 = 0;
    r1 = b;
    s1 = 0;
    t1 = 1;
    q1 = None;
    while r1 != 0:
        q1 = r0 / r1;
        r2 = r0 % r1;
        s2 = s0 - (q1 * s1);
        t2 = t0 - (q1 * t1);
        # print q1, r2, s2, t2;
        r0 = r1;
        r1 = r2;
        s0 = s1;
        s1 = s2;
        t0 = t1;
        t1 = t2;
    return (r0, s0, t0);

# Find the m closest to sqrt(D) such that k divides (x + ym), i.e. k | (x + ym).
#   kt = x + ym
#   kt - ym = x
#   kt + -ym = x
# extended_euclid(k, -y) will give a solution (g, r, s) such that kr + (-ys) = g, where g = gcd(k, -y).
# It must be that g|x, or there is no solution (this function checks this). So x/g is integral.
#   kr + (-ys) = g
# Multiply by x / g:
#   k(rx/g) + -y(sx/g) = gx/g = x
# This means the following are solutions to the third equation above, kt + -ym = x:
#   t = rx/g, m = sx/g
# Solutions for m will be in the form kt + m' where m' is any solution for m. Since sx/g is a solution for m:
#   m = kt + sx/g
# sx/g will not generally be > 0 and <= k. To get that value:
#   m = kt + ((sx/g) % k)
# To get the m closest to sqrt(D):
#   m = kt + ((sx/g) % k) ~ sqrt(D)
#   kt = sqrt(D) - ((sx/g) % k)
#   t = (sqrt(D) - ((sx/g) % k)) / k
#   m = kt + ((sx/g) % k)
def find_m(D, x, y, k):
    sqrtD = int(round(math.sqrt(D)));
    (g, r, s) = extended_euclid(k, -y);
    if x % g != 0:
        print "Error: %d does not divide %d." % (g, x);
        sys.exit(-1);
    print D, k;
    z = ((s * (x / g)) % k);
    print z;
    t = (sqrtD - z) / k;
    m1 = (k * t) + z;
    m2 = m1 + k;
    print m1, m2;
    if D - (m1 * m1) < (m2 * m2) - D:
        return m1;
    else:
        return m2;

# Source: https://en.wikipedia.org/wiki/Chakravala_method
# Examples from source:
#    3 |  1m + 8   ->   3 |  1m + 2  ->  m =  3t + 1
#    6 |  5m + 41  ->   6 |  5m + 5  ->  m =  6t + 5
#    7 | 11m + 90  ->   7 | 11m + 6  ->  m =  7t + 2
# Own examples:
#   22 |  4m + 6   ->  22 |  4m + 6  ->  m = 22t + 4
#   11 |  2m + 3   ->  11 |  2m + 3  ->  m = 11t + 4
def chakravala(D, x, y, k):
    abs_k = abs(k);
    m = find_m(D, x, y, abs_k);
    x_prime = ((x * m) + (D * y)) / abs_k;
    y_prime = (x + (y * m)) / abs_k;
    k_prime = ((m * m) - D) / k;
    print "m = %d." % m;
    print ((x * m) + (D * y)), abs_k, ((x * m) + (D * y)) % abs_k, x_prime;
    print (x + (y * m)), abs_k, (x + (y * m)) % abs_k, y_prime;
    print (D - (m * m)), k, (D - (m * m)) % k, k_prime;
    return (x_prime, y_prime, k_prime);

x_max = 0;
x_argmax_D = 0;
for D in range(N + 1):
    # Exclude perfect squares.
    if (int(math.sqrt(D)) ** 2) != D:
        x = int(math.sqrt(D));
        y = 1;
        k = (x * x) - D;
        while k != 1:
            (x, y, k) = chakravala(D, x, y, k);
            print x, y, k;
            print;
        print x;
        if x > x_max:
            x_max = x;
            x_argmax_D = D;
        print "----------------------------------------------------------------------------";
print "x_max = %d, x_argmax_D = %d." % (x_max, x_argmax_D);

print;
print "Execution time = %f seconds." % (time.time() - start_time);
