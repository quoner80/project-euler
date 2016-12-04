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
# Use 1-based indexing so m(k) = m[index]; m[0] is not used. Initialize m[1] = 0.
m = [0] * (k_max + 1);
for k in range(2, k_max + 1):
    # The final addition must be some addition of 2 terms which sums to k.
    # The minimal addition count at most k_max which you would get by adding k_max 1's to get k_max.
    addition_count_min = k_max;
    for term_1 in range(1, (k / 2) + 1):
        term_2 = k - term_1;
        # The number of additions is 1 (for the final addition) plus m[term_1] plus m[term_2].
        addition_count = 1 + m[term_1] + m[term_2];
        print term_1, term_2, addition_count;
        if addition_count_min > addition_count:
            addition_count_min = addition_count;
    print addition_count_min;
    m[k] = addition_count_min;
    print;
print m;

print_execution_time();
