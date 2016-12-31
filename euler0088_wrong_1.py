# Product-sum numbers
# Problem 88
#
# A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers, {a1, a2, ... , ak} is called a product-sum number: N = a_1 + a_2 + ... + a_k = a_1 x a_2 x ... x a_k.
#
# For example, 6 = 1 + 2 + 3 = 1 x 2 x 3.
#
# For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number. The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.
#   k = 2:  4 = 2 x 2 = 2 + 2
#   k = 3:  6 = 1 x 2 x 3 = 1 + 2 + 3
#   k = 4:  8 = 1 x 1 x 2 x 4 = 1 + 1 + 2 + 4
#   k = 5:  8 = 1 x 1 x 2 x 2 x 2 = 1 + 1 + 2 + 2 + 2
#   k = 6: 12 = 1 x 1 x 1 x 1 x 2 x 6 = 1 + 1 + 1 + 1 + 2 + 6
#
# Hence for 2 <= k <= 6, the sum of all the minimal product-sum numbers is 4 + 6 + 8 + 12 = 30; note that 8 is only counted once in the sum.
#
# In fact, as the complete set of minimal product-sum numbers for 2 <= k <= 12 is {4, 6, 8, 12, 15, 16}, the sum is 61.
#
# What is the sum of all the minimal product-sum numbers for 2 <= k <= 12000?

import math;
import time;
import sys;

start_time = time.time();

K = 6;
K = 12;
K = 12000;
R = 1 + int(math.log(K, 2));
S_k_r = [None] * (K + 1);
for k in range(K + 1):
    S_k_r[k] = [None] * (R + 1);
    for r in range(R + 1):
        S_k_r[k][r] = [];

def print_execution_time():
    print "Execution time = %f seconds." % (time.time() - start_time);

def calculate_S_k_r(k, r):
    if len(S_k_r[k][r]) > 0:
        return;
    if r == 2:
        d_max = int(math.sqrt(k - 1));
        for d in range(1, d_max + 1):
            if (k - 1) % d == 0:
                S_k_r[k][r].append([d + 1, ((k - 1) / d) + 1]);
        return;
    j_max = (k - (3 * r) + 2) / 2;
    j_min = (2 ** (r - 2)) - r;
    if j_min > j_max:
        return;
    for j in (j_max, j_min - 1, -1):
        for array in S_k_r[j + r][r - 1]:
            numerator = k - r - j;
            denominator = sum(array) + j;
            if numerator % denominator == 0:
                new_array = sorted(array + ([1 + (numerator / denominator)]));
                if not new_array in S_k_r[k][r]:
                    S_k_r[k][r].append(new_array);

for k in range(2, K + 1):
    r_max = 1 + int(math.log(k, 2));
    for r in range(r_max, 1, -1):
        calculate_S_k_r(k, r);

v_min = [sys.maxint] * (K + 1);
for k in range(len(S_k_r)):
    for r in range(len(S_k_r[k])):
        ones = k - r;
        for array in S_k_r[k][r]:
            v = ones + sum(array);
            if v < v_min[k]:
                v_min[k] = v;

v_min_unique = set();
for i in range(2, len(v_min)):
    v_min_unique.add(v_min[i])
    # print i, v_min[i], S_k_r[i];

# print len(v_min_unique);
# print sorted(v_min_unique);
print "sum of minimal product-sum numbers for (2 <= k <= %d) = %d." % (K, sum(v_min_unique));

print_execution_time();
