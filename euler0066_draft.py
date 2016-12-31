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

# x1^2 - D * y1^2 = k1
# x2^2 - D * y2^2 = k2
# (x1^2 - D * y1^2) * (x2^2 - D * y2^2) = k1 * k2
#
# Brahmagupta's identity:
#   (x1^2 - D * y1^2)(x2^2 - D * y2^2)
#   = x1^2 * x2^2 - D * x1^2 * y2^2 - D * x2^2 * y1^2 + D^2 * y1^2 * y2^2
#   = (x1^2 * x2^2 + 2 * D * x1 * x2 * y1 * y2 + D^2 * y1^2 * y2^2) - D * x1^2 * y2^2 - D * x2^2 * y1^2 - 2 * D * x1 * x2 * y1 * y2
#   = ((x1 * x2 + D * y1 * y2)^2) - D * (x1^2 * y2^2 + 2 * x1 * x2 * y1 * y2 + x2^2 * y1^2)
#   = ((x1 * x2 + D * y1 * y2)^2) - D * (x1 * y2 + x2 * y1)^2
#
# (x1^2 - D * y1^2)(x2^2 - D * y2^2) = k1 * k2
# ((x1 * x2 + D * y1 * y2)^2) - D * (x1 * y2 + x2 * y1)^2 = k1 * k2
#   x' = (x1 * x2 + D * y1 * y2)
#   y' = (x1 * y2 + x2 * y1)
#   k' = (k1 * k2)
def compose(D, x1, y1, k1, x2, y2, k2):
    abs_k1 = abs(k1);
    x_prime = ((x1 * x2) + (D * y1 * y2)) / abs_k1;
    y_prime = ((x1 * y2) + (x2 * y1)) / abs_k1;
    k_prime = k2 / k1;
    return (x_prime, y_prime, k_prime);

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

def test_extended_euclid(a, b, c):
    (r, s, t) = extended_euclid(a, b);
    print (a, b, (r, s, t), c / r, c % r);
    print;

#test_extended_euclid(7, 11, 6);
#test_extended_euclid(7, -11, 6);
#test_extended_euclid(-7, 11, 6);
#test_extended_euclid(-7, -11, 6);
#test_extended_euclid(22, 4, 6);
#test_extended_euclid(22, -4, 6);
#test_extended_euclid(-22, 4, 6);
#test_extended_euclid(-22, -4, 6);
#test_extended_euclid(3, -1, 8);
#test_extended_euclid(6, -5, 41);
#test_extended_euclid(7, -11, 90);
#test_extended_euclid(22, -4, 6);
#test_extended_euclid(11, -2, 3);
'''
print find_m(61, 8, 1, 3);
print;
print find_m(67, 8, 1, 3);
print;
print find_m(67, 41, 5, 6);
print;
print find_m(67, 90, 11, 7);
'''

'''
print (1071, 462, extended_euclid(1071, 462));
print;
print (240, 46, extended_euclid(240, 46));
print;
print (-46, 240, extended_euclid(-46, 240));
print;
print (240, 46, extended_euclid(240, 46));
'''
#print compose(61, 8, 1, 3, 7, 1, -12);
#print compose(67, 8, 1, -3, 7, 1, -18);
#print chakravala(61, 8, 1, 3); # 7
#print chakravala(67, 8, 1, -3); # 7
#print chakravala(67, 41, 5, 6); # 5

D = 67;
x = 8;
y = 1;
k = -3;
while k != 1:
    (x, y, k) = chakravala(D, x, y, k);
    print x, y, k;
    print;

print "----------------------------------------------------------------------------";

D = 61;
x = 8;
y = 1;
k = 3;
while k != 1:
    (x, y, k) = chakravala(D, x, y, k);
    print x, y, k;
    print;

"""
# x^2 - D * y^2 = 1
#
# x = sqrt(1 + (D * y^2))
def get_x(D, y):
    x_squared = 1 + (D * y * y);
    x = int(math.sqrt(x_squared));
    if (x * x) == x_squared:
        return x;
    else:
        return None;

for D in [2, 3, 5, 6, 7, 13, 92]:
# for D in range(61):
    # Exclude perfect squares.
    if (int(math.sqrt(D)) ** 2) != D and not D in [61, 109, 149]:
        y = 1;
        while True:
            x = get_x(D, y);
            if x != None:
                print "D = %04d: x = %d, y = %d." % (D, x, y);
                break;
            y += 1;
"""

print;
print "Execution time = %f seconds." % (time.time() - start_time);
